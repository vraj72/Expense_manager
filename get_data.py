import mysql.connector as con
mycon=con.connect(host="localhost",user="*****",passwd="******",database="Expense_manager")
mycur=mycon.cursor()
from mysql.connector import Error

class get_data ():

	def __init__(self,id):
		self.id=id
	
	def display(self):
		mycur.execute("SELECT * FROM user")
		record=mycur.fetchall()
		print(record[0][1])

	def get_name(self):
		val=[]
		val.append(self.id)
		print(val)
		sql="SELECT * FROM user where id=%s"
		mycur.execute(sql,val)
		record=mycur.fetchall()
		try:
			return(record[0][1])
		except Exception as e:
			print("Id not found")
			return(-1)

	def expense_data_total(self):
		val=[]
		val.append(self.id)
		#sql="SELECT type , sum(amount) FROM expense where id=%s"
		sql="SELECT type , sum(amount) as t FROM expense where id='2017135040' group by type "
		record=mycur.execute(sql)
		record=mycur.fetchall()
		print(record)
		return(record)
		
	def income_data_total(self):
		val=[]
		val.append(self.id)
		#sql="SELECT type , sum(amount) FROM expense where id=%s"
		sql="SELECT type , sum(amount) as t FROM income where id=%s group by type "
		record=mycur.execute(sql,val)
		record=mycur.fetchall()
		print(record)
		return(record)

	def ei_total(self):
		val=[]
		val.append(self.id)
		#sql="SELECT type , sum(amount) FROM expense where id=%s"
		sql="SELECT  sum(amount) as income FROM income where id=%s"
		record=mycur.execute(sql,val)
		record=mycur.fetchall()
		print(record)
		sql="SELECT  sum(amount) as  expense from expense where id=%s"
		record2=mycur.execute(sql,val)
		record2=mycur.fetchall()
		print(record2)
		return(record,record2)

	def recentq(self):
		val=[]
		val.append(self.id)
		#sql="SELECT type , sum(amount) FROM expense where id=%s"
		sql="SELECT *  FROM income where id=%s order by date"
		record=mycur.execute(sql,val)
		record=mycur.fetchall()
		
		return record
		#return(record)

	def insert_e(id,type,amount,date,desc):
		val=[]
		
		val.append(id)
		val.append(type)
		val.append(amount)
		val.append(date)
		val.append(desc)
		print("values im going to insert ************",str(val))
		sql="INSERT INTO expense VALUES(%s,%s,%s,%s,%s)"
		mycur.execute(sql,val)
		mycon.commit()
		print("Commited")
		sql="SELECT type , sum(amount) as t FROM expense where id='2017135040' group by type "
		mycur.execute(sql)
		record=mycur.fetchall()
		print("after commited:-"+str(record))
		return 1
		print("returned but still here")


	def insert_i(id,type,amount,date,desc):
		val=[]
		
		val.append(id)
		val.append(type)
		val.append(amount)
		val.append(date)
		val.append(desc)
		
		sql="INSERT INTO income VALUES(%s,%s,%s,%s,%s)"
		mycur.execute(sql,val)
		mycon.commit()
		print("Commited")

	