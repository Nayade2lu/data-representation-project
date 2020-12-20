import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="andorra1",
    database="datarep2"
)
cursor = db.cursor()
sql="insert into countriestable2 (countryname, equalityrate) values (%s,%s)"
values = ("Canada2",22)
cursor.execute(sql, values)
db.commit()
print("1 record inserted, ID:", cursor.lastrowid)