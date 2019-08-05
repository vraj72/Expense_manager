import matplotlib.pyplot as plt
from get_data import get_data
import matplotlib as pltl
import datetime as dt
import matplotlib.dates as pltd

class create_graph():

	
	def ge1(self,id,c):
		t=get_data(id)
		print("In ge1\n\n\n\n")
		data=t.expense_data_total()
		print(data)
		print(len(data))
		size=[]
		labels=[]
		for i in range(0,len(data)):
			print(data[i][1])
			print(data[i][0])
			size.append(data[i][1])
			labels.append(data[i][0]+"\n"+str(data[i][1]))
		print(size)
		print(labels)
		
		ax = self.figure.add_subplot(111)
		ax.pie(size,labels=labels)
		self.draw()

	def gi1(self,id):
		t=get_data(id)
		data=t.income_data_total()
		print(data )
		print("from gi1")
		print(len(data))
		size=[]
		labels=[]
		for i in range(0,len(data)):
			print(data[i][1])
			print(data[i][0])
			size.append(data[i][1])
			labels.append(data[i][0]+"\n"+str(data[i][1]))
		print(size)
		print(labels)
		ax = self.figure.add_subplot(111)
		ax.pie(size,labels=labels)
		self.draw()

	def go1(self,id):
		t=get_data(id)
		data,data2=t.ei_total()
		print(data ,data2)
		print("from go1")
		size=[]
		size.append(int(data[0][0]))
		size.append(int(data2[0][0]))
		label=["income"+"\n"+str(size[0]),"expense"+"\n"+str(size[1])]
		print(size)
		print(label)
		ax = self.figure.add_subplot(111)
		ax.pie(size,labels=label)
		self.draw()

	def go2(self):
		list_of_datetimes=["1999-7-4","2015-7-6","2016-7-13","2017-8-4","2018-6-4"]
		list_of_datetimes.sort()
		print(list_of_datetimes) 
		values=["200","700","700","800","500"]
		values2=["300","400","500","850","58"]
		dates = pltd.datestr2num(list_of_datetimes)
		x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in list_of_datetimes]
		
		
		ax = self.figure.add_subplot(111)
		ax.plot(x, values)
		ax.plot(x, values2)
		#self.gcf().autofmt_xdate()
		self.draw()

	def go3(self):
		list_of_datetimes=["1999-7-4","2015-7-6","2016-7-13","2017-8-4","2018-6-4"]
		list_of_datetimes.sort()
		print(list_of_datetimes) 
		values=["1200","70","200","230","500"]
		#values2=["300","400","500","850","58"]
		dates = pltd.datestr2num(list_of_datetimes)
		x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in list_of_datetimes]
		
		
		ax = self.figure.add_subplot(111)
		ax.plot(x, values)
		#ax.plot(dates, values2)
		#self.gcf().autofmt_xdate()
		self.draw()

	def gi2(self):
		list_of_datetimes=["1999-7-4","2015-7-6","2016-7-13","2017-8-4","2018-6-4"]
		list_of_datetimes.sort()
		print(list_of_datetimes) 
		values=["20","760","70","24","650"]
		dates = pltd.datestr2num(list_of_datetimes)
		x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in list_of_datetimes]
		ax = self.figure.add_subplot(111)
		ax.plot(x, values)
		#self.gcf().autofmt_xdate()
		self.draw()


	def ge2(self):
		list_of_datetimes=["1999-7-4","2015-7-6","2016-7-13","2017-8-4","2018-6-4"]
		list_of_datetimes.sort()
		print(list_of_datetimes) 
		#values=[("1999-7-4","200"),("2015-7-6","208"),("2016-7-13","700"),("2017-8-4","40"),("2018-6-4","230")]
		values=["200","700","700","800","500"]
		dates = pltd.datestr2num(list_of_datetimes)
		x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in list_of_datetimes]
		ax = self.figure.add_subplot(111)
		ax.plot(x, values)
		plt.gcf().autofmt_xdate()
		self.draw()

	def go4(self,id):
		t=get_data(id)
		data=t.income_data_total()
		print(data )
		print("from gi1")
		print(len(data))
		size=[]
		labels=[]
		for i in range(0,len(data)):
			print(data[i][1])
			print(data[i][0])
			size.append(data[i][1])
			labels.append(data[i][0]+"\n"+str(data[i][1]))
		print(size)
		print(labels)
		data2=t.expense_data_total()
		print(data )
		print("from gi1")
		print(len(data2))
		for i in range(0,len(data)):
			print(data2[i][1])
			print(data2[i][0])
			size.append(data2[i][1])
			labels.append(data2[i][0]+"\n"+str(data2[i][1]))
		print(size)
		print(labels)
		
		ax = self.figure.add_subplot(111)
		ax.pie(size,labels=labels)
		self.draw()

	def recent(id):
		t=get_data(id)
		data=t.recentq()
		return data


#pyuic5 expense_manager.ui > xyz.py