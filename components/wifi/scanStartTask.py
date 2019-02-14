import uasyncio as asyncio

async def scanStartTask(store):
    while True:
        store.dispatch("wifi", "scanStart")
        asyncio.sleep(5)
