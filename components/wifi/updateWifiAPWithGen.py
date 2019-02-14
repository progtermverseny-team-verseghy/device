import network


async def updateWifiAPWithGen(store):
    apInterface = network.WLAN(network.AP_IF)
    apInterface.active(True)

    while True:
        await store.get("wifi", "updateWifiAPWithGen")
        store.clear("wifi", "updateWifiAPWithGen")


