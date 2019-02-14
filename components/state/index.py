GameState = {
    "NONE": 0,
    "FREE": 1,
    "MINIGAME": 2,
    "DOWNED": 3,
    "DEAD": 4
}

Type = {
    "NONE": 0,
    "SURVIVOR": 1,
    "KILLER": 2,
    "GENERATOR": 3,
    "GATE": 4
}

class State:
    state = {
        "type": Type["NONE"],
        "gen": {
            0: False,
            1: False,
            2: False,
            3: False,
            4: False,
            5: False,
        },
        "gate": {
            0: False,
            1: False
        },
        "gamestate": GameState["NONE"],
        "downed": 0,
        "percentage": 0,
        "minigamesucceeded": False
    }

    def __init__(self, newtype: Type):
        self.state["type"] = newtype
        self.state["gamestate"] = GameState["FREE"]

    def parseWifiString(self, statestring):
        state = {
            "type": Type["NONE"],
            "gen": {
                0: False,
                1: False,
                2: False,
                3: False,
                4: False,
                5: False,
            },
            "gate": {
                0: False,
                1: False
            },
            "gamestate": GameState["NONE"],
            "downed": 0,
            "percentage": 0,
            "minigamesucceeded": False
        }
        for i in range(0, len(statestring)):
            c = statestring[i]
            if i == 0 and c != "$": return None
            if i == 1 and c != "$": return None
            if i == 2 and c != "$": return None
            if i == 3: state["type"] = int(c)
            if i == 4 and c == "1": state["gen"][0] = True
            if i == 5 and c == "1": state["gen"][1] = True
            if i == 6 and c == "1": state["gen"][2] = True
            if i == 7 and c == "1": state["gen"][3] = True
            if i == 8 and c == "1": state["gen"][4] = True
            if i == 9 and c == "1": state["gen"][5] = True
            if i == 10: state["percentage"] += int(c) * 10
            if i == 11: state["percentage"] += int(c)
            if i == 12 and c == "1": state["minigamesucceeded"] = True

        print(state)
        return state

    def updateFromWifi(self, statestring):
        self.state = self.parseWifiString(statestring)

