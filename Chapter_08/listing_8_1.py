import mysqlx
from config import connect_args

fmt = "{0:28s}: {1:4d}"

db = mysqlx.get_session(**connect_args)

# Get the world.city table
schema = db.get_schema("world")
city = schema.get_table("city")

db.start_transaction()

print(fmt.format(
  "Number of rows before insert",
  city.count()
))

# Define the insert statement
insert = city.insert(
  "Name",
  "CountryCode",
  "District",
  "Population"
)

# Add row using a list
darwin = [
  "Darwin",
  "AUS",
  "Northern Territory",
  145916
]
insert.values(darwin)

# Add row by arguments
insert.values(
  "Sunshine Coast",
  "AUS",
  "Queensland",
  302122
)

# Execute the insert
result = insert.execute()

# Get the auto-increment ID generated
# for the inserted row
print(fmt.format(
  "Number of rows inserted",
  result.get_affected_items_count()))
print(fmt.format(
  "First ID generated",
  result.get_autoincrement_value()))

print(fmt.format(
  "Number of rows after insert",
  city.count()))

# Reset the data
db.rollback()
db.close()
