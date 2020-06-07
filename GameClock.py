import pygame

from PopupManagement.Reason import Reason
from Rendering.RenderingManager import RenderingManager
from ActionProviders.QuitHandler import QuitHandler
from PopupManagement.PopupHandler import PopupHandler
from PopupManagement.PopupAction import PopupAction


class GameClock:

    def __init__(self, frame_actions_manager, game_manager):
        self.frame_actions_manager = frame_actions_manager
        self.game_manager = game_manager

    def start_game(self, is_bot_game, rendering_enabled):
        clock = pygame.time.Clock()
        end_reason = None
        done = False

        while not done:

            while end_reason is None:
                if rendering_enabled:
                    clock.tick(10)
                actions = self.frame_actions_manager.carry_frame_actions(self.game_manager.get_current_game_state())
                end_reason = self.game_manager.simulate_move(actions)

            if not is_bot_game or end_reason == Reason.game_pause:
                self.game_manager.call_popup(end_reason)
                popup = self.game_manager.popup
                popup_closed = False
                popup_handler = PopupHandler(popup)

                while not popup_closed:
                    clock.tick(10)
                    QuitHandler.check_quit()
                    popup_response = popup_handler.handle_popup()
                    if popup_response:
                        if popup_response == PopupAction.return_to_menu:
                            RenderingManager.reset_action_frames()
                            popup_closed = True
                            done = True
                        elif popup_response == PopupAction.restart_game:
                            end_reason = None
                            self.game_manager.reset()
                            popup_closed = True
                        else:
                            end_reason = None
                            self.game_manager.unpause()
                            popup_closed = True

                    RenderingManager.render()
            else:
                end_reason = None
                self.frame_actions_manager.pass_lost_game_info(self.game_manager.get_game_score())
                self.game_manager.reset()
