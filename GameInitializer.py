from FrameActionsManager import FrameActionsManager
from GameClock import GameClock
from GameManager import GameManager
from InputProviders.BotInputProvider import BotInputProvider
from InputProviders.PlayerInputProvider import PlayerInputProvider
from Rendering.RenderingManager import RenderingManager
from Model.Vector import Vector
from Rendering.ResourceManager import ResourceManager


class GameInitializer:

    def start_game(self, game_settings):
        if game_settings.is_bot_game:
            frame_actions_manager=FrameActionsManager(game_settings.rendering_enabled, BotInputProvider(), None)
        else:
            frame_actions_manager = FrameActionsManager(game_settings.rendering_enabled, None, PlayerInputProvider())
        game_manager = GameManager(Vector(12, 12))
        RenderingManager.add_action_frame(game_manager.get_action_frame())
        ResourceManager.initialize_score_bar(12 * 40)
        clock = GameClock(frame_actions_manager, game_manager)

        clock.start_game()
