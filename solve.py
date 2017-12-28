from time import time
from copy import deepcopy
from queue import Queue

def print_solve(name, board, gen, rep, exp, dur):
    print(name)
    print("Solution: " + board.getDirections())
    print("Nodes Generated: " + str(gen))
    print("Nodes Repeated: " + str(rep))
    print("Nodes Explored: " + str(exp))
    print("Duration: " + str(dur) + " secs")


# Depth-first search: https://en.wikipedia.org/wiki/Depth-first_search
def dfs(board):
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
                    print_solve("DFS", child, nodes_created, nodes_repeated, len(explored), end - start)
                    return child

        elif (node in explored):
            nodes_repeated += 1
    if len(path) == 0:
        print("No solution found")
        return board


# Breadth-First Search:
def bfs(board):
    start = time()
    nodes_created = 1
    nodes_repeated = 0
    frontier = Queue()
    frontierSet = set()
    frontier.put(board)
    frontierSet.add(board)

    explored = set()

    while len(frontierSet) > 0:
        node = frontier.get()
        frontierSet.remove(node)

        moves = node.moves_available()
        for m in moves:
            child = deepcopy(node)
            nodes_created += 1
            child.move(m)
            if child.is_win():
                end = time()
                print_solve("BFS", child, nodes_created, nodes_repeated, len(explored), end - start)
                return child
            if (child not in explored) and (not child.is_stuck):
                frontier.put(child)
                frontierSet.add(child)
                explored.add(child)
                nodes_created += 1
            elif (child in explored):
                nodes_repeated += 1

    if len(frontierSet) == 0:
        print("No solution found")
        return board








