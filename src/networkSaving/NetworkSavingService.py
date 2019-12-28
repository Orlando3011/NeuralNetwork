class NetworkSavingService:

    @staticmethod
    def saveNetworkToFile(network, fileName):
        with open(fileName, 'w') as f:
            for item in network.weightsVector:
                f.write("%s\n" % item)

    @staticmethod
    def makeNetworkFromFile(network, fileName):
        with open(fileName) as f:
            networkVector = f.readlines()
        newVector = []
        for item in networkVector:
            newItem = float(item[0: len(item) - 3])
            newVector.append(newItem)
        network.weightsVector = newVector
        network.updateNetwork()
        return network
