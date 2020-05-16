import asyncio
import time
from random import random

from Model.Vector import Vector


class BotInputProvider:
    bool = True

    def retrieve_input(self):
        return self.move

    def start_thinking(self, game_state):
        if BotInputProvider.bool:
            self.move = Vector(0, 1)
        else:
            self.move = Vector(1, 0)

        BotInputProvider.bool = not BotInputProvider.bool
