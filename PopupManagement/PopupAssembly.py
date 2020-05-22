from PopupManagement.Popup import Popup
from Menu.Button import Button
from Model.Vector import Vector
from Rendering.ResourceManager import ResourceManager
from PopupManagement.Reason import Reason


class PopupAssembly:

    @staticmethod
    def get_standard_finish_popup(position, length, reason):

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

        return Popup(position, Vector(length, 5), message_sprite, [back_button, retry_button])
