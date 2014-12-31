from uphexfunctions import *
#from __future__ import print_function
import numpy as np
from statsmodels.tsa.arima_process import arma_generate_sample
from statsmodels.tsa.arima_model import ARIMA

		
def main():
	timeseries={}
	timeseries['value']=readTextFile(15)
	timeseries['point']=range(1,(len(timeseries['value'])+1))
	print(len(timeseries['value']))
        print(len(timeseries['point']))

	#timeseries['value']=[0.0,10.0,5.0,100.0,50.0,40.0,23.0,20.0,23.0,22.0]

	#elements=forecast(timeseries,10)
	#print(elements)
	# prediction=timeseries
	prediction={}
	prediction['value']=readTextFile(15)
	prediction['actual_value']=prediction['value']
	prediction['point']=range(1,(len(prediction['actual_value'])+1))
	prediction['predictions']=[0]*(len(prediction['actual_value'])+1) 
	prediction['expected_value']=[0]*(len(prediction['actual_value'])+1)
	elements=history(prediction,10)
	print(elements)
	# print timeseries 
	# print type(timeseries)
	# print timeseries.keys()
	# print prediction 
	# print type(prediction)
	# print prediction.keys()


if __name__ == '__main__':
	main()
