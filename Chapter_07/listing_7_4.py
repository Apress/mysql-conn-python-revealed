import mysqlx
from config import connect_args

db = mysqlx.get_session(**connect_args)
schema = db.create_schema("py_test_db")
city_col = schema.get_collection("city")

# Use the count() method to get the
# total number of cities.
num_cities = city_col.count()
print("Total number of cities: {0}"
  .format(num_cities))
print("")

statement = city_col.find(
  "Geography.Country = :country") \
  .fields("Geography.State AS State",
          "COUNT(*) AS NumCities") \
  .group_by("Geography.State") \
  .having("COUNT(*) > 1") \
  .sort("COUNT(*) DESC") \
  .limit(3)

result = statement.bind(
  "country", "Australia"
).execute()

states = result.fetch_all()
print("Num states in result: {0}"
  .format(result.count))
print("")

print("{0:15s}   {1:8s}"
  .format("State", "# Cities"))
print("-"*26)
for state in states:
  print("{State:15s}       {NumCities:1d}"
    .format(**state))

db.close()
