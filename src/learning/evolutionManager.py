from src.network.NetworkFactory import NetworkFactory


class EvolutionManager:
    population = []

    def __init__(self, populationSize, generationsNumber, mutationChance):
        self.populationSize = populationSize
        self.generationsNumber = generationsNumber
        self.mutationChance = mutationChance

    def initializePopulation(self):
        counter = 0
        networkFactory = NetworkFactory()
        while counter < self.populationSize:
            network = networkFactory.createNetwork()
            self.population.append(network)
            counter = counter + 1
