from .submodules import wifiEvents, stateEvents, minigameEvents, ledEvents, buttonEvents


class Store:
    def __init__(self):
        self._state = {
            "wifi": wifiEvents,
            "state": stateEvents,
            "minigame": minigameEvents,
            "led": ledEvents,
            "button": buttonEvents
        }

    def dispatch(self, modulename, eventname, value):
        self._state[modulename][eventname].set(value)

    def clear(self, modulename, eventname):
        self._state[modulename][eventname].clear()

    def get(self, modulename, eventname):
        return self._state[modulename][eventname]
