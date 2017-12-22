from board import Board



class Sokoban:

    '''
    Sokoban classic game
    '''

    def new_board(self, filename):
        ''' Create a new board '''
        b = Board([])

        with open(filename, 'r') as f:
            read_data = f.read()
            lines = read_data.split('\n')
            height = len(lines)
            width = 0
            x = 0
            y = 0
            for line in lines:
                if len(line) > width:
                    width = len(line)
                for char in line:
                    # adds Spots to beard's sets according to the level
                    if char == '#':
                        b.add_wall(x, y)
                    elif char == '.':
                        b.add_goal(x, y)
                    elif char == '$':
                        b.add_box(x, y)
                    elif char == '@':
                        b.set_player(x, y)
                    elif char == '+':
                        b.set_player(x, y)
                        b.add_goal(x, y)
                    elif char == '*':
                        b.add_box(x, y)
                        b.add_goal(x, y)
                    x += 1
                y += 1
                x = 0
            # Check if there is a player in the board
            if hasattr(b, 'player'):
                b.height = int(height)
                b.width = int(width)
                return b
            else:
                print("Board does not have a player")
                return None

