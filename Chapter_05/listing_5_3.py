from mysql.connector import pooling

pool = pooling.MySQLConnectionPool(
  option_files="my.ini",
  pool_name="test",
)

db = pool.get_connection()

cursor = db.cursor(named_tuple=True)
cursor.execute("""
SELECT Name, CountryCode, Population
  FROM world.city
 WHERE CountryCode = %s""", ("AUS",))

if (cursor.with_rows):
  # Print the rows found
  print(
    "{0:15s}   {1:7s}   {2:10s}".format(
      "City", "Country", "Population"
    )
  )
  city = cursor.fetchone()
  while (city):
    print(
      "{0:15s}   {1:^7s}    {2:8d}".format(
        city.Name,
        city.CountryCode,
        city.Population
      )
    )
    city = cursor.fetchone()

cursor.close()
db.close()
