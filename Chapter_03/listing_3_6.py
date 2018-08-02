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

# Initialize the converter
converter = MySQLConverter(
  db.charset, True)

# Fetch and print the rows
print(__file__
      + " - Using get_rows with limit:")
print("")
count = 0
(cities, eof) = db.get_rows(4)
while (cities):
  count = count + 1
  print("count = {0}".format(count))

  # Print the rows found in this batch
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
  print("")

  # Read the next batch of rows
  if (eof == None):
    (cities, eof) = db.get_rows(count=4)
  else:
    cities = []

db.close()
