import network
from state import State
from .asny import Event
import uasyncio as asyncio

class Scanner:
    scannerInterface = None
    scannFinished = Event()

    def __init__(self):
        self.scannerInterface = network.WLAN(network.STA_IF)
        self.scannerInterface.active(True)

    async def scanningTask(self, state):
        while True:
            self.scannFinished.set(self.scannerInterface.scan())
            await asyncio.sleep(5)

