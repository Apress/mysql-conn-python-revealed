import mysql.connector
import pprint

printer = pprint.PrettyPrinter(indent=1)

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
result_set = db.get_rows()

# Print the result dictionary
print("Result Dictionary\n" + "="*17)
printer.pprint(result)

# Print the rows
print("\nResult Set\n" + "="*10)
printer.pprint(result_set)

db.close()
