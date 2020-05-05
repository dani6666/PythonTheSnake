from RenderPacket import RenderPacket
import pygame


class ActionFrame:

    def __init__(self, possible_sprites_providers, window, grid_size, components=[], bg_color=(150, 150, 150)):
        self.possible_sprites_providers = possible_sprites_providers
        if not window:
            window = pygame.display.set_mode((40 * 12, 40 * 12))
            pygame.display.set_caption("Python the Snake")
        self.window = window
        self.grid_size = grid_size
        self.components = components
        self.bg_color = bg_color

    def add_rendering_component(self, component):
        self.components.append(component)

    def remove_rendering_component(self, component):
        self.components.remove(component)

    def apply_absolute_cords(self, rendering_component):
        pos = rendering_component.position
        pos.x *= self.grid_size[0]
        pos.y *= self.grid_size[1]
        return rendering_component

    def get_rendering_components(self):
        return [self.apply_absolute_cords(rc) for c in self.components for rc in c.get_rendering_components()]
