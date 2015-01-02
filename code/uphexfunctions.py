import datetime
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.arima_model import ARIMA

dir="/cygdrive/c/Users/cjacobik/Desktop/Personal/uphex"
dir="/home/cjacobik/uphex"

def forecast(series,n):
	# print series
	nseries={}

	series=runarimaforecast(series,n)
	nseries=fill_series(series,i=(len(series['point'])-n))
	return nseries

def runforecast(series,n,minrequired=4,lookback=2):
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
	print('history function series')
	print(series)
	returnelements={}
	for i in range(0,(len(series['point'])+n)):
		series2=fill_series(series,j=i)
		print("history series2")
		print(series2)
		elements=runarimaforecast(series2,n)
		print("history elements")
		print(elements)
		temp_predictions=elements['value']
		elements=fill_series(elements,i=i,j=(i+1))
		elements['actual_value']=series['value'][i:(i+1)]
		elements['predictions'].append(temp_predictions)
		print("history elements")
		print(elements)
		elements['expected_value']=elements['value']
		returnelements=appendelements(returnelements,elements)
	return returnelements


def fill_series(ser,i=None,j=None):
	ser2={}
	for key in ser.iterkeys():
		ser2[key]=ser[key][i:j]
	return ser2




def arima_aic(values,order):
	#fit=ARIMA(values, order=order).fit(disp=False,skip_hessian=True,full_output=False)
	fit=ARIMA(values, order=order).fit()
	return fit.aic

def autoarima(y):
	print('autoarima')
	aics={}
	for i in range(0,3):
		for j in range(0,3):
			for k in range(0,3):
				if(len(y)>(i+j+k)):
					try:
						aic=arima_aic(y,(i,j,k))
						#print(' '.join(['i','j','k','aic']))
						#print(' '.join(str([i,j,k,aic])))
						aics[(i,j,k)]=aic
					except:
						pass
	first=True
	for key in aics.iterkeys():
		val=aics[key]
		if not (isNaN(val)):
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

def runarimaforecast(series,n,minrequired=4,lookback=2):
	if len(series['value'])<minrequired:
		return series
	print("series")
	print(series)	
	bestkey=autoarima(series['value'])
	print("bestkey")
	print(bestkey)
	if(bestkey!=0):
		maxpoint=max(series['point'])
		model=ARIMA(series['value'], order=bestkey).fit()
		predict_model=model.forecast(n)
		print('\npredict')
		print(predict_model[0])
		series['point'].extend(range((maxpoint+1),(maxpoint+n+1)))
		series['value'].extend(predict_model[0].tolist())
	return series

def isNaN(x):
    return str(float(x)).lower() == 'nan'




















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

