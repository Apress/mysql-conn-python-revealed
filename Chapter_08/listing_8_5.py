import mysqlx
from config import connect_args

db = mysqlx.get_session(**connect_args)
sql = db.sql("""
SELECT CONVERT(District USING utf8mb4)
         AS District,
       COUNT(*) AS NumCities
  FROM world.city
 WHERE CountryCode = 'DEU'
       AND Population > 500000
 GROUP BY District
 ORDER BY NumCities DESC, District""")

result = sql.execute()
fmt = "{0:19s}   {1:6d}"
print("{0:19s}   {1:6s}".format(
  "State", "Cities"))
print("-"*28)

row = result.fetch_one()
while row:
  print(fmt.format(
    row["District"],
    row["NumCities"]
  ))
  row = result.fetch_one()

db.close()
