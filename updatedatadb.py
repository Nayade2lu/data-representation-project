import mysql.connector
db = mysql.connector.connect(
 host="localhost",
 user="root",
 password="",

 database="datarep2"
)
cursor = db.cursor()
sql="update countriestable2 set countryname= %s, equalityrate=%s where id = %s"
values = ("NewZeland",33, 1)
cursor.execute(sql, values)
db.commit()
print("update done")