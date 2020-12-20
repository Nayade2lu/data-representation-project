import mysql.connector
import configcountries as cfg

db = mysql.connector.connect(
  host=cfg.mysql['host'],
  user=cfg.mysql['username'],
  password=cfg.mysql['password'],
  database=cfg.mysql['database']
)

cursor = db.cursor()
sql="select * from countriestable2"


cursor.execute(sql)
result = cursor.fetchall()
for x in result:
  print(x)