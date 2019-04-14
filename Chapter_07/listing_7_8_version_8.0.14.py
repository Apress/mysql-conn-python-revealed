import mysqlx
from config import connect_args

db = mysqlx.get_session(**connect_args)
schema = db.get_schema("py_test_db")
city_col = schema.get_collection("city")

db.start_transaction()

# Get the current population
statement = city_col.find(
  "Geography.State = :state")
statement.fields("Name AS CityName",
  "Demographics.Population AS Population")
statement.sort("Name")
statement.bind("state", "Victoria")

before = statement.execute()

# Update the population for cities
# in the state of Victoria to increase
# the population with 10%
expr = mysqlx.expr("FLOOR(Demographics.Population * 1.10)")
result = city_col.modify(
  "Geography.State = :state") \
  .set("Demographics.Population", expr) \
  .bind("state", "Victoria") \
  .execute()

print("Number of affected docs: {0}"
  .format(result.get_affected_items_count()))
print("")

after = statement.execute()

before_cities = before.fetch_all()
after_cities  = after.fetch_all()

print("{0:10s}   {1:^17s}"
  .format("City", "Population"))
print("{0:10s}   {1:7s}   {2:7s}"
  .format("", "Before", "After"))
print("-"*30)

for before_city, after_city \
  in zip(before_cities, after_cities):
  print("{0:10s}   {1:7d}   {2:7d}"
    .format(
      before_city["CityName"],
      int(before_city["Population"]),
      int(after_city["Population"])
    )
  )

# Leave the data in the same state as
# before the changes
db.rollback()
db.close()
