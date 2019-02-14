import network


async def scanningTask(store):
    scannerInterface = network.WLAN(network.STA_IF)
    scannerInterface.active(True)

    while True:
        await store.get("wifi", "scanStart")
        store.dispatch("wifi", "scanComplete", scannerInterface.scan())
        store.clear("wifi", "scanStart")

