import datetime

dir="/cygdrive/c/Users/cjacobik/Desktop/Personal/uphex"

def forecast(series,n):
	# print series
	nseries={}

	series=runforecast(series,n)
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
		elements2=runforecast(series2,n)
		elements2=fill_series(elements2,i=i,j=(i+1))
		elements2['actual_value']=series['value'][i:(i+1)]
		# print "elements 2 "+str(i)
		# print elements2
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

def readTextFile(filename="observations.csv"):
	header=False
	dirfilename=dir+"/"+filename
	d={}
	with open(dirfilename,'rb') as source:
		for line in source:
			if header:
				fields=line.split(',')
				print fields[1]
				fields[1]=datetime.datetime.strptime(fields[1][0:19],"%Y-%m-%d %H:%M:%S")
				d[fields[4],fields[1]]=fields[2]
			header=True
	print d
	return d

