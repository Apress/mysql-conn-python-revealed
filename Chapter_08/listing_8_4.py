import mysqlx
from config import connect_args

fmt = "{0:22s}: {1:4d}"

db = mysqlx.get_session(**connect_args)

# Get the world.city table
schema = db.get_schema("world")
city = schema.get_table("city")

db.start_transaction()

# Check the number of rows before
# deleting rows.
print(fmt.format(
  "Number of rows before",
  city.count()
))

# Define the update
delete = city.delete()
delete.where("Population < :min_pop")
delete.bind("min_pop", 1000)
result = delete.execute()

print(fmt.format(
  "Number of rows deleted",
  result.get_affected_items_count()
))

# Check the affect
print(fmt.format(
  "Number of rows after",
  city.count()
))

# Reset the data
db.rollback()
db.close()
