from GameClock import GameClock
from GameManager import GameManager
from PlayerInputProvider import PlayerInputProvider
from RenderingManager import RenderingManager
from Vector import Vector


class GameInitializer:

    def start_game(self, game_settings):
        input_provider = PlayerInputProvider()
        game_manager = GameManager(Vector(12, 12))
        rendering_manager = RenderingManager()
        rendering_manager.add_action_frame(game_manager.get_action_frame())
        clock = GameClock(input_provider, game_manager, rendering_manager)

        clock.start_game()