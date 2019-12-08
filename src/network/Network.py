class Network:
    inputLayer = []
    hiddenLayer = []
    outputLayer = []
    weightsVector = []

    def setWeightsVector(self):
        for neuron in self.inputLayer:
            self.weightsVector.extend(neuron.weights)
        for neuron in self.hiddenLayer:
            self.weightsVector.extend(neuron.weights)
        for neuron in self.outputLayer:
            self.weightsVector.extend(neuron.weights)

    def displayInputLayer(self):
        for neuron in self.inputLayer:
            neuron.displayNeuronState()

    def displayHiddenLayer(self):
        for neuron in self.hiddenLayer:
            neuron.displayNeuronState()

    def displayOutputLayer(self):
        for neuron in self.outputLayer:
            neuron.displayNeuronState()

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
