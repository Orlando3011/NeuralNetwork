class Neuron:
    name = ""
    inputs = []
    weights = []
    output = 0
    accumulatedError = 0

    def __init__(self, name):
        self.name = str(name)

    def setOutput(self):
        tempSum = 0
        for inputData in self.inputs:
            tempSum = tempSum + self.weights[self.inputs.index(inputData)] * inputData
        tempSum = self.characteristic(tempSum)
        self.output = tempSum

    @staticmethod
    def characteristic(x):
        from math import e
        return 1/(1 + e**(-1 * x))

    def displayNeuronState(self):
        print("---------------------------")
        print("I am neuron named: " + self.name)
        print("My inputs are: ")
        print(self.inputs)
        print("My weights are: ")
        print(self.weights)
        print("My output is: ")
        print(self.output)
        if self.name == "output":
            print("My accumulated error is: ")
            print(self.accumulatedError)
