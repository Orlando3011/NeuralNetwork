import random

from src.network.NetworkFactory import NetworkFactory
from src.network.NetworkService import NetworkService
from src.networkSaving.NetworkSavingService import NetworkSavingService


class EvolutionManager:
    population = []

    def __init__(self, populationSize, generationsNumber, mutationChance):
        self.populationSize = populationSize
        self.generationsNumber = generationsNumber
        self.mutationChance = mutationChance

    def proceedAlgorithm(self, dataList, fileName):
        meanOfErrors = []
        minimumError = []
        outputData = [meanOfErrors, minimumError]
        self.initializePopulation()
        networkService = NetworkService()
        networkSavingService = NetworkSavingService()

        counter = 0
        while counter < self.generationsNumber:
            for network in self.population:
                networkService.learn(network, dataList)

            bestInstances = self.getTwoBestInstances()
            for network in bestInstances:
                networkService.learn(network, dataList)

            msg = "Generation no. " + str(counter)
            print(msg)
            bestInstances = self.getTwoBestInstances()
            print("Best instances: ")
            print(bestInstances[0].outputLayer[0].accumulatedError)
            print(bestInstances[1].outputLayer[0].accumulatedError)
            minimumError.append(self.getBestInstanceError())
            meanOfErrors.append(self.meanOfPopulation())
            self.crossover()
            counter = counter + 1
            print("==============")
        networkSavingService.saveNetworkToFile(self.getBestInstance(), fileName)
        return outputData

    def initializePopulation(self):
        counter = 0
        networkFactory = NetworkFactory()
        while counter < self.populationSize:
            network = networkFactory.createNetwork()
            self.population.append(network)
            counter = counter + 1

    def crossover(self):
        tmpPopulation = self.getTwoBestInstances()
        while len(tmpPopulation) < self.populationSize:
            offspring = self.breed()
            for instance in offspring:
                rd = random.random()
                if rd < self.mutationChance:
                    instance = self.mutate(instance)
                tmpPopulation.append(instance)

        self.population = tmpPopulation

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
        tmpVector = secondCandidate.weightsVector
        counter = 0
        while counter < len(tmpVector):
            r = random.random()
            if r > 0.5:
                secondCandidate.weightsVector[counter] = firstCandidate.weightsVector[counter]
                firstCandidate.weightsVector[counter] = tmpVector[counter]
            counter = counter + 1
        firstCandidate.updateNetwork()
        secondCandidate.updateNetwork()
        offspringList = [firstCandidate, secondCandidate]
        return offspringList

    @staticmethod
    def mutate(network):
        randomWeight = random.randrange(0, (len(network.weightsVector) - 1))
        network.weightsVector[randomWeight] = random.uniform(-5, 5)
        network.updateNetwork()
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

    def getTwoBestInstances(self):
        tmpPopulation = self.population
        firstInstance = tmpPopulation[0]

        for instance in tmpPopulation:
            if instance.outputLayer[0].accumulatedError < firstInstance.outputLayer[0].accumulatedError:
                firstInstance = instance

        bestCouple = [firstInstance]
        tmpPopulation.remove(firstInstance)
        secondInstance = tmpPopulation[0]

        for instance in tmpPopulation:
            if instance.outputLayer[0].accumulatedError < secondInstance.outputLayer[0].accumulatedError:
                secondInstance = instance
        bestCouple.append(secondInstance)
        tmpPopulation.insert(0, firstInstance)
        return bestCouple





