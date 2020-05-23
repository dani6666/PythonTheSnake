import threading

from Rendering.RenderingManager import RenderingManager
from ActionProviders.QuitHandler import QuitHandler


class FrameActionsManager:

    def __init__(self, rendering_enabled, bot_action_provider, player_action_provider):
        self.rendering_enabled = rendering_enabled
        self.bot_action_provider = bot_action_provider
        self.player_action_provider = player_action_provider

    def carry_frame_actions(self, game_state):
        QuitHandler.check_quit()
        thread = None

        if self.bot_action_provider:
            thread = threading.Thread(target=self.bot_action_provider.start_thinking, args=(game_state,))
            thread.start()

        if self.rendering_enabled:
            RenderingManager.render()

        if self.player_action_provider:
            return self.player_action_provider.retrieve_input()

        if self.bot_action_provider:
            thread.join()
            return self.bot_action_provider.retrieve_input()
