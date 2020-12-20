import mysql.connector
db = mysql.connector.connect(
 host="localhost",
 user="root",
 password="andorra1",
 database="datarep2"
)
cursor = db.cursor()
sql="select * from countriestable2 where id = %s"
values = (1,)
cursor.execute(sql, values)
result = cursor.fetchall()
for x in result:
 print(x)