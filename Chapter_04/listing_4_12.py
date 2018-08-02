import mysql.connector
from mysql.connector import errors

# Create connection to MySQL
db = mysql.connector.connect(
  option_files="my.ini",
  consume_results=True
)

# First query the city table without
# a default database
try:
  result = db.cmd_query(
    """SELECT *
         FROM city
        WHERE id = 130"""
  )
except errors.ProgrammingError as err:
  print(
    "1: Failed to execute query with "
    + "the error:\n   {0}".format(err)
  )
else:
  print("1: Query executed successfully")


# Then query the city table with
# a default database
db.database = "world"
try:
  result = db.cmd_query(
    """SELECT *
         FROM city
        WHERE id = 130"""
  )
except errors.ProgrammingError as err:
  print(
    "2: Failed to execute query with "
    + "the error:\n   {0}".format(err)
  )
else:
  print("2: Query executed successfully")

db.close()
