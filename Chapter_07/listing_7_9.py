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
statement = city_col.find("Name = :city_name")
statement.fields(
  "_id",
  "Suburbs",
  "JSON_SEARCH("
     + "Suburbs,"
     + " 'one',"
     + " 'Central Business District')"
  + " AS Index")
statement.bind("city_name", "Sydney")

before = statement.execute().fetch_one()
print("Suburbs before the changes:")
print("-"*27)
printer.pprint(before["Suburbs"])
print("")

docid = before["_id"]
# The returned index includes $ to
# signify the start of the path, but
# that is relative to Suburbs, so
# remove for this use.
index = before["Index"][1:]
print("Index = '{0}'\n"
  .format(before["Index"]))

# Use array_append() to change the
# Central Busines District suburb into
# an array of itself plus an array of
# some places within the suburb.
modify = city_col.modify("_id = :id")
modify.array_append(
  "Suburbs{0}".format(index),
  ["Circular Quay", "Town Hall"])
modify.bind("id", docid)
modify.execute()

after1 = statement.execute().fetch_one()
print("Suburbs after the array_append:")
print("-"*31)
printer.pprint(after1["Suburbs"])
print("")

# Reset the data
db.rollback()

# Use array_insert to add the suburb
# Liverpool
db.start_transaction()
num_suburbs = len(before["Suburbs"])
modify = city_col.modify("_id = :id")
modify.array_insert(
  "Suburbs[{0}]".format(num_suburbs),
  "Liverpool")
modify.bind("id", docid)
modify.execute()

after2 = statement.execute().fetch_one()
print("Suburbs after the array_insert:")
print("-"*31)
printer.pprint(after2["Suburbs"])

# Reset the data
db.rollback()
db.close()
