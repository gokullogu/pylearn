import mysql.connector

#connecting to database
mydb=mysql.connector.connect(
host="localhost",
user="root",
password=""
)

print(mydb)


