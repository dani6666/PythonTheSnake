import copy

import pygame

from Model.Vector import Vector
from Rendering.RenderPacket import RenderPacket


class Text:

    def __init__(self, position, text):
        Text.text_font = pygame.font.Font(None, 30)
        self.text_image = Text.text_font.render(text, 1, pygame.Color('white'))
        self.position = position

    def get_rendering_components(self):
        return [RenderPacket(self.text_image, Vector(self.position.x + 0.3, self.position.y + 0.4))]
