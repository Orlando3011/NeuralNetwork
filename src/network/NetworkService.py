class NetworkService:

    @staticmethod
    def loadData(network, data):
        for inputNeuron in network.inputLayer:
            inputNeuron.inputs[0] = data[network.inputLayer.index(inputNeuron) + 1]
            # +1 to avoid adding id column to the network
            inputNeuron.setOutput()

    @staticmethod
    def proceedData(network):
        for hiddenNeuron in network.hiddenLayer:
            for inputNeuron in network.inputLayer:
                hiddenNeuron.inputs[network.inputLayer.index(inputNeuron)] = \
                    network.inputLayer[network.inputLayer.index(inputNeuron)].output
            hiddenNeuron.setOutput()

    @staticmethod
    def finishTask(network):
        for outputNeuron in network.outputLayer:
            for hiddenNeuron in network.hiddenLayer:
                outputNeuron.inputs[network.hiddenLayer.index(hiddenNeuron)] = \
                    network.hiddenLayer[network.hiddenLayer.index(hiddenNeuron)].output
            outputNeuron.setOutput()

    @staticmethod
    def checkOutput(network, correctAnswer):
        for outputNeuron in network.outputLayer:
            if correctAnswer == 1:
                outputNeuron.accumulatedError = outputNeuron.accumulatedError + (correctAnswer - outputNeuron.output)
            else:
                outputNeuron.accumulatedError = outputNeuron.accumulatedError + outputNeuron.output

    def solveTask(self, network, data):
        self.loadData(network, data)
        self.proceedData(network)
        self.finishTask(network)

    def learn(self, network, dataList):
        network.resetError()
        for data in dataList:
            self.solveTask(network, data)
            self.checkOutput(network, data[10])
