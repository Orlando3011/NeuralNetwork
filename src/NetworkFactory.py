from src.NeuronFactory import NeuronFactory
from src.Network import Network


class NetworkFactory:

    def createNetwork(self):
        network = Network()
        self.fillInputLayer(network)
        self.fillHiddenLayer(network)
        self.fillOutputLayer(network)
        return network

    @staticmethod
    def fillInputLayer(network):
        factory = NeuronFactory()
        network.inputLayer.append(factory.createInputNeuron("survival"))
        network.inputLayer.append(factory.createInputNeuron("still_alive"))
        network.inputLayer.append(factory.createInputNeuron("age_at_heart_attack"))
        network.inputLayer.append(factory.createInputNeuron("pericardial_effusion"))
        network.inputLayer.append(factory.createInputNeuron("fractional_shortening"))
        network.inputLayer.append(factory.createInputNeuron("epss"))
        network.inputLayer.append(factory.createInputNeuron("lvdd"))
        network.inputLayer.append(factory.createInputNeuron("wall_motion_score"))
        network.inputLayer.append(factory.createInputNeuron("wall_motion_index"))

    @staticmethod
    def fillHiddenLayer(network):
        factory = NeuronFactory()
        network.hiddenLayer.append(factory.createOutputNeuron("hidden1"))
        network.hiddenLayer.append(factory.createHiddenNeuron("hidden2"))
        network.hiddenLayer.append(factory.createHiddenNeuron("hidden3"))
        network.hiddenLayer.append(factory.createHiddenNeuron("hidden4"))
        network.hiddenLayer.append(factory.createHiddenNeuron("hidden5"))
        network.hiddenLayer.append(factory.createHiddenNeuron("hidden6"))
        network.hiddenLayer.append(factory.createHiddenNeuron("hidden7"))
        network.hiddenLayer.append(factory.createHiddenNeuron("hidden8"))
        network.hiddenLayer.append(factory.createHiddenNeuron("hidden9"))

    @staticmethod
    def fillOutputLayer(network):
        factory = NeuronFactory()
        network.outputLayer.append(factory.createOutputNeuron("alive"))
        network.outputLayer.append(factory.createOutputNeuron("notAlive"))

