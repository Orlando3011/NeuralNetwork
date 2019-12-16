from src.neuron.Neuron import Neuron
import random as rd


class NeuronFactory:

    @staticmethod
    def createInputNeuron(name):
        neuron = Neuron(name)
        neuron.inputs = [0]
        neuron.weights = [rd.uniform(-5, 5)]
        return neuron

    @staticmethod
    def createHiddenNeuron(name):
        neuron = Neuron(name)
        neuron.inputs = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        neuron.weights = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for x in neuron.weights:
            neuron.weights[neuron.weights.index(x)] = rd.uniform(-5, 5)
        return neuron

    @staticmethod
    def createOutputNeuron(name):
        neuron = Neuron(name)
        neuron.inputs = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        neuron.weights = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for x in neuron.weights:
            neuron.weights[neuron.weights.index(x)] = rd.uniform(-5, 5)
        return neuron
