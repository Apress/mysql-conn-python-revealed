import mysql.connector
import pprint

printer = pprint.PrettyPrinter(indent=1)

# Create connection to MySQL
db = mysql.connector.connect(
  option_files="my.ini")

# Execute a query
result = db.cmd_query(
  """SELECT *
       FROM world.city
      WHERE ID = 130"""
)

# Print the result dictionary
print("Result Dictionary\n" + "="*17)
printer.pprint(result)

db.close()
