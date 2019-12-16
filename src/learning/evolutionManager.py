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
        meanOfErrors = []
        minimumError = []
        outputData = [meanOfErrors, minimumError]
        self.initializePopulation()
        networkService = NetworkService()

        counter = 0
        while counter < self.generationsNumber:
            for network in self.population:
                networkService.learn(network, dataList)
            minimumError.append(self.getBestInstanceError())
            meanOfErrors.append(self.meanOfPopulation())
            self.crossover()
            counter = counter + 1
            msg = "Generation no. " + str(counter)
            print(msg)
        print("\n--------------------------------\n")
        return outputData

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
        bestInstance = self.getBestInstance()
        crossoverGeneration.append(bestInstance)
        self.population.remove(bestInstance)
        secondBestInstance = self.getBestInstance()
        crossoverGeneration.append(secondBestInstance)
        self.population.append(bestInstance)
        while counter < (self.populationSize - 2) / 2:
            offspring = self.breed()
            for instance in offspring:
                instance = self.mutate(instance)
                crossoverGeneration.append(instance)
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
        return offspring

    @staticmethod
    def makeOffspring(firstCandidate, secondCandidate):
        offspring = firstCandidate
        secondOffspring = secondCandidate
        neuronCounter = 0
        weightCounter = 0
        while neuronCounter < len(offspring.inputLayer):
            while weightCounter < len(offspring.inputLayer[neuronCounter].weights):
                rd = random.random()
                if rd > 0.5:
                    firstWeight = offspring.inputLayer[neuronCounter].weights[weightCounter]
                    secondWeight = secondOffspring.inputLayer[neuronCounter].weights[weightCounter]
                    offspring.inputLayer[neuronCounter].weights[weightCounter] = secondWeight
                    secondOffspring.inputLayer[neuronCounter].weights[weightCounter] = firstWeight
                weightCounter = weightCounter + 1
            weightCounter = 0
            neuronCounter = neuronCounter + 1
        neuronCounter = 0
        while neuronCounter < len(offspring.hiddenLayer):
            while weightCounter < len(offspring.hiddenLayer[neuronCounter].weights):
                rd = random.random()
                if rd > 0.5:
                    firstWeight = offspring.hiddenLayer[neuronCounter].weights[weightCounter]
                    secondWeight = secondOffspring.hiddenLayer[neuronCounter].weights[weightCounter]
                    offspring.hiddenLayer[neuronCounter].weights[weightCounter] = secondWeight
                    secondOffspring.hiddenLayer[neuronCounter].weights[weightCounter] = firstWeight
                weightCounter = weightCounter + 1
            weightCounter = 0
            neuronCounter = neuronCounter + 1
        neuronCounter = 0
        while neuronCounter < len(offspring.outputLayer):
            while weightCounter < len(offspring.outputLayer[neuronCounter].weights):
                rd = random.random()
                if rd > 0.5:
                    firstWeight = offspring.outputLayer[neuronCounter].weights[weightCounter]
                    secondWeight = secondOffspring.outputLayer[neuronCounter].weights[weightCounter]
                    offspring.outputLayer[neuronCounter].weights[weightCounter] = secondWeight
                    secondOffspring.outputLayer[neuronCounter].weights[weightCounter] = firstWeight
                weightCounter = weightCounter + 1
            weightCounter = 0
            neuronCounter = neuronCounter + 1
        offspringList = [offspring, secondOffspring]
        return offspringList

    def mutate(self, network):
        rd = random.random()
        if rd <= self.mutationChance:
            rd = random.random()
            if rd >= 94:
                weightId = random.randint(0, network.outputLayer[0].weights)
                network.outputLayer[0].weights[weightId] = random.uniform(-5, 5)
            if 46 < rd < 94:
                weightId = random.randint(0, (len(network.hiddenLayer[0].weights) - 1))
                neuronId = random.randint(0, (len(network.hiddenLayer) - 1))
                network.hiddenLayer[neuronId].weights[weightId] = random.uniform(-5, 5)
            else:
                neuronId = random.randint(0, (len(network.inputLayer) - 1))
                network.inputLayer[neuronId].weights[0] = random.uniform(-5, 5)
        return network

    def getBestInstance(self):
        bestInstance = self.population[0]
        for instance in self.population:
            if instance.outputLayer[0].accumulatedError < bestInstance.outputLayer[0].accumulatedError:
                bestInstance = instance
        return bestInstance

    def displayPopulationErrors(self):
        for instance in self.population:
            print(instance.outputLayer[0].accumulatedError)

    def getBestInstanceError(self):
        bestInstance = self.getBestInstance()
        return bestInstance.outputLayer[0].accumulatedError

    def resetInstancesErrors(self):
        for instance in self.population:
            instance.resetError()

    def meanOfPopulation(self):
        mean = 0
        for instance in self.population:
            mean = mean + instance.outputLayer[0].accumulatedError
        mean = mean / len(self.population)
        return mean
