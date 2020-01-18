import sys

from src.dataLoading.dataManager import DataManager
from src.learning.evolutionManager import EvolutionManager
from src.network.NetworkFactory import NetworkFactory
from src.network.NetworkService import NetworkService
from src.networkSaving.NetworkSavingService import NetworkSavingService
from src.plotting.plottingService import PlottingService


class Menu:
    def __init__(self):
        networkFactory = NetworkFactory()
        self.network = networkFactory.createNetwork()

    def mainMenu(self):
        result = '0'
        while result != '3':
            print("This program creates and teaches neural networks, which are working on ECG data."
                  "\n1. Use evolutionary algorithm to generate network"
                  "\n2. Load saved network from .txt file"
                  "\n3. Manually test network (if no network is loaded, system will use random one)"
                  "\n4. Auto test loaded network with test dataset"
                  "\n5. Exit program")
            result = input()
            if result == '1':
                self.evolutionaryMenu()
                result = '0'
            if result == '2':
                self.loadMenu()
                result = '0'
            if result == '3':
                self.testMenu()
                result = '0'
            if result == "4":
                self.autoTestMenu()
                result = "0"
            if result == '5':
                sys.exit()
            if result == '0':
                pass
            else:
                print("There is no option like that.")

    def evolutionaryMenu(self):
        print("This algorithm will generate a population of X networks, and proceed it through Y generations."
              " Each instance will have Z chance to mutate."
              "\nInput population size: ")
        populationSize = float(input())
        print("Input number of generations: ")
        generations = float(input())
        print("Input mutation chance: ")
        mutation = float(input())
        print("Input file, in which the best network will be saved: ")
        fileName = input()
        self.doAlgorithm(populationSize, generations, mutation, fileName)

    @staticmethod
    def doAlgorithm(populationSize, generations, mutation, fileName):
        dataManager = DataManager("learningData.csv")
        evolutionManager = EvolutionManager(populationSize, generations, mutation)
        outputData = evolutionManager.proceedAlgorithm(dataManager.dataList, fileName)
        plottingService = PlottingService()
        df = plottingService.loadDataToDataFrame(outputData)

        plottingService.makePlot(df, "Mean of errors", "mean.png")
        plottingService.makePlot(df, "Minimal error", "minimal.png")

    def loadMenu(self):
        print("Load network from a file:")
        fileName = input()
        networkSavingService = NetworkSavingService()
        networkSavingService.makeNetworkFromFile(self.network, fileName)
        print("Successfully loaded network: ")
        self.network.displayNetworkState()

    def testMenu(self):
        data = '0'
        while data != '1':
            print("Input list of arguments - you can copypaste one row from larningData.txt:"
                  "\nType 1 to go back"
                  "\nMind that the last element of the list is the result network will try to reach - do not input it!")
            data = input()
            if data == '1':
                break
            data = data.replace('"', '')
            dataList = list(data.split(','))
            for data in dataList:
                dataList[dataList.index(data)] = float(data)
            self.testNetwork(dataList)

    def testNetwork(self, dataList):
        networkService = NetworkService()
        networkService.solveTask(self.network, dataList)
        output = self.network.outputLayer[0].output
        print("Network proceeded data! Output is: ")
        print(output)

    def autoTestMenu(self):
        dataManager = DataManager("testData.csv")
        networkService = NetworkService()
        correctAnswers = networkService.testNetwork(self.network, dataManager.dataList)
        print("Test finished! Out of 50 records, network classified correctly:")
        print(correctAnswers)
        print("of them.")



