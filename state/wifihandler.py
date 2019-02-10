from .index import State

async def wifiHandler(event, state: State):
    while True:
        await event
        wifilist = event.value()
        for wifi in wifilist:
            state.updateFromWifi(wifi[0].decode("utf-8"))
        event.clear()
