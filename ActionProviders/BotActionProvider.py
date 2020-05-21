from Bot.BotManager import BotManager
from Model.Vector import Vector


class BotActionProvider:

    bool = True

    def __init__(self):
        self.move = None
        self.bot = BotManager()

    def retrieve_input(self):
        return self.move

    def start_thinking(self, game_state):
        if BotActionProvider.bool:
            self.move = Vector(0, 1)
        else:
            self.move = Vector(1, 0)

        BotActionProvider.bool = not BotActionProvider.bool

    def inform_about_lose(self):#gogogo tą funckje wywołać z clocka czy czego kolwiek
        #w nowej grze zcalluj normalnie start_thinking ze swiezym game state jak gdyby nigdy nic
        #mozliwe ze bedze trzeba przekazac dane o grze (czas, score) ale to potem
        self.bot.game_lost()
