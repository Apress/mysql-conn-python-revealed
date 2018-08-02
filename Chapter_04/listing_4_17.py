import _mysql_connector

# Create connection to MySQL
connect_args = {
  "host": "127.0.0.1",
  "port": 3306,
  "user": "pyuser",
  "password": "Py@pp4Demo",
};

db = _mysql_connector.MySQL()
db.connect(**connect_args)
charset_mysql = "utf8mb4"
charset_python = "utf-8"
db.set_character_set(charset_mysql)

# Execute the query
db.query(
  """SELECT Name, CountryCode,
            Population
       FROM world.city
      WHERE Population > 9000000
      ORDER BY Population DESC"""
)

print(__file__ + " - Using _mysql_connector:")
print("")
if (db.have_result_set):
  # Print the rows found
  print(
    "{0:15s}   {1:7s}   {2:3s}".format(
      "City", "Country", "Pop"
    )
  )
  city = db.fetch_row()
  while (city):
    print(
      "{0:15s}   {1:^7s}   {2:4.1f}".format(
        city[0].decode(charset_python),
        city[1].decode(charset_python),
        city[2]/1000000.0
      )
    )
    city = db.fetch_row()

db.free_result()
db.close()
