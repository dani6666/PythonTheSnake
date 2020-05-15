from Model.Vector import Vector
from Rendering.RenderPacket import RenderPacket
import copy

from Rendering.ResourceManager import ResourceManager


class Apple:

    def __init__(self, position=Vector(0, 0)):
        self.position = position

    def change_pos(self, position):
        self.position = position

    def get_pos(self):
        return self.position

    def get_rendering_components(self):
        return [RenderPacket(ResourceManager.apple, copy.deepcopy(self.position))]
