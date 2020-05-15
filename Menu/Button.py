import copy

import pygame

from Model.Vector import Vector
from Rendering.RenderPacket import RenderPacket
from Rendering.ResourceManager import ResourceManager


class Button:

    def __init__(self, position, size, is_marked, text, sprite=None):
        self.text_image = ResourceManager.text_font.render(text, 1, pygame.Color('white'))
        self.is_marked = is_marked
        self.size = size
        self.position = position
        self.sprite = sprite

    def contains_position(self, position):
        return self.position.x <= position.x < self.position.x + self.size.x and \
               self.position.y <= position.y < self.position.y + self.size.y

    def get_rendering_components(self):
        if self.sprite:
            button_image = self.sprite
        else:
            if self.is_marked:
                button_image = ResourceManager.snake_body
            else:
                button_image = ResourceManager.button_inactive
        return [RenderPacket(button_image, copy.deepcopy(self.position)),
                RenderPacket(self.text_image, Vector(self.position.x + 1.5, self.position.y + 0.4))]
