import mysqlx
from config import connect_args

db = mysqlx.get_session(**connect_args)
schema = db.get_schema("py_test_db")
city_col = schema.get_collection("city")

# Get the current document for Geelong
db.start_transaction()
result = city_col.find("Name = :city_name") \
  .bind("city_name", "Geelong") \
  .lock_exclusive() \
  .execute()
geelong = result.fetch_one()

# Get the Geelong document ID and
# update the population
geeling_id = geelong["_id"]
geelong["Demographics"]["Population"] = 193000

# Upsert the document
result = city_col.add_or_replace_one(
  geeling_id, geelong)

print("Number of affected docs: {0}"
  .format(result.get_affected_items_count()))

# Attempt to use the same document
# to change a non-existing ID
result = city_col.replace_one(
  "No such ID", geelong)

print("Number of affected docs: {0}"
  .format(result.get_affected_items_count()))

# Leave the data in the same state as
# before the changes
db.rollback()
db.close()
