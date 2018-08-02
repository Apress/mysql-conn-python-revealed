import mysql.connector
from mysql.connector.conversion import MySQLConverter
from datetime import datetime
from time import sleep

# Format strings
FMT_QUERY = "Query {0} - {1}:\n" + "-"*19
FMT_HEADER = "{0:18s}   {1:7s}   {2:3s}"
FMT_ROW = "{0:18s}   {1:^7s}   {2:4.1f}"

# Create connection to MySQL
db = mysql.connector.connect(
  option_files="my.ini", use_pure=True)

# Prepare the converter
converter = MySQLConverter(db.charset, True)

# Define the queries
sql1 = """
SELECT Name, CountryCode, Population
  FROM world.city
 WHERE CountryCode = 'USA'
 ORDER BY Population DESC
 LIMIT 3"""
sql2 = "DO SLEEP(3)"
sql3 = """
SELECT Name, CountryCode, Population
  FROM world.city
 WHERE CountryCode = 'IND'
 ORDER BY Population DESC
 LIMIT 3"""
queries = [sql1, sql2, sql3]

# Execute the queries and obtain the
# iterator
results = db.cmd_query_iter(";".join(queries))

# Iterate through the results
count = 0
for result in results:
  count = count + 1;
  time = datetime.now().strftime('%H:%M:%S')
  print(FMT_QUERY.format(count, time))
  if ('columns' in result):
    # It is one of the SELECT statements
    # as it has column definitions.
    # Print the result.
    print(FMT_HEADER.format(
      "City", "Country", "Pop"))
    (city, eof) = db.get_row()
    while (not eof):
      values = converter.row_to_python(
        city, result["columns"])
      print(FMT_ROW.format(
        values[0],
        values[1],
        values[2]/1000000.0
      ))
      (city, eof) = db.get_row()
  else:
    # Not a SELECT statement
    print("No result to print")

  sleep(2)
  print("")

db.close()
