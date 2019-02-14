import network


async def updateWifiAPWithPassiveHandler(store):
    apInterface = network.WLAN(network.AP_IF)
    apInterface.active(True)

    while True:
        await store.get("wifi", "updateWifiAPWithPassive")
        store.clear("wifi", "updateWifiAPWithPassive")

