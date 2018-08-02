import mysql.connector

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

# Print the rows found
print(__file__ + " – Using decode:")
print("")
print(
  "{0:15s}   {1:7s}   {2:3s}".format(
    "City", "Country", "Pop"
  )
)
for city in cities:
  print(
    "{0:15s}   {1:^7s}   {2:4.1f}".format(
      city[0].decode(db.python_charset),
      city[1].decode(db.python_charset),
      int(
        city[2].decode(db.python_charset)
      )/1000000.0
    )
  )

# Print the eof package
print("\nEnd-of-file:");
for key in eof:
  print("{0:15s} = {1:2d}".format(
    key, eof[key]
  ))

db.close()
