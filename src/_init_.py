from src.network.NetworkFactory import NetworkFactory
from src.network.NetworkService import NetworkService

networkFactory = NetworkFactory()
networkService = NetworkService(networkFactory.createNetwork())

networkService.network.displayNetworkState()

print("\n\nLet's test network with this data row: [4, 0, 71, 0, 0.26, 9, 4.6, 14, 1]\n\n")

networkService.solveTask([4, 0, 71, 0, 0.26, 9, 4.6, 14, 1])

networkService.network.displayNetworkState()
