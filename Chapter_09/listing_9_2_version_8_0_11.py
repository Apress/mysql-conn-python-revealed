import mysql.connector

def print_warnings(warnings, charset):
  for warning in warnings:
    print("Level  : {0}".format(
      warning[0].decode(charset)))
    print("Errno  : {0}".format(
      warning[1].decode(charset)))
    print("Message: {0}".format(
      warning[2].decode(charset)))

db = mysql.connector.connect(
  option_files="my.ini", use_pure=True)

print("Using the pure Python implementation\n")

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
(warnings, eof) = db.get_rows()
print_warnings(warnings, db.python_charset)
print("")

# Try a SELECT statement
result = db.cmd_query("SELECT 1/0")
(rows, eof) = db.get_rows()

print("Warnings for SELECT:")
print("--------------------")
print("SELECT: Number of warnings: {0}"
  .format(eof["warning_count"]))

# Get the warnings
db.cmd_query("SHOW WARNINGS")
(warnings, eof) = db.get_rows()
print_warnings(warnings, db.python_charset)

db.close()
