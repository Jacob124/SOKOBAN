import pygame, os
from pygame.locals import *
from sokoban import Sokoban
from direction import Direction
from spot import Spot
from solve import *
from spritesheet import Spritesheet
from button import Button


W, H = 400, 400
G_SIZE = 20
window = pygame.display.set_mode((W, H))

game = Sokoban()
level_name = 'levels/mod1.xsb'
board = game.new_board(level_name)
G_SIZE = int(min(W, H) / max(board.width, board.height))
sheet = Spritesheet()
green = (20, 236, 136)
blue = (72, 136, 240)


L = Direction(Spot(-1, 0), 'l')
R = Direction(Spot(1, 0), 'r')
U = Direction(Spot(0, -1), 'u')
D = Direction(Spot(0, 1), 'd')
directions = [U, D, L, R]

solve_button = Button((W-60, 10, 50, 20), "Solve", blue)
restart_button = Button((W-60, 40, 50, 20), "Restart", green)


def draw_player(board, window, last_dir):
    l = last_dir.char
    name = 'Character7.png'
    if l == 'l':
        name = 'Character1.png'
    elif l == 'r':
        name = 'Character2.png'
    elif l == 'u':
        name = 'Character7.png'
    else:
        name = 'Character4.png'

    char_img = sheet.get_img(name, G_SIZE)
    window.blit(char_img, (board.player.x * G_SIZE, board.player.y * G_SIZE))


def display_board(board, window, dir):
    # Define the images
    floor_img = sheet.get_img('GroundGravel_Concrete.png', G_SIZE)
    wall_img = sheet.get_img('Wall_Brown.png', G_SIZE)
    box_img = sheet.get_img('Crate_Blue.png', G_SIZE)
    goal_img = sheet.get_img('EndPoint_Yellow.png', G_SIZE)

    # draw the floor
    for i in range(board.width):
        for j in range(board.height):
            x = i * G_SIZE
            y = j * G_SIZE
            window.blit(floor_img, (x, y))

    for g in board.goals:
        x = g.x * G_SIZE
        y = g.y * G_SIZE
        window.blit(goal_img, (x, y))

    for w in board.walls:
        x = w.x * G_SIZE
        y = w.y * G_SIZE
        window.blit(wall_img, (x, y))

    for b in board.boxes:
        x = b.x * G_SIZE
        y = b.y * G_SIZE
        window.blit(box_img, (x, y))

    draw_player(board, window, dir)


def draw(dir):
    display_board(board, window, dir)
    # Draw solve button
    mouse = pygame.mouse.get_pos()
    solve_button.draw(window)
    restart_button.draw(window)
    # Refresh the window
    pygame.display.flip()


draw(directions[1])
dirList = []
moveIndex = 0
clock = pygame.time.Clock()

loop = 1
while loop:
    clock.tick(5)
    for event in pygame.event.get():
        if event.type == QUIT:
            loop = 0
        if event.type == MOUSEBUTTONDOWN:
            if solve_button.mouse_on():
                print("Solving...")
                moveIndex = 0
                dirList = solve_level_dfs(board).dir_list
            if restart_button.mouse_on():
                print("\n"*60)
                board = game.new_board(level_name)
                draw(directions[1])

        if event.type == KEYDOWN:
            dir = None
            if event.key == K_DOWN:
                dir = directions[1]
            elif event.key == K_UP:
                dir = directions[0]
            elif event.key == K_LEFT:
                dir = directions[2]
            elif event.key == K_RIGHT:
                dir = directions[3]
            if dir:

                moves = board.moves_available()
                valid_dir = False
                for move in moves:
                    if move.spot == dir.spot:
                        valid_dir = True
                if valid_dir:
                    board.move(dir)

                if board.is_win():
                    print("YOU HAVE WON!!!")
                    loop = 0
                draw(dir)
            if event.key == K_s:
                print("Solving...")
                dirList = solve_level_dfs(board).dir_list
                moveIndex = 0

    if len(dirList) > 0:
        dir = dirList.pop(0)
        board.move(dir)
        draw(dir)