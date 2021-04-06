import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",user="root",password="",database="pydb1"
)

mycur=mydb.cursor()

sql="insert into pytb1(name,age) values (%s,%s)"
val=('tharun','19')

mycur.execute(sql,val)

mydb.commit()

print(mycur.rowcount,"row inserted")

