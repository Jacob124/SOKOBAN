from spot import Spot


class Direction:
    '''
    Contains a Spot object and a char
    '''

    def __init__(self, spot, char):
        self.spot = spot
        self.char = char

    def __str__(self):
        return self.char
