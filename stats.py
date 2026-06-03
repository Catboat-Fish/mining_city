import json

game_data = {
    "city": {
        "name": "Testopia",
        "turn": 1,
    },

    "resources": {
        "coal": 20,
        "iron": 10,
        "food": 50,
        "wood": 20,
        "tools": 2,
    },

    "stations": {
        "furnace": {
            "workers": 0,
            "deployed": 0,
            "size": 0,
            "queue": 0,
            "disabled": 0
        },
        "farm": {
            "workers": 0,
            "deployed": 0,
            "size": 20,
            "queue": 0,
            "disabled": 0
        },
        "coal_mine": {
            "workers": 0,
            "deployed": 0,
            "size": 10,
            "queue": 0,
            "disabled": 0
        },
        "iron_mine": {
            "workers": 0,
            "deployed": 0,
            "size": 10,
            "queue": 0,
            "disabled": 0
        },
        "factory": {
            "workers": 0,
            "deployed": 0,
            "size": 10,
            "queue": 0,
            "disabled": 0
        },
        "construction": {
            "workers": 0,
            "deployed": 0,
            "size": 10,
            "queue": 0,
            "disabled": 0
        },
        "lumber": {
            "workers": 0,
            "deployed": 0,
            "size": 10,
            "queue": 0,
            "disabled": 0
        },
        "housing": {
            "workers": 0,
            "deployed": 0,
            "size": 12,
            "queue": 0,
            "disabled": 0
        }
    },

    "upgrade_cost" : {
        "farm": {
            "wood": 10,
            "tools": 5
        },
        "coal_mine": {
            "coal": 5,
            "iron": 5,
            "wood": 5,
            "tools": 5
        },
        "iron_mine": {
            "coal": 5,
            "iron": 10,
            "wood": 5,
            "tools": 10
        },
        "factory": {
            "coal": 10,
            "iron": 20,
            "wood": 10,
            "tools": 10
        },
        "construction": {
            "wood": 5,
            "tools": 5
        },
        "lumber": {
            "wood": 5,
            "tools": 5
        },
        "housing": {
            "wood": 3
        }
    },

    "living": {
        "free_workers": 8,
        "residents": 2,
        "teenagers": 0,
        "children": 0,
        "fetuses": 0
    },

    "social_disasters": { # WIP
        "no_chance"
        "minor_chance": 0,
        "moderate_chance": 0,
        "major_chance": 0,
        "shortage": {
            "status": False,
            "pop_at_start": 0,
            "pop_reduction": 0.00,
            "factory_reduction": 0
        },
        "unrest": 0
    },

    "natural_disasters": { # WIP
        "chance": 0.00,
    }
}


# NOTES
    # housing and furnace shouldn't have workers
    # workers are unused, deployed are used
    # size is amount there, queue is being built
    