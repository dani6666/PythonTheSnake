import random

from Bot.BotFilesManager import BotFilesManager
from Bot.NeuralNetwork import NeuralNetwork
from Bot.NeuralNetworkDataHelper import NeuralNetworkDataHelper


class BotTrainer:
    population_count = 2000
    top_elements_for_breed = 400
    total_elements_for_breed = 220
    random_elements_for_breed = 20
    mutations_count = 200

    def __init__(self):
        self.helper = NeuralNetworkDataHelper()
        self.current_index = 0
        self.population = BotFilesManager.check_for_saved_bot()
        if not self.population:
            self.population = []
            for i in range(BotTrainer.population_count):
                self.population.append(self.helper.generate_data())

        self.current_neural_network = NeuralNetwork(self.population[0])

    def perform_move(self, input_var):
        return self.current_neural_network.get_output(input_var)

    def game_lost(self, game_result):

        self.population[self.current_index].game_result = game_result
        self.current_index += 1
        if self.current_index >= len(self.population):
            self.breed_population()
            self.current_index = 0
        else:
            self.current_neural_network = NeuralNetwork(self.population[self.current_index])

    def breed_population(self):
        self.population = sorted(self.population, key=lambda p: p.game_result, reverse=True)

        print_result = self.population[0].game_result
        print("Score: " + str(print_result.score) + " Moves: " + str(print_result.moves) + " Alive: " +
              str(print_result.was_snake_idle))
        BotFilesManager.save_bot(self.population)

        new_population = []
        breeding_population = self.population[0:BotTrainer.top_elements_for_breed]
        random_selection = self.population[BotTrainer.top_elements_for_breed:-1]
        while len(breeding_population) != BotTrainer.total_elements_for_breed:
            element = random.choice(random_selection)
            while breeding_population.__contains__(element):
                element = random.choice(random_selection)
            breeding_population.append(element)

        for t in range(20):
            print(str(len(new_population)) + " - " + str(t))
            for i in range(BotTrainer.total_elements_for_breed):
                for j in range(BotTrainer.total_elements_for_breed):
                    if len(new_population) == BotTrainer.population_count:
                        break
                    if i != j and random.random() > 0.9:
                        new_element = NeuralNetworkDataHelper.crossover_data(breeding_population[i],
                                                                             breeding_population[j])

                        if not new_population.__contains__(new_element):
                            new_population.append(new_element)

        for i in range(BotTrainer.mutations_count):
            index = random.randint(0, BotTrainer.population_count)
            new_population[index] = NeuralNetworkDataHelper.mutate_data(new_population[index])

        self.population = new_population
