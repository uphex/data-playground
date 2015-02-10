from autoregressive_integrated_moving_average import *

def main():
    timeseries={}

    timeseries['value']=readTextFile(15)
    timeseries['point']=range(1,(len(timeseries['value'])+1))

    print(len(timeseries['value']))
    print(len(timeseries['point']))

    #timeseries['value']=[0.0,10.0,5.0,100.0,50.0,40.0,23.0,20.0,23.0,22.0]

    elements=forecast(timeseries,10)

    print("forecast elements")
    print(elements)

    timeseries = {}
    timeseries['value'] = readTextFile(15)[0:20]
    timeseries['point'] = range(1,(len(timeseries['value'])+1))
    elements = history(timeseries,10)

    print("history elements")
    print(elements)

    # print timeseries
    # print type(timeseries)
    # print timeseries.keys()
    # print prediction
    # print type(prediction)
    # print prediction.keys()
