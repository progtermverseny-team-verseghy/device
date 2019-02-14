import uasyncio as asyncio
from components.state import Type
from components.wifi import scanStartHandler, scanCompleteHandler, updateWifiAPWithPassiveHandler,
from components.button import buttonOneTask, buttonTwoTask
from components.led import setBottomLayoutHandler, setTopLayoutHandler
from components.minigame import startMinigameHandler, resetMinigameHandler
from store import Store


def initialize(type):
    store = Store()

    store.dispatch("state", "setType", type)

    loop = asyncio.get_event_loop()

    # WIFI
    loop.create_task(scanCompleteHandler(store))
    loop.create_task(scanStartHandler(store))

    # STATE

    # MINIGAME
    loop.create_task(startMinigameHandler(store))
    loop.create_task(resetMinigameHandler(store))

    # LED
    loop.create_task(setBottomLayoutHandler(store))
    loop.create_task(setTopLayoutHandler(store))

    # BUTTON
    loop.create_task(buttonOneTask(store))
    loop.create_task(buttonTwoTask(store))


    loop.run_forever()


initialize(
    Type["SURVIVOR"]
)
