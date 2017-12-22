import pygame
pygame.init()

class Button():
    def __init__(self, rect, text, color):
        self.rect = rect
        self.text = text
        self.color = color
        self.font = pygame.font.Font(pygame.font.get_default_font(), 12)
        self.center = (rect[0] + (rect[2]/2), rect[1] + (rect[3]/2))

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)

        text = self.font.render(self.text, 0, (0, 0, 0))
        text_rect = text.get_rect(center=self.center)
        window.blit(text, text_rect)

    def mouse_on(self):
        mouse = pygame.mouse.get_pos()
        return (self.rect[0]+self.rect[2] > mouse[0] > self.rect[0]) and (self.rect[1] + self.rect[3] > mouse[1] > self.rect[1])
