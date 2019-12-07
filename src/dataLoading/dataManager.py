import pandas as pd


class DataManager:
    dataList = []

    def __init__(self):
        self.loadData()

    def loadData(self):
        df = pd.read_csv("learningData.txt")
        self.dataList = df.values.tolist()
