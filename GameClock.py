import pygame

from RenderingManager import RenderingManager


class GameClock:
    def __init__(self, input_provider, game_manager, rendering_manager):
        self.input_provider = input_provider
        self.game_manager = game_manager
        self.rendering_manager = rendering_manager

    def start_game(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(10)
            input = self.input_provider.retrieve_input(self.game_manager.get_current_game_state())
            self.game_manager.simulate_move(input)
            self.rendering_manager.render()