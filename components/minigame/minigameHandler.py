minigameState = {}

import machine
import random
import neopixel

LEFT_BUTTON_PIN = 14
RIGHT_BUTTON_PIN = 12

async def startMinigameHandler(store):

    stepButton = machine.Pin(LEFT_BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
    killButton = machine.Pin(RIGHT_BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_UP)

    while True:
        await store.get("minigame", "startMinigame")

        if stepButton.value():
            minigameState["selected"] = (minigameState["selected"] + 1) % 8
            continue

        if killButton.value():
            selected = minigameState["selected"]
            if minigameState["dots"][selected]==True:
                minigameState["dots"][selected] = False
                continue
            else:
                store.dispatch("minigame", "resetMinigameLevel")
                continue

        if False:
            store.dispatch("minigame", "resetMinigame")


LED_PIN = 13

COLORS = {
    True: (0, 255, 0),
    False: (0,0,0),
    "SELECTED": (255, 0, 0),
}

async def drawMinigameTask(store):
    pixels = neopixel.NeoPixel(machine.Pin(LED_PIN), 16)

    while True:
        await store.get("minigame", "startMinigame")
        for i in range(8,16):
            pixels[i] = COLORS[minigameState["dots"][i]]
        pixels[minigameState["selected"]] = COLORS["SELECTED"]
        pixels.write()



async def resetMinigameLevelHandler(store):
    while True:
        await store.get("minigame", "resetMinigameLevel")

        minigameState["dots"] = [random.choice([True, False]) for _ in range(8)]
        minigameState["selected"] = random.choice(range(8))



async def resetMinigameHandler(store):
    while True:
        await store.get("minigame", "resetMinigame")
        store.clear("minigame", "startMinigame")

        minigameState["levels"] = 0
        store.dispatch("minigame","resetMinigameLevel")
