async def setBottomLayoutHandler(store):
    while True:
        value = await store.get("led", "setTopLayout")
        # TODO: Implement it with actual led
        store.clear("led", "setTopLayout")
