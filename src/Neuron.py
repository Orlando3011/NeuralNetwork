class Neuron:
    name = "default"
    inputs = []
    weights = []
    output = 0

    def __init__(self, name):
        self.name = name

    def setWeight(self, newWeights):
        self.weights = newWeights

    def setInput(self, newInputs):
        self.inputs = newInputs

    def setOutput(self):
        tempSum = 0
        for x in self.inputs:
            tempSum = tempSum + x * self.weights[self.inputs.index(x)]
        tempSum = self.characteristic(tempSum)
        self.output = tempSum

    @staticmethod
    def characteristic(x):
        from math import e
        return 1/(1 + e**(-1 * x))
