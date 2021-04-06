import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

mycur=mydb.cursor()

mycur.execute("create database pydb1")
