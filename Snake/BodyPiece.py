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
    def convert_sprites():
        BodyPiece.fat_sprite = BodyPiece.fat_sprite.convert()
        BodyPiece.sprite = BodyPiece.sprite.convert()
        BodyPiece.fat_sprite.set_colorkey((255, 0, 255))
        BodyPiece.sprite.set_colorkey((255, 0, 255))

    def get_rendering_components(self):
        if self.fat:
            return RenderPacket(BodyPiece.fat_sprite, copy.deepcopy(self.position))
        else:
            return RenderPacket(BodyPiece.sprite, copy.deepcopy(self.position))
