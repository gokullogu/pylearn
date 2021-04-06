import mysql.connector

mydb = mysql.connector.Connect(
    host="localhost",
    user="root",
    password="",
    database='pydb1'
)

mycur = mydb.cursor()

mycur.execute('select * from pytb1 order by age')

myres=mycur.fetchall()

for x in myres:
   print(x) 

"""
('kavya', 17)
('kavya', 17) 
('kavya', 17) 
('vishnu', 19)
('vishnu', 19)
('gokul', 19) 
('vishnu', 19)
('tharun', 19)
('ram', 27)   
('ram', 27)   
('ram', 27)   
"""
