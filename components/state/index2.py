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

async def saveTypeHandler(store):
    type = await store.get("state", "setType")
    state["type"] = type


async def changeStateHandler(store, key, value):

async def queryStateHandler(state):