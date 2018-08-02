import mysql.connector

def print_warnings(warnings):
  for warning in warnings:
    print("Level  : {0}".format(
      warning[0]))
    print("Errno  : {0}".format(
      warning[1]))
    print("Message: {0}".format(
      warning[2]))

print("Using cursors\n")

db = mysql.connector.connect(
  option_files="my.ini")

cursor = db.cursor()

# Ensure the DDL statement will cause
# a warnings by executing the same
# CREATE SCHEMA IF NOT EXISTS statement
# twice.
cursor.execute(
  "CREATE SCHEMA IF NOT EXISTS py_test_db")

# Enable retriaval of warnings
db.get_warnings = True

# For a DDL statement
cursor.execute(
  "CREATE SCHEMA IF NOT EXISTS py_test_db")

# Get the warnings
warnings = cursor.fetchwarnings()

print("Warnings for CREATE SCHEMA:")
print("---------------------------")
print("DDL: Number of warnings: {0}"
  .format(len(warnings)))
print_warnings(warnings)
print("")

# Try a SELECT statement
cursor.execute("SELECT 1/0")
rows = cursor.fetchall()

# Get the warnings
warnings = cursor.fetchwarnings()

print("Warnings for SELECT:")
print("--------------------")
print("SELECT: Number of warnings: {0}"
  .format(len(warnings)))
print_warnings(warnings)

db.close()
