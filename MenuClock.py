import pygame

from Rendering.RenderingManager import RenderingManager


class MenuClock:
    def __init__(self, input_provider, main_menu_window, game_initializer):
        self.input_provider = input_provider
        self.main_menu_window = main_menu_window
        self.game_initializer = game_initializer

    def start_app(self):
        clock = pygame.time.Clock()

        game_starting = False
        while not game_starting:
            clock.tick(10)
            click = self.input_provider.get_click_position()
            if click:
                game_starting = self.main_menu_window.handle_mouse_click(click)
            RenderingManager.render()

        RenderingManager.reset_action_frames()
        game_settings = self.main_menu_window.get_game_settings()
        self.game_initializer.start_game(game_settings)
