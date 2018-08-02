import mysqlx
from mysqlx.errorcode import *
from config import connect_args

db = mysqlx.get_session(**connect_args)

# Ensure the DDL statement will cause
# a warnings by executing the same
# CREATE SCHEMA IF NOT EXISTS statement
# twice.
sql = db.sql(
  "CREATE SCHEMA IF NOT EXISTS py_test_db")
sql.execute()

# For a DDL statement
sql = db.sql(
  "CREATE SCHEMA IF NOT EXISTS py_test_db")
result = sql.execute()

# Get the warnings
for warning in result.get_warnings():
  if warning["code"] == ER_DB_CREATE_EXISTS:
    print("Ignoring the warning")
  else:
    raise mysqlx.errors.DatabaseError(
      warning["msg"], warning["code"])

db.close()
