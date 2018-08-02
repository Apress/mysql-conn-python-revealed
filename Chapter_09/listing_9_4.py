import mysqlx
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
print("Warnings for CREATE SCHEMA:")
print("---------------------------")
print("DDL: Number of warnings: {0}"
  .format(result.get_warnings_count()))
print(result.get_warnings())
print("")

# Try a SELECT statement
sql = db.sql("SELECT 1/0")
result = sql.execute()
row = result.fetch_all()

# Get the warnings
print("Warnings for SELECT:")
print("--------------------")
print("SELECT: Number of warnings: {0}"
  .format(result.get_warnings_count()))
print(result.get_warnings())

db.close()
