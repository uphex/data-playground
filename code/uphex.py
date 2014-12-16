from uphexfunctions import *

		
def main():
	timeseries={}
	timeseries['point']=[0,1,2,3,4,5,6,7,8,9]
	timeseries['value']=[0.0,10.0,5.0,100.0,50.0,40.0,23.0,20.0,23.0,22.0]

	elements=history(timeseries,2)
	print elements
	# prediction=timeseries
	prediction={}
	prediction['point']=[1000,1005,1010]
	prediction['predictions']=[0]*len(prediction['point']) 
	prediction['expected_value']=[0]*len(prediction['point']) 
	prediction['actual_value']=[None]*len(prediction['point']) 
	# print timeseries 
	# print type(timeseries)
	# print timeseries.keys()
	# print prediction 
	# print type(prediction)
	# print prediction.keys()


if __name__ == '__main__':
	main()
