import mysql.connector
from mysql.connector import FieldType

# Create connection to MySQL
db = mysql.connector.connect(
  option_files="my.ini")
cursor = db.cursor()

# Create a test table
cursor.execute(
  """CREATE TEMPORARY TABLE world.t1 (
    id int unsigned NOT NULL PRIMARY KEY,
    val1 tinyint,
    val2 bigint,
    val3 decimal(10,3),
    val4 text,
    val5 varchar(10),
    val6 char(10)
  )"""
)

# Select all columns (no rows returned)
cursor.execute("SELECT * FROM world.t1")

# Print the field type for each column
print("{0:6s}   {1}".format(
  "Column", "Field Type"))
print("=" * 25);
for column in cursor.description:
  print("{0:6s}   {1:3d} - {2}".format(
    column[0],
    column[1],
    FieldType.get_info(column[1])
  ))

# Consume the (non-existing) rows
cursor.fetchall()

cursor.close
db.close()
