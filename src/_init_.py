from src.dataLoading.dataManager import DataManager
from src.network.NetworkFactory import NetworkFactory
from src.network.NetworkService import NetworkService

networkFactory = NetworkFactory()
networkService = NetworkService(networkFactory.createNetwork())

networkService.network.displayNetworkState()

dataManager = DataManager()

networkService.learn(dataManager.dataList)

print("\n\nLet's test network with learning data:\n\n")

networkService.network.displayNetworkState()
