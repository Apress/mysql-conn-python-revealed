import mysqlx
from config import connect_args

db = mysqlx.get_session(**connect_args)

# Reinitialize employees collection in
# the py_test_db schema
schema = db.get_schema("py_test_db")
employees = schema.get_collection(
  "employees")

# Drop the index on the Name field.
employees.drop_index("employee_name")
print("Index employee_name has been dropped")

db.close()
