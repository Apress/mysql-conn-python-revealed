import mysql.connector
from mysql.connector.conversion import MySQLConverter

# Create connection to MySQL
db = mysql.connector.connect(
  option_files="my.ini", use_pure=True)

# Execute a query
result = db.cmd_query(
  """SELECT Name, CountryCode,
            Population
       FROM world.city
      WHERE Population > 9000000
      ORDER BY Population DESC"""
)

# Fetch the rows
(cities, eof) = db.get_rows()

# Initialize the converter
converter = MySQLConverter(
  db.charset, True)

# Print the rows found
print(__file__ + " - Using MySQLConverter:")
print("")
print(
  "{0:15s}   {1:7s}   {2:3s}".format(
    "City", "Country", "Pop"
  )
)
for city in cities:
  values = converter.row_to_python(
    city, result["columns"])
  print(
    "{0:15s}   {1:^7s}   {2:4.1f}".format(
      values[0],
      values[1],
      values[2]/1000000.0
    )
  )

db.close()
