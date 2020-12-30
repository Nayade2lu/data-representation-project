from mysql import mysql.connector
mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="andorra1"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE datarepres3	")