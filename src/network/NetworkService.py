class NetworkService:

    def __init__(self, network):
        self.network = network

    def loadData(self, data):
        for inputNeuron in self.network.inputLayer:
            inputNeuron.inputs[0] = data[self.network.inputLayer.index(inputNeuron)]
            inputNeuron.setOutput()

    def proceedData(self):
        for hiddenNeuron in self.network.hiddenLayer:
            for inputNeuron in self.network.inputLayer:
                hiddenNeuron.inputs[self.network.inputLayer.index(inputNeuron)] = \
                    self.network.inputLayer[self.network.inputLayer.index(inputNeuron)].output
            hiddenNeuron.setOutput()

    def finishTask(self):
        for outputNeuron in self.network.outputLayer:
            for hiddenNeuron in self.network.hiddenLayer:
                outputNeuron.inputs[self.network.hiddenLayer.index(hiddenNeuron)] = \
                    self.network.hiddenLayer[self.network.hiddenLayer.index(hiddenNeuron)].output
            outputNeuron.setOutput()

    def solveTask(self, data):
        self.loadData(data)
        self.proceedData()
        self.finishTask()
