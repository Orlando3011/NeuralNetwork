import random

from src.network.NetworkFactory import NetworkFactory
from src.network.NetworkService import NetworkService


class EvolutionManager:
    population = []

    def __init__(self, populationSize, generationsNumber, mutationChance):
        self.populationSize = populationSize
        self.generationsNumber = generationsNumber
        self.mutationChance = mutationChance

    def proceedAlgorithm(self, dataList):
        self.initializePopulation()
        networkService = NetworkService()
        counter = 0
        while counter < self.generationsNumber:
            for network in self.population:
                networkService.learn(network, dataList)
            self.printBestInstanceError()
            print("Mean of the population is:")
            print(self.meanOfPopulation())
            print("-----------------------")
            self.crossover()
            counter = counter + 1

    def initializePopulation(self):
        counter = 0
        networkFactory = NetworkFactory()
        while counter < self.populationSize:
            network = networkFactory.createNetwork()
            self.population.append(network)
            counter = counter + 1

    def crossover(self):
        counter = 0
        crossoverGeneration = []
        while counter < self.populationSize:
            crossoverGeneration.append(self.breed())
            counter = counter + 1
        self.population = crossoverGeneration

    def breed(self):
        candidates = random.choices(self.population, k=6)
        firstCandidate = candidates[0]
        for candidate in candidates:
            if candidate.outputLayer[0].accumulatedError < firstCandidate.outputLayer[0].accumulatedError:
                firstCandidate = candidate
        candidates.remove(firstCandidate)
        secondCandidate = candidates[0]
        for candidate in candidates:
            if candidate.outputLayer[0].accumulatedError < secondCandidate.outputLayer[0].accumulatedError:
                secondCandidate = candidate

        offspring = self.makeOffspring(firstCandidate, secondCandidate)
        offspring = self.mutate(offspring)
        offspring.setWeightsVector()
        return offspring

    @staticmethod
    def makeOffspring(firstCandidate, secondCandidate):
        offspring = firstCandidate
        for neuron in offspring.inputLayer:
            secondNeuron = secondCandidate.inputLayer[offspring.inputLayer.index(neuron)]
            for weight in neuron.weights:
                rd = random.random()
                if rd > 0.5:
                    substituteWeight = secondNeuron.weights[neuron.weights.index(weight)]
                    offspring.inputLayer[offspring.inputLayer.index(neuron)].weights[neuron.weights.index(weight)] \
                        = substituteWeight
        for neuron in offspring.hiddenLayer:
            secondNeuron = secondCandidate.hiddenLayer[offspring.hiddenLayer.index(neuron)]
            for weight in neuron.weights:
                rd = random.random()
                if rd > 0.5:
                    substituteWeight = secondNeuron.weights[neuron.weights.index(weight)]
                    offspring.hiddenLayer[offspring.hiddenLayer.index(neuron)].weights[neuron.weights.index(weight)] \
                        = substituteWeight
        for neuron in offspring.outputLayer:
            secondNeuron = secondCandidate.outputLayer[offspring.outputLayer.index(neuron)]
            for weight in neuron.weights:
                rd = random.random()
                if rd > 0.5:
                    substituteWeight = secondNeuron.weights[neuron.weights.index(weight)]
                    offspring.outputLayer[offspring.outputLayer.index(neuron)].weights[neuron.weights.index(weight)] \
                        = substituteWeight
        return offspring

    def mutate(self, offspring):
        for neuron in offspring.inputLayer:
            for weight in neuron.weights:
                rd = random.random()
                if rd < self.mutationChance:
                    offspring.inputLayer[offspring.inputLayer.index(neuron)].weights[neuron.weights.index(weight)]\
                        = random.randrange(-5, 5)
        for neuron in offspring.hiddenLayer:
            for weight in neuron.weights:
                rd = random.random()
                if rd < self.mutationChance:
                    offspring.hiddenLayer[offspring.hiddenLayer.index(neuron)].weights[neuron.weights.index(weight)]\
                        = random.randrange(-5, 5)
        for neuron in offspring.outputLayer:
            for weight in neuron.weights:
                rd = random.random()
                if rd < self.mutationChance:
                    offspring.outputLayer[offspring.outputLayer.index(neuron)].weights[neuron.weights.index(weight)]\
                        = random.randrange(-5, 5)
        return offspring

    def getBestInstance(self):
        bestInstance = self.population[0]
        for instance in self.population:
            if instance.outputLayer[0].accumulatedError < bestInstance.outputLayer[0].accumulatedError:
                bestInstance = instance
        return bestInstance

    def displayPopulationErrors(self):
        for instance in self.population:
            print(instance.outputLayer[0].accumulatedError)

    def printBestInstanceError(self):
        bestInstance = self.getBestInstance()
        print("The best instance of this generation has error of value: ")
        print(bestInstance.outputLayer[0].accumulatedError)

    def resetInstancesErrors(self):
        for instance in self.population:
            instance.resetError()

    def meanOfPopulation(self):
        mean = 0
        for instance in self.population:
            mean = mean + instance.outputLayer[0].accumulatedError
        mean = mean / len(self.population)
        return mean
