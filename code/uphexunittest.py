import unittest
from uphexfunctions import *


class TestSuite(unittest.TestCase):
	def test_number_forecast_elements(self):
		n=5
		ts={}
		ts['point']=[0,1,2,3,4,5,6,7,8]
		ts['value']=[0,1,2,3,4,5,6,7,8]
		elements=forecast(ts,n)
		assert len(elements['expected_value'])==n
	def test_point_forecast_elements(self):
		n=2
		ts={}
		ts['point']=[0,1,2,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
		ts['value']=[0,1,2,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
		elements=forecast(ts,n)
		assert elements['point']==[21,22]
	def test_minrequired_runforecast_elements(self):
		n=2
		ts={}
		ts['point']=[1,2,3]
		ts['value']=[1.0,2.0,3.0]
		elements=runforecast(ts,n,minrequired=5)
		assert elements['value']==ts['value']
	def test_number_history_elements(self):
		n=5
                ts={}
                ts['value']=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
                ts['actual_value']=ts['value']
                ts['point']=range(1,(len(ts['actual_value'])+1))
                ts['predictions']=[0]*(len(ts['actual_value'])+1)
                ts['expected_value']=[0]*(len(ts['actual_value'])+1)
		elements=history(ts,n)
		assert len(elements['expected_value'])==(len(ts['value'])+n)
	def test_keys_history(self):
		n=5
                ts={}
                ts['value']=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
                ts['actual_value']=ts['value']
                ts['point']=range(1,(len(ts['actual_value'])+1))
                ts['predictions']=[0]*(len(ts['actual_value'])+1)
                ts['expected_value']=[0]*(len(ts['actual_value'])+1)
		elements=history(ts,n)
		for key in elements.iterkeys():
			assert key in ['actual_value','value','point','predictions','expected_value']
	def test_point_history_elements(self):
		n=5
		ts={}
		ts['value']=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
	        ts['actual_value']=ts['value']
        	ts['point']=range(1,(len(ts['actual_value'])+1))
       		ts['predictions']=[0]*(len(ts['actual_value'])+1)
        	ts['expected_value']=[0]*(len(ts['actual_value'])+1)
		elements=history(ts,n)
		assert elements['point']==[None, None, None, None, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
	def test_actual_value_history_elements(self):
		n=5
                ts={}
                ts['value']=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
                ts['actual_value']=ts['value']
                ts['point']=range(1,(len(ts['actual_value'])+1))
                ts['predictions']=[0]*(len(ts['actual_value'])+1)
                ts['expected_value']=[0]*(len(ts['actual_value'])+1)
		elements=history(ts,n)
		assert elements['actual_value']==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14,15,16,17, None, None, None, None, None]
	def test_keys_appendelements(self):
		a={}
		b={}
		b['key']=[1,2,3]
		f=appendelements(a,b)
		for key in f.iterkeys():
			assert key in ['key']
	def test_value_appendelements(self):
		a={}
		b={}
		b['key']=[1,2,3]
		f=appendelements(a,b)
		assert f['key']==[3]
	def test_autoarima_bestkey(self):
		ts={}
		ts['value']=[93.0, 51.0, 45.0, 101.0, 216.0, 169.0, 127.0, 105.0, 49.0, 59.0, 108.0, 118.0, 135.0, 127.0, 73.0, 40.0, 51.0, 75.0, 98.0, 81.0, 78.0, 62.0, 39.0, 41.0, 70.0, 60.0, 76.0, 109.0, 109.0, 38.0, 40.0, 81.0, 89.0, 107.0, 79.0, 64.0, 37.0, 36.0, 55.0, 70.0, 65.0, 81.0, 63.0, 33.0, 40.0, 51.0, 73.0, 50.0, 69.0, 65.0, 43.0, 35.0, 59.0, 84.0, 54.0, 184.0, 80.0, 24.0, 24.0, 64.0, 69.0, 60.0, 47.0, 70.0, 32.0, 45.0, 58.0, 77.0, 58.0, 72.0, 39.0, 35.0, 41.0, 58.0, 93.0, 111.0, 84.0, 89.0, 49.0, 60.0, 66.0, 95.0, 81.0, 98.0, 75.0, 38.0, 37.0, 81.0, 85.0, 75.0, 93.0, 83.0, 52.0, 30.0, 88.0, 89.0, 88.0, 69.0, 50.0, 32.0, 30.0, 78.0, 114.0, 71.0, 76.0, 49.0, 40.0, 16.0, 51.0, 61.0, 47.0, 46.0, 49.0, 26.0, 52.0, 73.0, 85.0, 68.0, 57.0, 57.0, 34.0, 27.0, 71.0, 56.0, 67.0, 62.0, 52.0, 37.0, 25.0, 58.0, 64.0, 61.0, 56.0, 54.0, 40.0, 32.0, 47.0, 56.0, 92.0, 76.0, 52.0, 29.0, 30.0, 50.0, 66.0, 87.0, 62.0, 40.0, 32.0, 36.0, 45.0, 84.0, 43.0, 58.0, 53.0, 50.0, 27.0, 51.0, 60.0, 48.0, 53.0, 42.0, 23.0, 23.0, 56.0, 60.0, 74.0, 63.0, 47.0, 31.0, 30.0, 76.0, 50.0, 61.0, 71.0, 52.0, 30.0, 18.0, 61.0, 31.0, 76.0, 57.0, 50.0, 39.0, 29.0, 66.0, 36.0, 42.0, 54.0, 63.0, 22.0, 44.0, 54.0, 52.0, 31.0, 37.0, 56.0, 43.0, 56.0, 37.0, 70.0, 61.0, 44.0, 47.0, 16.0, 30.0, 59.0, 55.0, 49.0, 62.0, 56.0, 40.0, 32.0, 55.0, 46.0, 62.0, 46.0, 52.0, 28.0, 29.0, 60.0, 55.0, 51.0, 52.0, 45.0, 80.0, 38.0, 83.0, 52.0, 91.0, 69.0, 57.0, 23.0, 55.0, 63.0, 62.0, 24.0, 76.0, 30.0, 55.0, 32.0, 63.0, 40.0, 55.0, 74.0, 95.0, 38.0, 30.0, 77.0, 62.0, 54.0, 59.0, 63.0, 96.0, 43.0, 223.0, 26.0, 83.0, 27.0, 198.0, 67.0, 84.0, 154.0, 292.0, 233.0, 57.0, 183.0, 39.0, 207.0, 170.0, 137.0, 107.0, 360.0, 65.0, 60.0, 142.0, 60.0, 206.0, 136.0, 98.0, 75.0, 91.0, 98.0, 73.0, 67.0, 50.0, 53.0, 22.0, 80.0, 88.0, 26.0, 46.0, 84.0, 53.0, 84.0, 91.0, 129.0, 40.0, 80.0, 180.0, 86.0, 123.0, 106.0, 56.0, 67.0, 72.0, 71.0, 92.0, 46.0, 42.0, 73.0, 84.0, 74.0, 86.0, 105.0, 100.0, 42.0, 70.0, 43.0, 72.0, 52.0, 60.0, 96.0, 75.0, 79.0, 91.0, 64.0, 35.0, 46.0]
		bestkey=autoarima(ts['value'])
		assert bestkey==(0, 1, 1)
	def test_arima_aic_fit(self):
		ts={}
		ts['value']=[93.0, 51.0, 45.0, 101.0, 216.0, 169.0, 127.0, 105.0, 49.0, 59.0, 108.0, 118.0, 135.0, 127.0, 73.0, 40.0, 51.0, 75.0, 98.0, 81.0, 78.0, 62.0, 39.0, 41.0, 70.0, 60.0, 76.0, 109.0, 109.0, 38.0, 40.0, 81.0, 89.0, 107.0, 79.0, 64.0, 37.0, 36.0, 55.0, 70.0, 65.0, 81.0, 63.0, 33.0, 40.0, 51.0, 73.0, 50.0, 69.0, 65.0, 43.0, 35.0, 59.0, 84.0, 54.0, 184.0, 80.0, 24.0, 24.0, 64.0, 69.0, 60.0, 47.0, 70.0, 32.0, 45.0, 58.0, 77.0, 58.0, 72.0, 39.0, 35.0, 41.0, 58.0, 93.0, 111.0, 84.0, 89.0, 49.0, 60.0, 66.0, 95.0, 81.0, 98.0, 75.0, 38.0, 37.0, 81.0, 85.0, 75.0, 93.0, 83.0, 52.0, 30.0, 88.0, 89.0, 88.0, 69.0, 50.0, 32.0, 30.0, 78.0, 114.0, 71.0, 76.0, 49.0, 40.0, 16.0, 51.0, 61.0, 47.0, 46.0, 49.0, 26.0, 52.0, 73.0, 85.0, 68.0, 57.0, 57.0, 34.0, 27.0, 71.0, 56.0, 67.0, 62.0, 52.0, 37.0, 25.0, 58.0, 64.0, 61.0, 56.0, 54.0, 40.0, 32.0, 47.0, 56.0, 92.0, 76.0, 52.0, 29.0, 30.0, 50.0, 66.0, 87.0, 62.0, 40.0, 32.0, 36.0, 45.0, 84.0, 43.0, 58.0, 53.0, 50.0, 27.0, 51.0, 60.0, 48.0, 53.0, 42.0, 23.0, 23.0, 56.0, 60.0, 74.0, 63.0, 47.0, 31.0, 30.0, 76.0, 50.0, 61.0, 71.0, 52.0, 30.0, 18.0, 61.0, 31.0, 76.0, 57.0, 50.0, 39.0, 29.0, 66.0, 36.0, 42.0, 54.0, 63.0, 22.0, 44.0, 54.0, 52.0, 31.0, 37.0, 56.0, 43.0, 56.0, 37.0, 70.0, 61.0, 44.0, 47.0, 16.0, 30.0, 59.0, 55.0, 49.0, 62.0, 56.0, 40.0, 32.0, 55.0, 46.0, 62.0, 46.0, 52.0, 28.0, 29.0, 60.0, 55.0, 51.0, 52.0, 45.0, 80.0, 38.0, 83.0, 52.0, 91.0, 69.0, 57.0, 23.0, 55.0, 63.0, 62.0, 24.0, 76.0, 30.0, 55.0, 32.0, 63.0, 40.0, 55.0, 74.0, 95.0, 38.0, 30.0, 77.0, 62.0, 54.0, 59.0, 63.0, 96.0, 43.0, 223.0, 26.0, 83.0, 27.0, 198.0, 67.0, 84.0, 154.0, 292.0, 233.0, 57.0, 183.0, 39.0, 207.0, 170.0, 137.0, 107.0, 360.0, 65.0, 60.0, 142.0, 60.0, 206.0, 136.0, 98.0, 75.0, 91.0, 98.0, 73.0, 67.0, 50.0, 53.0, 22.0, 80.0, 88.0, 26.0, 46.0, 84.0, 53.0, 84.0, 91.0, 129.0, 40.0, 80.0, 180.0, 86.0, 123.0, 106.0, 56.0, 67.0, 72.0, 71.0, 92.0, 46.0, 42.0, 73.0, 84.0, 74.0, 86.0, 105.0, 100.0, 42.0, 70.0, 43.0, 72.0, 52.0, 60.0, 96.0, 75.0, 79.0, 91.0, 64.0, 35.0, 46.0]
		fit=arima_aic(ts['value'],(0,0,0))
		print("test_arima_aic_fit fit")
		print(fit)
		assert round(fit,0)==3368
	def test_arima_aic_fit2(self):
		ts={}
		ts['value']=[93.0, 51.0, 45.0, 101.0, 216.0, 169.0, 127.0, 105.0, 49.0, 59.0, 108.0, 118.0, 135.0, 127.0, 73.0, 40.0, 51.0, 75.0, 98.0, 81.0, 78.0, 62.0, 39.0, 41.0, 70.0, 60.0, 76.0, 109.0, 109.0, 38.0, 40.0, 81.0, 89.0, 107.0, 79.0, 64.0, 37.0, 36.0, 55.0, 70.0, 65.0, 81.0, 63.0, 33.0, 40.0, 51.0, 73.0, 50.0, 69.0, 65.0, 43.0, 35.0, 59.0, 84.0, 54.0, 184.0, 80.0, 24.0, 24.0, 64.0, 69.0, 60.0, 47.0, 70.0, 32.0, 45.0, 58.0, 77.0, 58.0, 72.0, 39.0, 35.0, 41.0, 58.0, 93.0, 111.0, 84.0, 89.0, 49.0, 60.0, 66.0, 95.0, 81.0, 98.0, 75.0, 38.0, 37.0, 81.0, 85.0, 75.0, 93.0, 83.0, 52.0, 30.0, 88.0, 89.0, 88.0, 69.0, 50.0, 32.0, 30.0, 78.0, 114.0, 71.0, 76.0, 49.0, 40.0, 16.0, 51.0, 61.0, 47.0, 46.0, 49.0, 26.0, 52.0, 73.0, 85.0, 68.0, 57.0, 57.0, 34.0, 27.0, 71.0, 56.0, 67.0, 62.0, 52.0, 37.0, 25.0, 58.0, 64.0, 61.0, 56.0, 54.0, 40.0, 32.0, 47.0, 56.0, 92.0, 76.0, 52.0, 29.0, 30.0, 50.0, 66.0, 87.0, 62.0, 40.0, 32.0, 36.0, 45.0, 84.0, 43.0, 58.0, 53.0, 50.0, 27.0, 51.0, 60.0, 48.0, 53.0, 42.0, 23.0, 23.0, 56.0, 60.0, 74.0, 63.0, 47.0, 31.0, 30.0, 76.0, 50.0, 61.0, 71.0, 52.0, 30.0, 18.0, 61.0, 31.0, 76.0, 57.0, 50.0, 39.0, 29.0, 66.0, 36.0, 42.0, 54.0, 63.0, 22.0, 44.0, 54.0, 52.0, 31.0, 37.0, 56.0, 43.0, 56.0, 37.0, 70.0, 61.0, 44.0, 47.0, 16.0, 30.0, 59.0, 55.0, 49.0, 62.0, 56.0, 40.0, 32.0, 55.0, 46.0, 62.0, 46.0, 52.0, 28.0, 29.0, 60.0, 55.0, 51.0, 52.0, 45.0, 80.0, 38.0, 83.0, 52.0, 91.0, 69.0, 57.0, 23.0, 55.0, 63.0, 62.0, 24.0, 76.0, 30.0, 55.0, 32.0, 63.0, 40.0, 55.0, 74.0, 95.0, 38.0, 30.0, 77.0, 62.0, 54.0, 59.0, 63.0, 96.0, 43.0, 223.0, 26.0, 83.0, 27.0, 198.0, 67.0, 84.0, 154.0, 292.0, 233.0, 57.0, 183.0, 39.0, 207.0, 170.0, 137.0, 107.0, 360.0, 65.0, 60.0, 142.0, 60.0, 206.0, 136.0, 98.0, 75.0, 91.0, 98.0, 73.0, 67.0, 50.0, 53.0, 22.0, 80.0, 88.0, 26.0, 46.0, 84.0, 53.0, 84.0, 91.0, 129.0, 40.0, 80.0, 180.0, 86.0, 123.0, 106.0, 56.0, 67.0, 72.0, 71.0, 92.0, 46.0, 42.0, 73.0, 84.0, 74.0, 86.0, 105.0, 100.0, 42.0, 70.0, 43.0, 72.0, 52.0, 60.0, 96.0, 75.0, 79.0, 91.0, 64.0, 35.0, 46.0]
		fit=arima_aic(ts['value'],(1,1,1))
		print("test_arima_aic_fit2 fit")
		print(fit)
		assert round(fit,0)==3289
	def test_isNaN(self):
		shouldbefalse=isNaN(100)
		assert shouldbefalse==False
	def test_isNaN2(self):
		shouldbetrue=isNaN(float('NaN'))
		assert shouldbetrue==True
	def test_forecast_expected_value(self):
		ts={}
		ts['value']=[93.0, 51.0, 45.0, 101.0, 216.0, 169.0, 127.0, 105.0, 49.0, 59.0, 108.0, 118.0, 135.0, 127.0, 73.0, 40.0, 51.0, 75.0, 98.0, 81.0, 78.0, 62.0, 39.0, 41.0, 70.0, 60.0, 76.0, 109.0, 109.0, 38.0, 40.0, 81.0, 89.0, 107.0, 79.0, 64.0, 37.0, 36.0, 55.0, 70.0, 65.0, 81.0, 63.0, 33.0, 40.0, 51.0, 73.0, 50.0, 69.0, 65.0, 43.0, 35.0, 59.0, 84.0, 54.0, 184.0, 80.0, 24.0, 24.0, 64.0, 69.0, 60.0, 47.0, 70.0, 32.0, 45.0, 58.0, 77.0, 58.0, 72.0, 39.0, 35.0, 41.0, 58.0, 93.0, 111.0, 84.0, 89.0, 49.0, 60.0, 66.0, 95.0, 81.0, 98.0, 75.0, 38.0, 37.0, 81.0, 85.0, 75.0, 93.0, 83.0, 52.0, 30.0, 88.0, 89.0, 88.0, 69.0, 50.0, 32.0, 30.0, 78.0, 114.0, 71.0, 76.0, 49.0, 40.0, 16.0, 51.0, 61.0, 47.0, 46.0, 49.0, 26.0, 52.0, 73.0, 85.0, 68.0, 57.0, 57.0, 34.0, 27.0, 71.0, 56.0, 67.0, 62.0, 52.0, 37.0, 25.0, 58.0, 64.0, 61.0, 56.0, 54.0, 40.0, 32.0, 47.0, 56.0, 92.0, 76.0, 52.0, 29.0, 30.0, 50.0, 66.0, 87.0, 62.0, 40.0, 32.0, 36.0, 45.0, 84.0, 43.0, 58.0, 53.0, 50.0, 27.0, 51.0, 60.0, 48.0, 53.0, 42.0, 23.0, 23.0, 56.0, 60.0, 74.0, 63.0, 47.0, 31.0, 30.0, 76.0, 50.0, 61.0, 71.0, 52.0, 30.0, 18.0, 61.0, 31.0, 76.0, 57.0, 50.0, 39.0, 29.0, 66.0, 36.0, 42.0, 54.0, 63.0, 22.0, 44.0, 54.0, 52.0, 31.0, 37.0, 56.0, 43.0, 56.0, 37.0, 70.0, 61.0, 44.0, 47.0, 16.0, 30.0, 59.0, 55.0, 49.0, 62.0, 56.0, 40.0, 32.0, 55.0, 46.0, 62.0, 46.0, 52.0, 28.0, 29.0, 60.0, 55.0, 51.0, 52.0, 45.0, 80.0, 38.0, 83.0, 52.0, 91.0, 69.0, 57.0, 23.0, 55.0, 63.0, 62.0, 24.0, 76.0, 30.0, 55.0, 32.0, 63.0, 40.0, 55.0, 74.0, 95.0, 38.0, 30.0, 77.0, 62.0, 54.0, 59.0, 63.0, 96.0, 43.0, 223.0, 26.0, 83.0, 27.0, 198.0, 67.0, 84.0, 154.0, 292.0, 233.0, 57.0, 183.0, 39.0, 207.0, 170.0, 137.0, 107.0, 360.0, 65.0, 60.0, 142.0, 60.0, 206.0, 136.0, 98.0, 75.0, 91.0, 98.0, 73.0, 67.0, 50.0, 53.0, 22.0, 80.0, 88.0, 26.0, 46.0, 84.0, 53.0, 84.0, 91.0, 129.0, 40.0, 80.0, 180.0, 86.0, 123.0, 106.0, 56.0, 67.0, 72.0, 71.0, 92.0, 46.0, 42.0, 73.0, 84.0, 74.0, 86.0, 105.0, 100.0, 42.0, 70.0, 43.0, 72.0, 52.0, 60.0, 96.0, 75.0, 79.0, 91.0, 64.0, 35.0, 46.0]
		ts['point']=range(1,(len(ts['value'])+1))
		elements=forecast(ts,10)
		assert elements['expected_value']==[63.71645486632963, 63.61287431854249, 63.50929377075535, 63.40571322296821, 63.30213267518107, 63.19855212739393, 63.09497157960679, 62.99139103181965, 62.887810484032514, 62.784229936245374]
	def test_forecast_actual_value(self):
		ts={}
		ts['value']=[93.0, 51.0, 45.0, 101.0, 216.0, 169.0, 127.0, 105.0, 49.0, 59.0, 108.0, 118.0, 135.0, 127.0, 73.0, 40.0, 51.0, 75.0, 98.0, 81.0, 78.0, 62.0, 39.0, 41.0, 70.0, 60.0, 76.0, 109.0, 109.0, 38.0, 40.0, 81.0, 89.0, 107.0, 79.0, 64.0, 37.0, 36.0, 55.0, 70.0, 65.0, 81.0, 63.0, 33.0, 40.0, 51.0, 73.0, 50.0, 69.0, 65.0, 43.0, 35.0, 59.0, 84.0, 54.0, 184.0, 80.0, 24.0, 24.0, 64.0, 69.0, 60.0, 47.0, 70.0, 32.0, 45.0, 58.0, 77.0, 58.0, 72.0, 39.0, 35.0, 41.0, 58.0, 93.0, 111.0, 84.0, 89.0, 49.0, 60.0, 66.0, 95.0, 81.0, 98.0, 75.0, 38.0, 37.0, 81.0, 85.0, 75.0, 93.0, 83.0, 52.0, 30.0, 88.0, 89.0, 88.0, 69.0, 50.0, 32.0, 30.0, 78.0, 114.0, 71.0, 76.0, 49.0, 40.0, 16.0, 51.0, 61.0, 47.0, 46.0, 49.0, 26.0, 52.0, 73.0, 85.0, 68.0, 57.0, 57.0, 34.0, 27.0, 71.0, 56.0, 67.0, 62.0, 52.0, 37.0, 25.0, 58.0, 64.0, 61.0, 56.0, 54.0, 40.0, 32.0, 47.0, 56.0, 92.0, 76.0, 52.0, 29.0, 30.0, 50.0, 66.0, 87.0, 62.0, 40.0, 32.0, 36.0, 45.0, 84.0, 43.0, 58.0, 53.0, 50.0, 27.0, 51.0, 60.0, 48.0, 53.0, 42.0, 23.0, 23.0, 56.0, 60.0, 74.0, 63.0, 47.0, 31.0, 30.0, 76.0, 50.0, 61.0, 71.0, 52.0, 30.0, 18.0, 61.0, 31.0, 76.0, 57.0, 50.0, 39.0, 29.0, 66.0, 36.0, 42.0, 54.0, 63.0, 22.0, 44.0, 54.0, 52.0, 31.0, 37.0, 56.0, 43.0, 56.0, 37.0, 70.0, 61.0, 44.0, 47.0, 16.0, 30.0, 59.0, 55.0, 49.0, 62.0, 56.0, 40.0, 32.0, 55.0, 46.0, 62.0, 46.0, 52.0, 28.0, 29.0, 60.0, 55.0, 51.0, 52.0, 45.0, 80.0, 38.0, 83.0, 52.0, 91.0, 69.0, 57.0, 23.0, 55.0, 63.0, 62.0, 24.0, 76.0, 30.0, 55.0, 32.0, 63.0, 40.0, 55.0, 74.0, 95.0, 38.0, 30.0, 77.0, 62.0, 54.0, 59.0, 63.0, 96.0, 43.0, 223.0, 26.0, 83.0, 27.0, 198.0, 67.0, 84.0, 154.0, 292.0, 233.0, 57.0, 183.0, 39.0, 207.0, 170.0, 137.0, 107.0, 360.0, 65.0, 60.0, 142.0, 60.0, 206.0, 136.0, 98.0, 75.0, 91.0, 98.0, 73.0, 67.0, 50.0, 53.0, 22.0, 80.0, 88.0, 26.0, 46.0, 84.0, 53.0, 84.0, 91.0, 129.0, 40.0, 80.0, 180.0, 86.0, 123.0, 106.0, 56.0, 67.0, 72.0, 71.0, 92.0, 46.0, 42.0, 73.0, 84.0, 74.0, 86.0, 105.0, 100.0, 42.0, 70.0, 43.0, 72.0, 52.0, 60.0, 96.0, 75.0, 79.0, 91.0, 64.0, 35.0, 46.0]
		ts['point']=range(1,(len(ts['value'])+1))
		elements=forecast(ts,10)
		assert elements['actual_value']==[]
	def test_forecast_predictions(self):
		ts={}
		ts['value']=[93.0, 51.0, 45.0, 101.0, 216.0, 169.0, 127.0, 105.0, 49.0, 59.0, 108.0, 118.0, 135.0, 127.0, 73.0, 40.0, 51.0, 75.0, 98.0, 81.0, 78.0, 62.0, 39.0, 41.0, 70.0, 60.0, 76.0, 109.0, 109.0, 38.0, 40.0, 81.0, 89.0, 107.0, 79.0, 64.0, 37.0, 36.0, 55.0, 70.0, 65.0, 81.0, 63.0, 33.0, 40.0, 51.0, 73.0, 50.0, 69.0, 65.0, 43.0, 35.0, 59.0, 84.0, 54.0, 184.0, 80.0, 24.0, 24.0, 64.0, 69.0, 60.0, 47.0, 70.0, 32.0, 45.0, 58.0, 77.0, 58.0, 72.0, 39.0, 35.0, 41.0, 58.0, 93.0, 111.0, 84.0, 89.0, 49.0, 60.0, 66.0, 95.0, 81.0, 98.0, 75.0, 38.0, 37.0, 81.0, 85.0, 75.0, 93.0, 83.0, 52.0, 30.0, 88.0, 89.0, 88.0, 69.0, 50.0, 32.0, 30.0, 78.0, 114.0, 71.0, 76.0, 49.0, 40.0, 16.0, 51.0, 61.0, 47.0, 46.0, 49.0, 26.0, 52.0, 73.0, 85.0, 68.0, 57.0, 57.0, 34.0, 27.0, 71.0, 56.0, 67.0, 62.0, 52.0, 37.0, 25.0, 58.0, 64.0, 61.0, 56.0, 54.0, 40.0, 32.0, 47.0, 56.0, 92.0, 76.0, 52.0, 29.0, 30.0, 50.0, 66.0, 87.0, 62.0, 40.0, 32.0, 36.0, 45.0, 84.0, 43.0, 58.0, 53.0, 50.0, 27.0, 51.0, 60.0, 48.0, 53.0, 42.0, 23.0, 23.0, 56.0, 60.0, 74.0, 63.0, 47.0, 31.0, 30.0, 76.0, 50.0, 61.0, 71.0, 52.0, 30.0, 18.0, 61.0, 31.0, 76.0, 57.0, 50.0, 39.0, 29.0, 66.0, 36.0, 42.0, 54.0, 63.0, 22.0, 44.0, 54.0, 52.0, 31.0, 37.0, 56.0, 43.0, 56.0, 37.0, 70.0, 61.0, 44.0, 47.0, 16.0, 30.0, 59.0, 55.0, 49.0, 62.0, 56.0, 40.0, 32.0, 55.0, 46.0, 62.0, 46.0, 52.0, 28.0, 29.0, 60.0, 55.0, 51.0, 52.0, 45.0, 80.0, 38.0, 83.0, 52.0, 91.0, 69.0, 57.0, 23.0, 55.0, 63.0, 62.0, 24.0, 76.0, 30.0, 55.0, 32.0, 63.0, 40.0, 55.0, 74.0, 95.0, 38.0, 30.0, 77.0, 62.0, 54.0, 59.0, 63.0, 96.0, 43.0, 223.0, 26.0, 83.0, 27.0, 198.0, 67.0, 84.0, 154.0, 292.0, 233.0, 57.0, 183.0, 39.0, 207.0, 170.0, 137.0, 107.0, 360.0, 65.0, 60.0, 142.0, 60.0, 206.0, 136.0, 98.0, 75.0, 91.0, 98.0, 73.0, 67.0, 50.0, 53.0, 22.0, 80.0, 88.0, 26.0, 46.0, 84.0, 53.0, 84.0, 91.0, 129.0, 40.0, 80.0, 180.0, 86.0, 123.0, 106.0, 56.0, 67.0, 72.0, 71.0, 92.0, 46.0, 42.0, 73.0, 84.0, 74.0, 86.0, 105.0, 100.0, 42.0, 70.0, 43.0, 72.0, 52.0, 60.0, 96.0, 75.0, 79.0, 91.0, 64.0, 35.0, 46.0]
		ts['point']=range(1,(len(ts['value'])+1))
		elements=forecast(ts,10)
		assert elements['predictions']==[[-6.774103343207628, 134.20701307586688], [-7.7570333437349674, 134.98278198081994], [-8.729259943669632, 135.74784748518033], [-9.691164725284231, 136.50259117122064], [-10.643107123007198, 137.24737247336935], [-11.585426182411275, 137.98253043719913], [-12.518442143563178, 138.70838530277678], [-13.44245786970513, 139.42523993334444], [-14.357760139343497, 140.13338110740852], [-15.264620817374471, 140.83308068986523]]
	def test_history_expected_value(self):
		ts={}
		ts['value']=[93.0, 51.0, 45.0, 101.0, 216.0, 169.0, 127.0, 105.0, 49.0, 59.0]
		ts['point']=range(1,(len(ts['value'])+1))
		elements=history(ts,10)
		assert elements['expected_value']==[None, None, None, None, 206.0, 383.33333361919733, 120.75, 85.0, 86.33333333333334, -9.0, 75.5, 98.5, 127.99999999999999, 163.99999999999997, 206.49999999999994, 255.49999999999994, 310.99999999999994, 372.99999999999994, 441.49999999999994, 516.4999999999999]
	def test_history_actual_value(self):
		ts={}
		ts['value']=[93.0, 51.0, 45.0, 101.0, 216.0, 169.0, 127.0, 105.0, 49.0, 59.0]
		ts['point']=range(1,(len(ts['value'])+1))
		elements=history(ts,10)
		assert elements['actual_value']==[93.0, 51.0, 45.0, 101.0, 216.0, 169.0, 127.0, 105.0, 49.0, 59.0, None, None, None, None, None, None, None, None, None, None]
	def test_history_predictions(self):
		ts={}
		ts['value']=[93.0, 51.0, 45.0, 101.0, 216.0, 169.0, 127.0, 105.0, 49.0, 59.0]
		ts['point']=range(1,(len(ts['value'])+1))
		elements=history(ts,10)
		assert elements['predictions']==[None, None, None, None, [180.5204682009793, 231.4795317990207], [360.56998342561087, 406.0966838127838], [-62.21751943027439, 303.71751943027436], [-78.72446259128048, 248.72446259128048], [-63.83822662814467, 236.50489329481135], [-150.36995403754275, 132.36995403754275], [-63.89188898594816, 214.89188898594816], [-213.18973928468426, 410.18973928468426], [-393.55669108064603, 649.556691080646], [-599.4808193085971, 927.4808193085971], [-827.2579162109951, 1240.257916210995], [-1074.213872632549, 1585.213872632549], [-1338.3070727156676, 1960.3070727156676], [-1617.914397425078, 2363.914397425078], [-1911.7059267720715, 2794.7059267720715], [-2218.5663621386398, 3251.5663621386398]]		
	# def test_readTextFile(self):
		# elements=readTextFile()
		# assert elements!=[]


if __name__ == '__main__':
	unittest.main()
