import datetime
import numpy as np
from statsmodels.tsa.arima_process import arma_generate_sample
from statsmodels.tsa.arima_model import ARIMA

dir="/cygdrive/c/Users/cjacobik/Desktop/Personal/uphex"
dir="/home/cjacobik/uphex"

def forecast(series,n):
	# print series
	nseries={}

	series=runforecast2(series,n)
	nseries=fill_series(series,i=(len(series['point'])-n))
	return nseries

def runforecast(series,n,minrequired=1,lookback=2):
	start=len(series['point'])
	# print series

	if len(series['point'])<minrequired:
		return series

	for i in range(start,start+n):
		temp=series['value'][max(i-lookback,0):i]
		# print temp
		series['point'].append(max(series['point'][(i-1):])+1)
		series['value'].append(float(sum(temp))/len(temp))
	return series

def appendelements(series,appendseries):
	for key in appendseries.iterkeys():
		t=appendseries[key]
		if len(t)>0:
			tt=max(t)
		else:
			tt=None
		if key not in series.iterkeys():
			series[key]=[]
		series[key].append(tt)
	return series

def history(series,n):
	felements={}
	for i in range(0,(len(series['point'])+n)):
		series2=fill_series(series,j=i)
		elements2=runforecast2(series2,n)
		elements2=fill_series(elements2,i=i,j=(i+1))
		elements2['actual_value']=series['value'][i:(i+1)]
		print("elements 2 ")
		print(elements2)
		felements=appendelements(felements,elements2)
	return felements

# def add_key_series(ser,i,j):
	# ser[j]=ser[i]
	# return ser

def fill_series(ser,i=None,j=None):
	ser2={}
	for key in ser.iterkeys():
		ser2[key]=ser[key][i:j]
	return ser2




def arima_aic(values,order):
	fit=ARIMA(values, order=order).fit()
	return fit.aic

def autoarima(y):
	print('autoarima')
	aics={}
	for i in range(1,5):
		for j in range(1,5):
			for k in range(1,5):
				try:
					aic=arima_aic(y,(i,j,k))
					print(' '.join(['i','j','k','aic']))
					print(' '.join(str([i,j,k,aic])))
					aics[(i,j,k)]=aic
				except:
					print('passing')
					pass
	first=True
	for key in aics.iterkeys():
		val=aics[key]
		if first:
			bestaic=val
			bestkey=key
			first=False
		else:
			if val<bestaic:
				bestaic=val
				bestkey=key
		print(str(key)+' '+str(val))

	if first:
		print('no best aic found')
		return 0
	else:
		print('bestaic '+str(bestaic)+' bestkey '+str(bestkey))
		return bestkey

def runforecast2(series,n,minrequired=5,lookback=2):
	if len(series['value'])<minrequired:
		return series
	
	bestkey=autoarima(series['value'])
	if(bestkey!=0):
		maxpoint=max(series['point'])
		model=ARIMA(series['value'], order=bestkey).fit()
		#predict_model=model.predict((maxpoint+1),(maxpoint+n-1))
		predict_model=model.forecast(n)[0]
		print('\npredict')
		print(predict_model)
		series['point'].extend(range((maxpoint+1),(maxpoint+n+1)))
		series['value'].extend(predict_model.tolist())
	return series






















def readTextFile(metric,filename="observations.csv"):
	header=False
	dirfilename=dir+"/"+filename
	d=[]
	with open(dirfilename,'rb') as source:
		for line in source:
			if header:
				fields=line.rstrip().split(',')
				fields[1]=datetime.datetime.strptime(fields[1][0:19],"%Y-%m-%d %H:%M:%S")
				if int(fields[4])==metric:
					d.append(float(fields[2]))
				
			header=True
	print d
	return d

