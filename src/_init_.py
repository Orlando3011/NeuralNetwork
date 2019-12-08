from src.learning.evolutionManager import EvolutionManager


evolutionManager = EvolutionManager(4, 100, 0.05)
evolutionManager.initializePopulation()

for network in evolutionManager.population:
    network.displayNetworkState()
