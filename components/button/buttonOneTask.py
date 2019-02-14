import uasyncio as asyncio



async def buttonOneTask(store):
    store.dispatch("button", "buttonOnePressed", False)
    while True:
        if False: # TODO: Implement it with actual button
            store.dispatch("button", "buttonOnePressed", False)
        await asyncio.sleep(1 / 30)
