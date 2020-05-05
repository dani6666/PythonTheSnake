from Vector import Vector
from RenderPacket import RenderPacket
import pygame
import copy


class Apple:

    sprite = pygame.image.load("resources/apple.png")

    def __init__(self, position=Vector(0, 0)):
        self.position = position

    def change_pos(self, position):
        self.position = position

    def get_pos(self):
        return self.position

    @staticmethod
    def get_sprites():
        return [Apple.sprite]

    def get_rendering_components(self):
        return [RenderPacket(Apple.sprite, copy.deepcopy(self.position))]
