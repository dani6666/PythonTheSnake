import copy

import pygame

from Rendering.RenderPacket import RenderPacket


class Button:
    sprite = pygame.image.load("resources/body.png")

    def __init__(self, position, size, is_marked):
        self.is_marked = is_marked
        self.size = size
        self.position = position

    def contains_posision(self, position):
        return self.position.x <= position.x < self.position.x + self.size.x and \
               self.position.y <= position.y < self.position.y + self.size.y

    @staticmethod
    def convert_sprites():
        Button.sprite = Button.sprite.convert()
        Button.sprite.set_colorkey((255, 0, 255))

    def get_rendering_components(self):
        return [RenderPacket(Button.sprite, copy.deepcopy(self.position))]