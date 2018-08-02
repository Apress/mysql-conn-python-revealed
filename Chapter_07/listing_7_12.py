import mysqlx
from config import connect_args

db = mysqlx.get_session(**connect_args)
schema = db.get_schema("py_test_db")
city_col = schema.get_collection("city")

# For printing information along the way
fmt = "{0:36s}: {1:2d}"

# Run inside a transaction, so the
# changes can be rolled back at the end.
db.start_transaction()

# Get the document ID for Canberra.
statement = city_col.find("Name = :city_name")
statement.fields("_id")
statement.bind("city_name", "Canberra")

result = statement.execute()
canberra_id = result.fetch_one()["_id"]

# Number of rows in the collection
# before removing any documents
print(fmt.format(
  "Initial number of documents",
  city_col.count()
))
print("")

result = city_col.remove_one(
  canberra_id)

items = result.get_affected_items_count()
print(fmt.format(
  "Number of rows deleted by remove_one",
  result.get_affected_items_count()
))
print(fmt.format(
  "Number of documents after remove_one",
  city_col.count()
))
print("")

statement = city_col.remove(
  "Geography.Country = :country")
statement.bind("country", "Australia")
result = statement.execute()

print(fmt.format(
  "Number of rows deleted by remove",
  result.get_affected_items_count()
))
print(fmt.format(
  "Number of documents after remove",
  city_col.count()
))

# Reset the data
db.rollback()
db.close()
