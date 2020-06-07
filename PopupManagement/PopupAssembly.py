from PopupManagement.Popup import Popup
from Menu.Button import Button
from Model.Vector import Vector
from Rendering.ResourceManager import ResourceManager
from PopupManagement.Reason import Reason
from PopupManagement.PopupType import PopupType


class PopupAssembly:

    @staticmethod
    def get_standard_finish_popup(position, length, reason):

        if reason == Reason.game_pause:
            message_sprite = ResourceManager.msg_pause
            back_button = Button(position + Vector(3, 3), Vector(1, 1), False, "", sprite=ResourceManager.button_back)
            resume_button = Button(position + Vector(7, 3), Vector(1, 1), False, "",
                                   sprite=ResourceManager.button_resume)

            return Popup(PopupType.game_pause, position, Vector(length, 5), message_sprite,
                         [back_button, resume_button])

        back_button = Button(position + Vector(3, 3), Vector(1, 1), False, "", sprite=ResourceManager.button_back)
        retry_button = Button(position + Vector(7, 3), Vector(1, 1), False, "", sprite=ResourceManager.button_retry)

        if reason == Reason.game_lost:
            message_sprite = ResourceManager.msg_lose
        elif reason == Reason.game_won:
            message_sprite = ResourceManager.msg_win
        elif reason == Reason.tie:
            message_sprite = ResourceManager.msg_tie
        else:
            message_sprite = ResourceManager.msg_px_wins[reason]

        return Popup(PopupType.game_ended, position, Vector(length, 5), message_sprite, [back_button, retry_button])
