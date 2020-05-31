import math
import os
import random

import numpy

from Bot.BotTrainer import BotTrainer
from Model.GameResult import GameResult
from Model.SpecialAction import SpecialAction
from Model.Vector import Vector
from Bot.Walk import Walk


class BotManager:
    bot_resources_file_name = "saved-bot.json"
    snake_idle_moves_limit = 100

    def __init__(self):
        self.moves_without_eating = 0
        self.total_moves = 0
        self.last_apple_position = None
        self.bot_trainer = BotTrainer()

    def perform_move(self, game_state):
        self.total_moves += 1
        if self.last_apple_position == game_state.apple_position:
            self.moves_without_eating += 1
        else:
            self.last_apple_position = game_state.apple_position
            self.moves_without_eating = 0

        if self.moves_without_eating > BotManager.snake_idle_moves_limit:
            self.bot_trainer.game_lost(GameResult(game_state.score, self.total_moves, True))
            self.total_moves = 0
            self.moves_without_eating = 0
            return SpecialAction.reset_game

        input_matrix = self.from_game_state_to_matrix(game_state)
        output_matrix = self.bot_trainer.perform_move(input_matrix)

        move = self.from_matrix_to_move(output_matrix)
        if move == 0:
            return [Vector(1, 0)]
        elif move == 1:
            return [Vector(-1, 0)]
        elif move == 2:
            return [Vector(0, 1)]
        elif move == 3:
            return [Vector(0, -1)]

    def game_lost(self, score):
        self.bot_trainer.game_lost(GameResult(score, self.total_moves, False))

    @staticmethod
    def from_game_state_to_matrix(game_state):
        result = \
            Walk(game_state.snake.position, [game_state.apple_position], game_state.grid_size).walk() + \
            Walk(game_state.snake.position, game_state.snake.get_slots_occupied_by_body(), game_state.grid_size).walk()
        result = numpy.array([result])

        return result

    @staticmethod
    def from_matrix_to_move(matrix):
        max_val = -math.inf
        index = None
        for i in range(4):
            if max_val < matrix[0][i]:
                index = i
                max_val = matrix[0][i]

        return index
