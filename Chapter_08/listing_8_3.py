import mysqlx
from config import connect_args

db = mysqlx.get_session(**connect_args)

# Get the world.city table
schema = db.get_schema("world")
city = schema.get_table("city")

db.start_transaction()

# Check the population before the update
select = city.select()
select.where(
  "Name = :city"
  + " AND CountryCode = :country"
)
select.bind("city", "Sydney")
select.bind("country", "AUS")
result = select.execute()
sydney = result.fetch_one()
print("Old population: {0}".format(
  sydney["Population"]))

# Define the update
update = city.update()
update.set("Population", 5000000)
update.where(
  "Name = :city"
  + " AND CountryCode = :country")
update.bind("city", "Sydney")
update.bind("country", "AUS")
result = update.execute()

print("Number of rows updated: {0}"
  .format(
    result.get_affected_items_count())
)

# Check the affect
result = select.execute()
sydney = result.fetch_one()
print("New population: {0}".format(
  sydney["Population"]))

# Reset the data
db.rollback()
db.close()
