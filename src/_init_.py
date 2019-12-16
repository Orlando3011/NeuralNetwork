from src.dataLoading.dataManager import DataManager
from src.learning.evolutionManager import EvolutionManager
from src.networkSaving.NetworkSavingService import NetworkSavingService
from src.plotting.plottingService import PlottingService

dataManager = DataManager("learningData.txt")

evolutionManager = EvolutionManager(100, 30, 0.2)
networkSavingService = NetworkSavingService()
outputData = evolutionManager.proceedAlgorithm(dataManager.dataList)

plottingService = PlottingService()
df = plottingService.loadDataToDataFrame(outputData)

plottingService.makePlot(df, "Mean of errors", "mean.png")
plottingService.makePlot(df, "Minimal error", "minimal.png")
