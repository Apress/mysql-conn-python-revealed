import mysqlx
from config import connect_args

# Create the session
db = mysqlx.get_session(
  schema="py_test_db",
  **connect_args
)

# Retrieve the default schema
# (py_test_db)
py_schema = db.get_default_schema()
print("Schema name: {0} - Exists? {1}"
  .format(
    py_schema.name,
    py_schema.exists_in_database()
  )
)

# If py_test_db does not exist,
# create it
if (not py_schema.exists_in_database()):
  db.create_schema(py_schema.name)

print("Schema name: {0} - Exists? {1}"
  .format(
    py_schema.name,
    py_schema.exists_in_database()
  )
)

# Get the world schema
w_schema = db.get_schema("world")
print("Schema name: {0} - Exists? {1}"
  .format(
    w_schema.name,
    w_schema.exists_in_database()
  )
)

# Get the session object of the world
# schema and see if it is the same as
# the db object.
w_session = w_schema.get_session()
print("db == w_session? {0}".format(
  db == w_session))

# Drop the py_test_db schema.
db.drop_schema(py_schema.name)
print("Schema name: {0} - Exists? {1}"
  .format(
    py_schema.name,
    py_schema.exists_in_database()
  )
)

db.close()
