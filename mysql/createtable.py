import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",user="root",password="",database="pydb1"
)

mycur=mydb.cursor()

mycur.execute('create table pytb1(name varchar(100),age int(100))')

