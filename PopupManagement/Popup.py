import pygame
from Rendering.RenderPacket import RenderPacket
from Model.Vector import Vector


class Popup:

    def __init__(self, position, dimensions, message_sprite, back_button, retry_button):
        self.position = position
        self.rect = pygame.Surface((dimensions.x * 40, dimensions.y * 40))
        self.rect.fill((50, 50, 50))
        self.message_sprite = message_sprite
        self.back_button = back_button
        self.retry_button = retry_button

    def check_click(self, click_position):
        if self.back_button.contains_position(click_position // Vector(40, 40)):
            return True
        elif self.retry_button.contains_position(click_position // Vector(40, 40)):
            return False

    def get_rendering_components(self):
        return [
                   RenderPacket(self.rect, Vector(0, self.position.y)),
                   RenderPacket(self.message_sprite, self.position + Vector(1, 1))
               ] + \
               [button_component for button in [self.back_button, self.retry_button] for button_component in button.get_rendering_components()]
