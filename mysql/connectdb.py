import mysql.connector

#to connect to specific database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pydb1"
)

mycur=mydb.cursor()
