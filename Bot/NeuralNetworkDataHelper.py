import numpy

from Bot.NeuralNetworkData import NeuralNetworkData


class NeuralNetworkDataHelper:

    def generate_data(self):
        return NeuralNetworkData(numpy.random.rand(12, 16), numpy.random.rand(12, 12), numpy.random.rand(4, 16))

    def crossover_data(self, first_data, second_data):#dostaniesz w porpertach obiektu te matrixy numpy'owe
        #oba argi typu NeuralNetworkData
        #pamietaj ze beda trasponowane od tych które generujemy
        #najlepiej zwrócić liste count = 2 [NeuralNetworkData, NeuralNetworkData]
        #nazwy tutaj beda pewnie do zmiany ale nie zmieniaj bo konflikty
        #gogogo

    def mutate_data(self, data_to_mutate):#dostaniesz w porpertach obiektu te matrixy numpy'owe
        #arg typu NeuralNetworkData
        #pamietaj ze beda trasponowane od tych które generujemy
        #najlepiej zwrócić po prostu NeuralNetworkData
        #nazwy tutaj beda pewnie do zmiany ale nie zmieniaj bo konflikty
        #gogogo
