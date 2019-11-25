import pandas as py
from src.NetworkFactory import NetworkFactory

networkFactory = NetworkFactory()
network = networkFactory.createNetwork()

network.displayNetworkState()
