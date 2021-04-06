import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database='pydb1'
)

mycur=mydb.cursor()
#to insert more rows in a table at a time
sql="insert into pytb1 values (%s,%s)"
val=[
    ('ram',27),
    ('vishnu',19),
    ('kavya',17)
]

mycur.executemany(sql,val)
mydb.commit()
print(mycur.rowcount,"rows inserted")
#3 more ri=ows inserted

#using cursor object to get the id of last inserted row
print(mycur.lastrowid)
