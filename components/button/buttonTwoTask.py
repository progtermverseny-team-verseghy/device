import uasyncio as asyncio


async def buttonTwoTask(store):
    store.dispatch("button", "buttonTwoPressed", False)
    while True:
        if False: # TODO: Implement it with actual button
            store.dispatch("button", "buttonTwoPressed", False)
        await asyncio.sleep(1 / 30)
