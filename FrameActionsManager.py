import threading

from Rendering.RenderingManager import RenderingManager


class FrameActionsManager:

    def __init__(self, rendering_enabled, bot_input_provider, player_input_provider, quit_input_provider):
        self.rendering_enabled = rendering_enabled
        self.bot_input_provider = bot_input_provider
        self.player_input_provider = player_input_provider
        self.quit_input_provider = quit_input_provider

    def carry_frame_actions(self, game_state):
        self.quit_input_provider.check_quit()
        thread = None

        if self.bot_input_provider:
            thread = threading.Thread(target=self.bot_input_provider.start_thinking, args=game_state)
            thread.start()

        if self.rendering_enabled:
            RenderingManager.render()

        if self.player_input_provider:
            return self.player_input_provider.retrieve_input()

        if self.bot_input_provider:
            thread.join()
            return self.bot_input_provider.retrieve_input()
