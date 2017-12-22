import pygame, os
from pygame.locals import *
from spritesheet import spritesheet

level = open('levels/level.xsb', 'r')
level_content = level.read()
level.close()

LEVEL_W = level_content.find('\n')
level_content = level_content.replace('\n', '')
LEVEL_SIZE = len(level_content)
LEVEL_H = LEVEL_SIZE // LEVEL_W
ListMap = []*

W, H = 400, 400
G_SIZE = 10
loop = True

window = pygame.display.set_mode((W, H))
background = pygame.image.load('img/background.jpg').convert()
loop = 1

Sheet = spritesheet()
char9 = Sheet.get_img('Character1.png', G_SIZE)

def handleEvents():
    for event in pygame.event.get():
        if event.type == QUIT:
            loop = 0
def draw():
    window.blit(background, (0, 0))

    window.blit(char9, (0, 0))
    # Refresh the window
    pygame.display.flip()

# while loop:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             loop = 0
#         if event.type == KEYDOWN:
#             keys[event.key] = True
#         if event.type == KEYUP:
#             keys[event.key] = False
#
#     draw()