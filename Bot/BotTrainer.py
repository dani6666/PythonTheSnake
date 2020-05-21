from Bot.Move import Move
from Bot.NeuralNetwork import NeuralNetwork
from Bot.NeuralNetworkDataHelper import NeuralNetworkDataHelper


class BotTrainer:
    population_count = 2000

    def __init__(self, starting_population=None):
        self.helper = NeuralNetworkDataHelper()
        self.current_index = 0
        self.current_neural_network = NeuralNetwork(starting_population[0])
        if not starting_population:
            self.population = []
            for i in range(BotTrainer.population_count):
                self.population.append(self.helper.generate_data())
        else:
            self.population = starting_population


    def perform_move(self, game_state):
        return Move.down

    def game_lost(self):
        self.current_index += 1
        if self.current_index >= len(self.population):
            self.breed_population()
        else:
            self.current_neural_network = NeuralNetwork(self.population[self.current_index])

    def breed_population(self):
