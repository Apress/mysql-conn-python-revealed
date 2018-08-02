import mysqlx
from config import connect_args
import pprint

printer = pprint.PrettyPrinter(indent=1)

db = mysqlx.get_session(**connect_args)
schema = db.get_schema("py_test_db")
city_col = schema.get_collection("city")

# Run inside a transaction, so the
# changes can be rolled back at the end.
db.start_transaction()

# Get the current suburbs, the document
# id, and the index of Central Business
# District in the Suburbs array.
statement = city_col.find(
  "Name = :city_name")
statement.bind("city_name", "Adelaide")
before = statement.execute().fetch_one()
print("Adelaide before patching:")
print("-"*25)
printer.pprint(dict(before))
print("")

docid = before["_id"]

# Make the following changes:
#  * Increase the area to 3400
#  * Increase the population to 1500000
#  * Remove the median weekly individual
#    income.
doc = {
  "Geography": {
    "Area": 3400
  },
  "Demographics": {
    "Population": 1500000,
    "Median weekly individual income": None
  }
}
modify = city_col.modify("_id = :id")
modify.patch(doc)
modify.bind("id", docid)
modify.execute()

after = statement.execute().fetch_one()
print("Adelaide after patching:")
print("-"*24)
printer.pprint(dict(after))

# Reset the data
db.rollback()
db.close()
