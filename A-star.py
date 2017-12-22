Infinity = 100000
COLUMNS = 5
ROWS = 5
node = {
    "x"     : 0,
    "y"     : 0,
    "gScore": Infinity,
    "hScore": Infinity,
    "fScore": Infinity,
    "isWall": 0,
    "cameFrom": None
}

def a_star(start, end):

    closedSet = []
    openSet   = []
