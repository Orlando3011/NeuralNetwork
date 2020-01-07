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
                instance = self.mutate(instance)
                tmpPopulation.append(instance)
        self.population = tmpPopulation

    def breed(self):
        tmpPopulation = self.population
        randomList = random.sample(range(2, (len(tmpPopulation) - 1)), 6)
        candidates = []
        for element in randomList:
            candidates.append(tmpPopulation[element])
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
        neuronCounter = 0
        weightCounter = 0
        while neuronCounter < len(firstCandidate.inputLayer):
            while weightCounter < len(firstCandidate.inputLayer[neuronCounter].weights):
                rd = random.random()
                if rd > 0.5:
                    firstWeight = firstCandidate.inputLayer[neuronCounter].weights[weightCounter]
                    secondWeight = secondCandidate.inputLayer[neuronCounter].weights[weightCounter]
                    firstCandidate.inputLayer[neuronCounter].weights[weightCounter] = secondWeight
                    secondCandidate.inputLayer[neuronCounter].weights[weightCounter] = firstWeight
                weightCounter = weightCounter + 1
            weightCounter = 0
            neuronCounter = neuronCounter + 1
        neuronCounter = 0
        while neuronCounter < len(firstCandidate.hiddenLayer):
            while weightCounter < len(firstCandidate.hiddenLayer[neuronCounter].weights):
                rd = random.random()
                if rd > 0.5:
                    firstWeight = firstCandidate.hiddenLayer[neuronCounter].weights[weightCounter]
                    secondWeight = secondCandidate.hiddenLayer[neuronCounter].weights[weightCounter]
                    firstCandidate.hiddenLayer[neuronCounter].weights[weightCounter] = secondWeight
                    secondCandidate.hiddenLayer[neuronCounter].weights[weightCounter] = firstWeight
                weightCounter = weightCounter + 1
            weightCounter = 0
            neuronCounter = neuronCounter + 1
        neuronCounter = 0
        while neuronCounter < len(firstCandidate.outputLayer):
            while weightCounter < len(firstCandidate.outputLayer[neuronCounter].weights):
                rd = random.random()
                if rd > 0.5:
                    firstWeight = firstCandidate.outputLayer[neuronCounter].weights[weightCounter]
                    secondWeight = secondCandidate.outputLayer[neuronCounter].weights[weightCounter]
                    firstCandidate.outputLayer[neuronCounter].weights[weightCounter] = secondWeight
                    secondCandidate.outputLayer[neuronCounter].weights[weightCounter] = firstWeight
                weightCounter = weightCounter + 1
            weightCounter = 0
            neuronCounter = neuronCounter + 1
        offspringList = [firstCandidate, secondCandidate]
        return offspringList

    def mutate(self, network):
        rd = random.random()
        if rd <= self.mutationChance:
            rd = random.random()
            if rd >= 94:
                weightId = random.randint(0, len(network.outputLayer[0].weights) - 1)
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





