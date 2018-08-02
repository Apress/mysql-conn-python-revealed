import mysql.connector
import mysqlx
from config import connect_args

# Execute a query using the traditional
# API
db_trad = mysql.connector.connect(
  option_files="my.ini")
cursor = db_trad.cursor()

sql = """SELECT *
           FROM world.city
          WHERE ID = %(id)s"""
params = {'id': 130}
cursor.execute(sql, params=params)

for row in cursor.fetchall():
  print(row)

db_trad.close()

# Execute a query using the X DevAPI
dbx = mysqlx.get_session(**connect_args)
world = dbx.get_schema("world")

city = world.get_table("city")
city_stmt = city.select()
city_stmt.where("ID = :city_id")
city_stmt.bind("city_id", 131)
res = city_stmt.execute()
for row in res.fetch_all():
  print("({0}, '{1}', '{2}', '{3}', {4})"
    .format(
       row[0], row[1],
       row[2],row[3],row[4]
  ))

dbx.close()
