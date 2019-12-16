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
        for item in networkVector:
            length = len(item)
            newItem = item[0: length - 3]
            networkVector[networkVector.index(item)] = newItem
        network.weightsVector = networkVector
        network.updateNetwork()
        return network
