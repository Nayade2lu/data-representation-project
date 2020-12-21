import mysql.connector
from mysql.connector import cursor
import config as cfg

class CountryDao:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host=cfg.mysql['host'],
            user=cfg.mysql['username'],
            password=cfg.mysql['password'],
            database=cfg.mysql['database']
    )
        #print ("connection made")

    def create(self, country):
        cursor = self.db.cursor()
        sql = "insert into countriestable2 (id, countryname, continent, equalityrate) values (%s,%s,%s,%s)"
        values = [
            country['id'],
            country['countryname'],
            country['continent'],
            country['equalityrate']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from countriestable2'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

    def findById(self, id):
        cursor = self.db.cursor()
        sql = 'select * from countriestable2 where id = %s'
        values = [ id ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
        

    def update(self, country):
       cursor = self.db.cursor()
       sql = "update countriestable2 set countryname = %s, continent = %s, equalityrate = %s where id = %s"
       values = [
           country['countryname'],
           country['continent'],
           country['equalityrate'],
           country['id']

       ]
       cursor.execute(sql, values)
       self.db.commit()
       return country   

    def delete(self, id):
       cursor = self.db.cursor()
       sql = 'delete from countriestable2 where id = %s'
       values = [id]
       cursor.execute(sql, values)
       
       return {}



    def convertToDict(self, result):
        colnames = ['id','countryname', 'continent', 'equalityrate']
        country = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                country[colName] = value
        return country

CountryDao = CountryDao()