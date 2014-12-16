

import unittest
from uphexfunctions import *


class TestSuite(unittest.TestCase):
	def test_number_forecast_elements(self):
		n=5
		ts={}
		ts['point']=[0,1,2,3,4,5,6,7,8]
		ts['value']=[0,1,2,3,4,5,6,7,8]
		elements=forecast(ts,n)
		assert len(elements['value'])==n
	def test_point_forecast_elements(self):
		n=2
		ts={}
		ts['point']=[0,1,2]
		ts['value']=[0,1,2]
		elements=forecast(ts,n)
		assert elements['point']==[3,4]
	def test_value_forecast_elements(self):
		n=2
		ts={}
		ts['point']=[0,1,2]
		ts['value']=[0,1,2]
		elements=forecast(ts,n)
		assert elements['value']==[1.5,1.75]
	def test_number_runforecast_elements(self):
		n=2
		ts={}
		ts['point']=[1,2,3]
		ts['value']=[1.0,2.0,3.0]
		l=(len(ts['value'])+n)
		elements=runforecast(ts,n)
		assert len(elements['value'])==l

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
		ts['point']=[0,1,2,3,4,5,6,7,8]
		ts['value']=[0,1,2,3,4,5,6,7,8]
		elements=history(ts,n)
		assert len(elements['value'])==(len(ts['value'])+n)
	def test_keys_history(self):
		n=5
		ts={}
		ts['point']=[0,1,2,3,4,5,6,7,8]
		ts['value']=[0,1,2,3,4,5,6,7,8]
		elements=history(ts,n)
		for key in elements.iterkeys():
			assert key in ['actual_value','value','point']
	def test_value_history_elements(self):
		n=5
		ts={}
		ts['point']=[0,1,2,3,4,5,6,7,8]
		ts['value']=[0,1,2,3,4,5,6,7,8]
		elements=history(ts,n)
		assert elements['value']==[None, 0.0, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 7.75, 7.625, 7.6875, 7.65625]
	def test_point_history_elements(self):
		n=5
		ts={}
		ts['point']=[0,1,2,3,4,5,6,7,8]
		ts['value']=[0,1,2,3,4,5,6,7,8]
		elements=history(ts,n)
		assert elements['point']==[None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
	def test_actual_value_history_elements(self):
		n=5
		ts={}
		ts['point']=[0,1,2,3,4,5,6,7,8]
		ts['value']=[0,1,2,3,4,5,6,7,8]
		elements=history(ts,n)
		assert elements['actual_value']==[0, 1, 2, 3, 4, 5, 6, 7, 8, None, None, None, None, None]
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
	# def test_readTextFile(self):
		# elements=readTextFile()
		# assert elements!=[]


if __name__ == '__main__':
	unittest.main()