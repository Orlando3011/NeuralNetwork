from src.Neuron import Neuron
import random as rd


class NeuronFactory:

    @staticmethod
    def createInputNeuron(name):
        neuron = Neuron(name)
        neuron.inputs = [0]
        neuron.weights = [rd.random.random()]
        return neuron

    @staticmethod
    def createHiddenNeuron(name):
        neuron = Neuron(name)
        neuron.inputs = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for x in neuron.weights:
            x = rd.random.random()
        return neuron

    @staticmethod
    def createOutputNeuron(name):
        neuron = Neuron(name)
        neuron.inputs = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for x in neuron.weights:
            x = rd.random.random()
        return neuron
