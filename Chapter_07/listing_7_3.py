import mysqlx
from config import connect_args
from cities import cities

db = mysqlx.get_session(**connect_args)
schema = db.create_schema("py_test_db")

# Reinitalize the city collection
schema.drop_collection("city")
city_col = schema.create_collection("city")

# Insert a single city
sydney = cities.pop("Sydney")
db.start_transaction()
result = city_col.add(sydney).execute()
db.commit()
items = result.get_affected_items_count()
print("1: Number of docs added: {0}"
  .format(items))
ids = result.get_generated_ids()
print("1: Doc IDs added: {0}".format(ids))
print("")

# Insert two cities in one call
melbourne = cities.pop("Melbourne")
brisbane  = cities.pop("Brisbane")
data = (melbourne, brisbane)

db.start_transaction()
result = city_col.add(data).execute()
db.commit()

items = result.get_affected_items_count()
print("2: Number of docs added: {0}"
  .format(items))
ids = result.get_generated_ids()
print("2: Doc IDs added: {0}".format(ids))
print("")

# Insert the rest of the cities by
# adding them to the statement object
# one by one.
db.start_transaction()
statement = city_col.add()
for city_name in cities:
  statement.add(cities[city_name])

result = statement.execute()
db.commit()

items = result.get_affected_items_count()
print("3: Number of docs added: {0}"
  .format(items))
print("")

db.close()
