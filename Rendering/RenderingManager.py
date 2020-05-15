import pygame


class RenderingManager:
    action_frames = []

    @staticmethod
    def add_action_frame(action_frame):
        RenderingManager.action_frames.append(action_frame)

    @staticmethod
    def remove_action_frame(action_frame):
        RenderingManager.action_frames.remove(action_frame)

    @staticmethod
    def set_action_frames(action_frames):
        RenderingManager.action_frames = action_frames

    @staticmethod
    def reset_action_frames():
        RenderingManager.action_frames = []

    @staticmethod
    def render():
        for action_frame in RenderingManager.action_frames:
            action_frame.window.fill(action_frame.bg_color)
            for rendering_component in action_frame.get_rendering_components():
                if rendering_component.rotation:
                    rendering_component.sprite = \
                        pygame.transform.rotate(rendering_component.sprite, rendering_component.rotation)
                rendering_component.sprite.set_colorkey((255, 0, 255))
                action_frame.window.blit(rendering_component.sprite, rendering_component.position.to_tup())
        pygame.display.update()
