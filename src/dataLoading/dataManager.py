import pandas as pd


class DataManager:
    dataList = []

    def __init__(self, dataSource):
        self.dataSource = dataSource
        self.loadData()

    def loadData(self):
        df = pd.read_csv(self.dataSource)
        self.dataList = df.values.tolist()
