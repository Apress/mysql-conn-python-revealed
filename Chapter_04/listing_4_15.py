def get_column_flags(column_info):
  """Returns a dictionary with a
  dictionary for each flag set for a 
  column. The dictionary key is the
  flag name. The flag name, the flag
  numeric value and the description of
  the flag is included in the flag
  dictionary.
  """
  from mysql.connector import FieldFlag

  flags = {}
  desc = FieldFlag.desc
  for name in FieldFlag.desc:
    (value, description) = desc[name]
    if (column_info[7] & value):
      flags[name] = {
        "name": name,
        "value": value,
        "description": description
      }

  return flags

# Main program
import mysql.connector

# Create connection to MySQL
db = mysql.connector.connect(
  option_files="my.ini")
cursor = db.cursor()

# Create a test table
cursor.execute("""
CREATE TEMPORARY TABLE world.t1 (
  id int unsigned NOT NULL auto_increment,
  val1 bigint,
  val2 varchar(10),
  val3 varchar(10) NOT NULL,
  val4 varchar(10),
  val5 varchar(10),
  PRIMARY KEY(id),
  UNIQUE KEY (val1),
  INDEX (val2),
  INDEX (val3, val4)
)"""
)

# Select all columns (no rows returned)
cursor.execute("SELECT * FROM world.t1")

# Print the field type for each column
print("{0:6s}   {1}".format(
  "Column", "Field Flags"))
print("=" * 74);
all_flags = {}
for column in cursor.description:
  flags = get_column_flags(column)

  # Add the flags to the list of
  # all flags, so the description
  # can be printed later
  # for flag_name in flags:
  all_flags.update(flags)

  # Print the flag names sorted
  # alphabetically
  print("{0:6s}   {1}".format(
    column[0],
    ", ".join(sorted(flags))
  ))

print("")

# Print description of the flags that
# were found
print("{0:18s}   {1}".format(
  "Flag Name", "Description"))
print("=" * 53);
for flag_name in sorted(all_flags):
  print("{0:18s}   {1}".format(
    flag_name,
    all_flags[flag_name]["description"]
  ))

# Consume the (non-existing) rows
cursor.fetchall()

cursor.close
db.close()
