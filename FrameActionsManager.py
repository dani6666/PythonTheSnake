import threading
import pygame

from Rendering.RenderingManager import RenderingManager
from ActionProviders.QuitHandler import QuitHandler
from ActionProviders.PauseActionProvider import PauseActionProvider
from Model.SpecialAction import SpecialAction


class FrameActionsManager:

    def __init__(self, rendering_enabled, bot_action_provider, player_action_provider):
        self.rendering_enabled = rendering_enabled
        self.bot_action_provider = bot_action_provider
        self.player_action_provider = player_action_provider

    def carry_frame_actions(self, game_state):
        QuitHandler.check_quit()
        events = [e for e in pygame.event.get() if e.type == pygame.KEYDOWN]
        if PauseActionProvider.check_pause(events):
            return SpecialAction.game_paused
        thread = None

        if self.bot_action_provider:
            thread = threading.Thread(target=self.bot_action_provider.start_thinking, args=(game_state,))
            thread.start()

        if self.rendering_enabled:
            RenderingManager.render()

        if self.player_action_provider:
            return self.player_action_provider.retrieve_input(events)

        if self.bot_action_provider:
            thread.join()
            return self.bot_action_provider.retrieve_input()

    def pass_lost_game_info(self, score):
        self.bot_action_provider.inform_about_lose(score)
