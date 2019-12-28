class Network:
    inputLayer = []
    hiddenLayer = []
    outputLayer = []
    weightsVector = []

    def setWeightsVector(self):
        self.weightsVector = []
        for neuron in self.inputLayer:
            self.weightsVector.extend(neuron.weights)
        for neuron in self.hiddenLayer:
            self.weightsVector.extend(neuron.weights)
        for neuron in self.outputLayer:
            self.weightsVector.extend(neuron.weights)

    def updateNetwork(self):
        inputLayerWeights = len(self.inputLayer)
        hiddenLayerWeights = (inputLayerWeights + (len(self.hiddenLayer) * len(self.inputLayer)))
        outputLayerWeights = hiddenLayerWeights + (len(self.hiddenLayer) * len(self.outputLayer))
        counter = 0
        neuronCounter = 0
        weightCounter = 0
        while counter < inputLayerWeights:
            self.inputLayer[counter].weights[0] = self.weightsVector[counter]
            counter = counter + 1
        while neuronCounter < len(self.hiddenLayer):
            while weightCounter < len(self.hiddenLayer[0].weights):
                self.hiddenLayer[neuronCounter].weights[weightCounter] = self.weightsVector[counter]
                weightCounter = weightCounter + 1
                counter = counter + 1
            neuronCounter = neuronCounter + 1
            weightCounter = 0
        weightCounter = 0
        while weightCounter < len(self.outputLayer[0].weights):
            self.outputLayer[0].weights[weightCounter] = self.weightsVector[counter]
            counter = counter + 1
            weightCounter = weightCounter + 1

    def displayInputLayer(self):
        for neuron in self.inputLayer:
            neuron.displayNeuronState()

    def displayHiddenLayer(self):
        for neuron in self.hiddenLayer:
            neuron.displayNeuronState()

    def displayOutputLayer(self):
        for neuron in self.outputLayer:
            neuron.displayNeuronState()

    def resetError(self):
        for neuron in self.outputLayer:
            neuron.accumulatedError = 0

    def displayNetworkState(self):
        print("\nI am neural network, that works on echocardiogram dataset.\n-----------------------\n" +
              "My input neuron layer looks like: \n")
        self.displayInputLayer()
        print("\n-----------------------\n" +
              "My hidden neuron layer looks like: \n")
        self.displayHiddenLayer()
        print("\n-----------------------\n" +
              "My output neuron layer looks like: \n")
        self.displayOutputLayer()
