from Model.Vector import Vector
from Rendering.RenderPacket import RenderPacket
import copy

from Rendering.ResourceManager import ResourceManager


class BodyPiece:

    def __init__(self, position=Vector(0, 0)):
        self.position = position
        self.fat = False

    def change_pos(self, position):
        self.position = position

    def get_pos(self):
        return self.position

    def get_rendering_components(self):
        if self.fat:
            return RenderPacket(ResourceManager.snake_fat_body, copy.deepcopy(self.position))
        else:
            return RenderPacket(ResourceManager.snake_body, copy.deepcopy(self.position))
