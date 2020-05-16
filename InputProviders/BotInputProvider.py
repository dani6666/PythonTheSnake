import asyncio
import time

from Model.Vector import Vector


class BotInputProvider:

    def retrieve_input(self):
        return self.move

    def start_thinking(self, game_state):
        time.sleep(10)
        self.move = Vector(0, 1)
