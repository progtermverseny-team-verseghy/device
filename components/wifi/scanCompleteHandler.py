async def scanCompleteHandler(store):
    while True:
        wifilist = await store.get("wifi", "scanComplete")
        for wifi in wifilist:
            store.dispatch("state", "updatePassiveState", wifi[0].decode("utf-8"))

        store.clear("wifi", "scanComplete")
