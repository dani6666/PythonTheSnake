from Model.Vector import Vector
from ActionProviders.MouseActionProvider import MouseActionProvider
from PopupManagement.PopupType import PopupType
from PopupManagement.PopupAction import PopupAction

import pygame


class PopupHandler:

    def __init__(self, popup):
        self.popup = popup

    def handle_popup(self):
        events = pygame.event.get()
        key_events = [e for e in events if e.type == pygame.KEYDOWN]
        click = MouseActionProvider.get_click_position(events)
        if click:
            if self.popup.buttons[0].contains_position(click // Vector(40, 40)):
                return PopupAction.return_to_menu
            elif self.popup.buttons[1].contains_position(click // Vector(40, 40)):
                if self.popup.type == PopupType.game_ended:
                    return PopupAction.restart_game
                else:
                    return PopupAction.resume_game
        if self.popup.type == PopupType.game_pause and pygame.K_SPACE in [e.key for e in key_events]:
            return PopupAction.resume_game
        return PopupAction.idle
