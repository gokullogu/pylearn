import mysql.connector

mydb=mysql.connector.Connect(
    host="localhost",
    user='root',
    password='',
    database='pydb1'
)

mycur=mydb.cursor()

mycur.execute('select * from pytb1 where name="ram"')

myres = mycur.fetchall()

for x in myres:
    print(x)
    """
('ram', 27)
('ram', 27)
('ram', 27)
    """

#to prevent sql injection
sql="select * from pytb1 where name=%s"
adr=('gokul',)

mycur.execute(sql,adr)

myres2=mycur.fetchall()

for i in myres2:
    print(i)
#('gokul', 19)
