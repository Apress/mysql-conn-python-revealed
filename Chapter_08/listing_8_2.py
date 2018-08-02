import mysqlx
from config import connect_args

db = mysqlx.get_session(**connect_args)

# Get the world.city table
schema = db.get_schema("world")
city = schema.get_table("city")

db.start_transaction()

statement = city.select(
  "District",
  "COUNT(*) AS NumCities",
  "MAX(Population) AS LargestCityPop")
statement.where(
  "CountryCode = :country"
  + " AND Population > :min_pop")
statement.group_by("District")
statement.order_by(
  "NumCities DESC",
  "LargestCityPop DESC")
statement.bind("country", "USA")
statement.bind("min_pop", 1000000)

print("SQL statement:\n{0}"
  .format(statement.get_sql()))

result = statement.execute()
print("Number of rows in result: {0}\n"
  .format(result.count))

fmt = "{0:12s}   {1:6d}   {2:12d}"
print("{0:12s}   {1:6s}   {2:12s}"
  .format(
    "State",
    "Cities",
    "Largest City"
))
print("-"*37)
for row in result.fetch_all():
  print(fmt.format(
    row["District"],
    row["NumCities"],
    row["LargestCityPop"]
  ))

print("")
print("Number of rows in result: {0}\n"
  .format(result.count))

db.commit()
db.close()
