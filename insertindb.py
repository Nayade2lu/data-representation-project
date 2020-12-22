import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="datarepres2"
)
cursor = db.cursor()
sql="insert into countriestable2 (countryname, continent, equalityrate) values (%s,%s,%s )"
values = ("Island", "Europe", 555)
cursor.execute(sql, values)
db.commit()
print("1 record inserted, ID:", cursor.lastrowid)