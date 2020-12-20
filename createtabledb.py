import mysql.connector
mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="",
 database="datarep2"
)
mycursor = mydb.cursor()
sql="CREATE TABLE countriestable2 (id INT AUTO_INCREMENT PRIMARY KEY, countryname VARCHAR(255), continent VARCHAR (100), equalityrate INT)"
mycursor.execute(sql)