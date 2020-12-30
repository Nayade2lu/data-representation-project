import mysql.connector
db = mysql.connector.connect(
 host="localhost",
 user="root",
 password="",

 database="datarepres2"
)
cursor = db.cursor()
sql="update countriestable2 set countryname= %s, continent=%s, equalityrate=%s where id = %s"
values = ("Iceland", "Europe",555, 3)
cursor.execute(sql, values)
db.commit()
print("update done")