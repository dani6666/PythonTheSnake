import pygame


class RenderingManager:

    def __init__(self):
        self.action_frames = []
        self.converted_sprite_classes = set()

    def add_action_frame(self, action_frame):
        self.action_frames.append(action_frame)
        self.append_converted_sprite_classes(action_frame.possible_sprites_providers)

    def remove_action_frame(self, action_frame):
        self.action_frames.remove(action_frame)

    def set_action_frames(self, action_frames):
        self.action_frames = action_frames

    def reset_action_frames(self):
        self.action_frames = []

    def append_converted_sprite_classes(self, classes):
        for c in classes:
            if c not in self.converted_sprite_classes:
                c.convert_sprites()
                self.converted_sprite_classes.add(c)

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
