import pygame


class RenderingManager:

    def __init__(self):
        self.action_frames = []
        self.converted_sprites = set()

    def add_action_frame(self, action_frame):
        self.action_frames.append(action_frame)
        self.append_converted_sprites(action_frame.get_sprites())

    def remove_action_frame(self, action_frame):
        self.action_frames.remove(action_frame)

    def set_action_frames(self, action_frames):
        self.action_frames = action_frames

    def reset_action_frames(self):
        self.action_frames = []

    def append_converted_sprites(self, sprites):
        for sprite in sprites:
            if sprite not in self.converted_sprites:
                sprite = sprite.convert()
                sprite.set_colorkey((255, 0, 255))
                self.converted_sprites.add(sprite)

    def render(self):
        for action_frame in self.action_frames:
            action_frame.window.fill(action_frame.bg_color)
            for rendering_component in action_frame.get_rendering_components():
                if rendering_component.rotation:
                    rendering_component.sprite = \
                        pygame.transform.rotate(rendering_component.sprite, rendering_component.rotation)
                rendering_component.sprite.set_colorkey((255, 0, 255))
                action_frame.window.blit(rendering_component.sprite, rendering_component.position.to_tup())
        pygame.display.update()
