import mysql.connector

# Format strings
FMT_QUERY = "Query {0}:\n" + "-"*8
FMT_HEADER = "{0:18s}   {1:7s}   {2:3s}"
FMT_ROW = "{0:18s}   {1:^7s}   {2:4.1f}"

# Define the queries
SQL = """
SELECT Name, CountryCode, Population
  FROM world.city
 WHERE CountryCode = %s
 ORDER BY Population DESC
 LIMIT 3"""


# Create connection to MySQL
db = mysql.connector.connect(
  option_files="my.ini", use_pure=True)

cursor = db.cursor(prepared=True)

# Execute the query finding the top
# three populous cities in the USA and
# India.
count = 0
for country in ("USA", "IND"):
  count = count + 1;
  print(FMT_QUERY.format(count))

  cursor.execute(SQL, (country,))

  if (cursor.with_rows):
    # Print the result.
    print(FMT_HEADER.format(
      "City", "Country", "Pop"))
    city = cursor.fetchone()
    while (city):
      print(FMT_ROW.format(
        city[0],
        city[1],
        city[2]/1000000
      ))
      city = cursor.fetchone()

  print("")

cursor.close()
db.close()
