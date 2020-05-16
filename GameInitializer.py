from FrameActionsManager import FrameActionsManager
from GameClock import GameClock
from GameManager import GameManager
from ActionProviders.BotActionProvider import BotActionProvider
from ActionProviders.PlayerActionProvider import PlayerActionProvider
from Rendering.RenderingManager import RenderingManager
from Model.Vector import Vector
from Rendering.ResourceManager import ResourceManager


class GameInitializer:

    @staticmethod
    def start_game(game_settings):
        if game_settings.is_bot_game:
            bot_input = BotActionProvider()
            player_input = None
        else:
            bot_input = None
            player_input = PlayerActionProvider()
        frame_actions_manager = \
            FrameActionsManager(game_settings.rendering_enabled, bot_input, player_input)
        game_manager = GameManager(Vector(game_settings.board_size, game_settings.board_size))
        RenderingManager.add_action_frame(game_manager.get_action_frame())
        ResourceManager.initialize_score_bar(game_settings.board_size * 40)
        clock = GameClock(frame_actions_manager, game_manager)

        clock.start_game()
