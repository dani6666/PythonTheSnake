import asyncio

import pygame

from Rendering.RenderingManager import RenderingManager


class GameClock:
    def __init__(self, frame_actions_manager, game_manager):
        self.frame_actions_manager = frame_actions_manager
        self.game_manager = game_manager
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

    def start_game(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(10)
            input = self.loop.run_until_complete(
                self.frame_actions_manager.carry_frame_actions(self.game_manager.get_current_game_state()))
            self.game_manager.simulate_move(input)
            RenderingManager.render()
