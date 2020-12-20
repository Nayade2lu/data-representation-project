import mysql.connector
db = mysql.connector.connect(
 host="localhost",
 user="root",
 password="",
 database="datarep2"
)
cursor = db.cursor()
sql="delete from countriestable2 where id = %s"
values = (1,)
cursor.execute(sql, values)
db.commit()
print("delete done")