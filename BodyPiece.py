from Vector import Vector
from RenderPacket import RenderPacket
import pygame
import copy


class BodyPiece:

    sprite = pygame.image.load("resources/body.png")
    fat_sprite = pygame.image.load("resources/fatbody.png")

    def __init__(self, position=Vector(0, 0)):
        self.position = position
        self.fat = False

    def change_pos(self, position):
        self.position = position

    def get_pos(self):
        return self.position

    @staticmethod
    def get_sprites():
        return [BodyPiece.sprite, BodyPiece.fat_sprite]

    def get_rendering_components(self):
        if self.fat:
            return RenderPacket(BodyPiece.fat_sprite, copy.deepcopy(self.position))
        else:
            return RenderPacket(BodyPiece.sprite, copy.deepcopy(self.position))
