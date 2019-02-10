import uasyncio as asyncio
import machine
from state import Type, State, wifihandler
from wifi import Scanner


def initialize(type):
    state = State(type)
    scanner = Scanner()

    loop = asyncio.get_event_loop()
    loop.create_task(scanner.scanningTask())
    loop.create_task(wifihandler.wifiHandler(scanner.scannFinished, state))
    loop.run_forever()


pin = machine.Pin(2, machine.Pin.OUT)


initialize(
    Type["SURVIVOR"]
)
