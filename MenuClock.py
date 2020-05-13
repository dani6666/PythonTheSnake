import pygame


class MenuClock:
    def __init__(self, input_provider, main_menu_window, rendering_manager, game_initializer):
        self.input_provider = input_provider
        self.main_menu_window = main_menu_window
        self.rendering_manager = rendering_manager
        self.game_initializer = game_initializer

    def start_app(self):
        clock = pygame.time.Clock()

        game_starting = False
        while not game_starting:
            clock.tick(10)
            click = self.input_provider.get_click_position()
            if click is not None:
                game_starting = self.main_menu_window.handle_mouse_click(click)
            self.rendering_manager.render()

        game_settings = self.main_menu_window.get_game_settings()
        self.game_initializer.start_game(game_settings)