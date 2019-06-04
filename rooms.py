
# structure defining the rooms in the game. Try adding more rooms to the game!
rooms = {
    "Tavern": {
        "description": "\nYou're in a cozy tavern warmed by an open fire. This seems like a nice place to relax and socialize\n",
        "exits": {"outside": "Outside Tavern"},
    },
    "Outside Tavern": {
        "description": "\nYou're standing outside a tavern. It's raining. To you left is a wooden out house.\n",
        "exits": {"inside": "Tavern", "behind tavern": "Behind Tavern", "to bathroom": "Out House"},
    },
    "Behind Tavern": {
        "description": "\nYou go behind the tavern building and find an overhang to protect you from rain.\n",
        "exits": {"front": "Outside Tavern"},
    },
    "Out House": {
        "description": "\nAs you open the door flys swarm disperse out. You step inside anyway...\n",
        "exits": {"outside": "Outside Tavern"},
    }
}
