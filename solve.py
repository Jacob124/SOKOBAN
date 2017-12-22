from time import time
from copy import deepcopy


def print_solve(board, gen, rep, exp, dur):
    print('Depth-first Search')
    print("Solution: " + board.getDirections())
    print("Nodes Generated: " + str(gen))
    print("Nodes Repeated: " + str(rep))
    print("Nodes Explored: " + str(exp))
    print("Duration: " + str(dur) + " secs")


# Depth-first search: https://en.wikipedia.org/wiki/Depth-first_search
def solve_level_dfs(board):
    start = time()
    nodes_created = 1
    nodes_repeated = 0
    path = set()
    path.add(board)

    explored = set()

    while len(path) > 0:
        node = path.pop()

        if (node not in explored) and (not node.is_stuck()):
            explored.add(node)

            moves = node.moves_available()
            i = 0
            lmoves = len(moves)
            while (i < lmoves):
                m = moves[i]
                i += 1
                child = deepcopy(node)
                nodes_created += 1
                child.move(m)
                path.add(child)
                if child.is_win():
                    end = time()
                    print_solve(child, nodes_created, nodes_repeated, len(explored), end - start)
                    return child

        elif (node in explored):
            nodes_repeated += 1
    if len(path) == 0:
        print("No solution found")
        return board








