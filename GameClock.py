import pygame

from Rendering.RenderingManager import RenderingManager


class GameClock:
    def __init__(self, input_provider, game_manager):
        self.input_provider = input_provider
        self.game_manager = game_manager

    def start_game(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(10)
            input = self.input_provider.retrieve_input(self.game_manager.get_current_game_state())
            self.game_manager.simulate_move(input)
            RenderingManager.render()
