from Model.Vector import Vector
from Rendering.RenderPacket import RenderPacket

from Rendering.ResourceManager import ResourceManager


class BodyPiece:

    def __init__(self, position=Vector(0, 0), num=0):
        self.position = position
        self.fat = False
        self.num = num

    def change_pos(self, position):
        self.position = position

    def get_pos(self):
        return self.position

    def get_rendering_components(self):
        if self.fat:
            return RenderPacket(ResourceManager.snake_fatbodies[self.num], self.position + Vector(0, 1))
        else:
            return RenderPacket(ResourceManager.snake_bodies[self.num], self.position + Vector(0, 1))
