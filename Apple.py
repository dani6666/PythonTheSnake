from Vector import Vector
from RenderPacket import RenderPacket
import pygame


class Apple:

    sprite = pygame.image.load("resources/apple.png")
    sprite.set_colorkey((255, 0, 255))

    def __init__(self, position=Vector(0, 0)):
        self.position = position
        self.fat = False

    def change_pos(self, position):
        self.position = position

    def get_pos(self):
        return self.position

    @staticmethod
    def get_sprites():
        return [Apple.sprite]

    def get_rendering_components(self):
        return [RenderPacket(Apple.sprite, self.position)]
