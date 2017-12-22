from spot import Spot
from direction import Direction

L = Direction(Spot(-1, 0), 'l')
R = Direction(Spot(1, 0), 'r')
U = Direction(Spot(0, -1), 'u')
D = Direction(Spot(0, 1), 'd')
directions = [U, R, D, L]


class Board:
    def __init__(self, dir_list):
        self.dir_list = dir_list
        self.walls = set()
        self.goals = set()
        self.boxes = set()
        self.fboxes = frozenset() # since set is not hashable
        self.player = None
        self.width = 0
        self.height = 0
        self.cost = 1  # used for heuristics

    """ Override class functions """
    def __eq__(self, other):
        """ Used for comparing board instances """
        return self.boxes.issubset(other.boxes) and self.player == other.player

    def __hash__(self):
        """
        http://www.asmeurer.com/blog/posts/what-happens-when-you-mess-with-hashing-in-python/
        hashes by frozenset of box positions
        """
        return hash((self.fboxes, self.player))

    """ Define helper functions"""
    def add_wall(self, x, y):
        self.walls.add(Spot(x, y))

    def add_goal(self, x, y):
        self.goals.add(Spot(x, y))

    def add_box(self, x, y):
        self.boxes.add(Spot(x, y))

    def set_player(self, x, y):
        self.player = Spot(x, y)

    def moves_available(self):
        moves = []
        for d in directions:
            if self.player + d.spot not in self.walls:
                if self.player + d.spot in self.boxes:
                    # Check if there is a box or wall behind it
                    if self.player + d.spot.double() not in self.boxes.union(self.walls):
                        moves.append(d)
                else:
                    moves.append(d)
        return moves

    def move(self, direction):
        """ Moves player and box """
        p = self.player + direction.spot
        if p in self.boxes:
            self.boxes.remove(p)
            self.boxes.add(p + direction.spot)
            # Update frozen set
            self.fboxes = frozenset(self.boxes)
        self.player = p
        self.cost += 1
        self.dir_list.append(direction)

    def is_win(self):
        return self.goals.issubset(self.boxes)

    def is_stuck(self):
        for b in self.boxes:
            if b not in self.goals:
                i = 0
                for d in directions:
                    sp = b + d.spot
                    if sp in self.walls:
                        if i + 1 > len(directions) - 1:
                            i = -1
                        nsp = b + directions[i + 1].spot
                        if nsp in self.walls:
                            return True
                    i += 1
        return False

    def getDirections(self):
        """ Outputs the list of directions taken for the solution """
        chars = ''
        for d in self.dir_list:
            chars += d.char
            chars += ', '
        return chars