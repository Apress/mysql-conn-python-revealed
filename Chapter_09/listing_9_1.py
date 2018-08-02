import mysql.connector

def print_warnings(warnings):
  if mysql.connector.__version_info__[0:3] > (8, 0, 11):
    (warnings, eof) = warnings

  for warning in warnings:
    print("Level  : {0}".format(
      warning[0]))
    print("Errno  : {0}".format(
      warning[1]))
    print("Message: {0}".format(
      warning[2]))

db = mysql.connector.connect(
  option_files="my.ini", use_pure=False)

# This example only works with the C
# Extension installed. Exit if that is
# not the case.
is_cext = isinstance(
  db,
  mysql.connector.connection_cext.CMySQLConnection
)
if not is_cext:
  print("The example requires the C "
    + "Extension implementation to be "
    + "installed")
  exit()

print("Using the C Extension implementation\n")

# Ensure the DDL statement will cause
# a warnings by executing the same
# CREATE SCHEMA IF NOT EXISTS statement
# twice.
db.cmd_query(
  "CREATE SCHEMA IF NOT EXISTS py_test_db")

# For a DDL statement
result = db.cmd_query(
  "CREATE SCHEMA IF NOT EXISTS py_test_db")

print("Warnings for CREATE SCHEMA:")
print("---------------------------")
print("DDL: Number of warnings: {0}"
  .format(result["warning_count"]))

# Get the warnings
db.cmd_query("SHOW WARNINGS")
warnings = db.get_rows()
print_warnings(warnings)
db.free_result()
print("")

# Try a SELECT statement
result = db.cmd_query("SELECT 1/0")
rows = db.get_rows()
db.free_result()

print("Warnings for SELECT:")
print("--------------------")
print("SELECT: Number of warnings: {0}"
  .format(db.warning_count))

# Get the warnings
db.cmd_query("SHOW WARNINGS")
warnings = db.get_rows()
print_warnings(warnings)

db.close()
