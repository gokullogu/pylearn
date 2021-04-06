import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pydb1"
)

mycur=mydb.cursor()

mycur.execute('select * from pytb1 group by name')

myres=mycur.fetchall()

for x in myres:
    print(x)
"""
('gokul', 19)
('tharun', 19)
('ram', 27)
('vishnu', 19)
('kavya', 17)
('ram', 27)
('vishnu', 19)
('kavya', 17)
('ram', 27)
('vishnu', 19)
('kavya', 17)
"""

"""
mycur.execute('select name from pytb1')
('gokul',)
('tharun',)
('ram',)
('vishnu',)
('kavya',)
('ram',)
('vishnu',)
('kavya',)
('ram',)
('vishnu',)
('kavya',)

"""

