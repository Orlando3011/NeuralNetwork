import pandas as pd


class PlottingService:

    @staticmethod
    def loadDataToDataFrame(dataList):
        df = pd.DataFrame(list(zip(dataList[0], dataList[1])), columns=["Mean of errors", "Minimal error"])
        print(df)
        df.to_html("data.html")
        return df

    @staticmethod
    def makePlot(dataframe, xAxis, fileName):
        dataframe.plot().get_figure().savefig(fileName)
