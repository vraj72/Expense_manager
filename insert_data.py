import mysql.connector as con
mycon=con.connect(host="localhost",user="viraj",passwd="qwerty",database="Expense_manager")
mycur=mycon.cursor()

class insert_data():
	"""docstring for insert_data"""
	def __init__(self, arg):
		super(insert_data, self).__init__()
		self.arg = arg
		
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
