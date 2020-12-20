import mysql.connector
class CountriesDAO:
 db=""
 def __init__(self):
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="andorra1",
        database="datarep2"
        )
 def create(self, values):
        cursor = self.db.cursor()
        sql="insert into countriestable2 (countryname, equalityrate) values (%s,%s)"
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid
 def getAll(self):
        cursor = self.db.cursor()
        sql="select * from countriestable2"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
 def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from countriestable2 where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return result
def update(self, values):
        cursor = self.db.cursor()
        sql="update countriestable2 set countryname= %s, equalityrate=%s where id = %s"
        cursor.execute(sql, values)
        self.db.commit()
def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from countriestable2 where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.db.commit()
        print("delete done")
CountriesDAO = CountriesDAO()