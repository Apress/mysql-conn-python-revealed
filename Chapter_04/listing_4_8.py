import mysql.connector

# Format strings
FMT_QUERY = "Query {0}:\n" + "-"*8
FMT_HEADER = "{0:18s}   {1:3s}"
FMT_ROW = "{0:18s}   {1:4.1f}"

# Create connection to MySQL
db = mysql.connector.connect(
  option_files="my.ini")
cursor = db.cursor()

# Execute the procedure
return_args = cursor.callproc(
  "world.min_max_cities",
  ("AUS", 500000, None)
)

# Print the returned arguments
print("""Country ..........: {0}
Min Population ...: {1:8d}
Max Population ...: {2:8d}
""".format(*return_args))

# Iterate over the result sets and print
# the cities and their population
# Convert the rows to dictionaries to
# avoid referencing the columns by
# ordinal position.
count = 0
for result in cursor.stored_results():
  count = count + 1;
  print(FMT_QUERY.format(count))
  if (result.with_rows):
    # It is one of the SELECT statements
    # as it has column definitions.
    # Print the result.
    print(FMT_HEADER.format("City", "Pop"))
    city = result.fetchone()
    while (city):
      city_dict = dict(
        zip(result.column_names, city))

      print(FMT_ROW.format(
        city_dict["Name"],
        city_dict["Population"]/1000000
      ))
      city = result.fetchone()
  print("")

cursor.close()
db.close()
