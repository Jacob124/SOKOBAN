import os, pygame
from xml.etree import ElementTree

class Spritesheet():
    def __init__(self):
        self.sheet = pygame.image.load('img/sprites.png').convert_alpha()
        self.xml = os.path.abspath('img/sprites.xml')
        self.dom = ElementTree.parse(self.xml)
        self.imgsXml = self.dom.findall('SubTexture')

    def get_img(self, name, size):
        img_data = None
        for i in self.imgsXml:
            if i.attrib["name"] == name:
                img_data = i.attrib
                break

        if img_data:

            rect = pygame.Rect((
                int(img_data["x"]),
                int(img_data["y"]),
                int(img_data["width"]),
                int(img_data["height"])))

            new_img = pygame.Surface(rect.size, pygame.SRCALPHA, 32).convert_alpha()
            new_img.blit(self.sheet, (0, 0), rect)
            new_img = pygame.transform.scale(new_img, (size, size))
            return new_img
        else:
            print('No sprite with name of', name, 'in spritesheet!')
