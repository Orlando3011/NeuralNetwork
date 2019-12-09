from src.dataLoading.dataManager import DataManager
from src.learning.evolutionManager import EvolutionManager

dataManager = DataManager("learningData.txt")

evolutionManager = EvolutionManager(100, 1000, 0.01)
evolutionManager.proceedAlgorithm(dataManager.dataList)
