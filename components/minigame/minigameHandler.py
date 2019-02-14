async def startMinigameHandler(store):
    while True:
        await store.get("minigame", "startMinigame")

        if False:
            store.dispatch("minigame", "resetMinigame")


async def resetMinigameHandler(store):
    while True:
        await store.get("minigame", "resetMinigame")
        store.clear("minigame", "startMinigame")
