import mysql.connector
from datetime import datetime

# Create connection to MySQL
db = mysql.connector.connect(
  option_files="my.ini", use_pure=True)
cursor = db.cursor(named_tuple=True)

# Create a temporary table for this
# example
cursor.execute("""
  CREATE TEMPORARY TABLE world.t1 (
    id int unsigned NOT NULL,
    val_datetime datetime,
    val_timestamp timestamp,
    PRIMARY KEY (id)
  )""")

# Set the time zone to UTC
db.time_zone = "+00:00"

# Insert a date and time value:
#    2018-05-06 21:10:12
#    (May 6th 2018 09:10:12pm)
time = datetime(2018, 5, 6, 21, 10, 12)

# Definte the query template and the
# parameters to submit with it.
sql = """
INSERT INTO world.t1
VALUES (%s, %s, %s)"""

params = (1, time, time)

# Insert the row
cursor.execute(sql, params)

# Define output formats
# and print output header
fmt = "{0:9s}   {1:^19s}   {2:^19s}"
print(fmt.format(
  "Time Zone", "Datetime", "Timestamp"))
print("-"*53)

# Retrieve the values using thee
# different time zones
sql = """
SELECT val_datetime, val_timestamp
  FROM world.t1
 WHERE id = 1"""

for tz in ("+00:00", "-05:00", "+10:00"):
  db.time_zone = tz
  cursor.execute(sql)
  row = cursor.fetchone()
  print(fmt.format(
    "UTC" + ("" if tz == "+00:00" else tz),
    row.val_datetime.isoformat(" "),
    row.val_timestamp.isoformat(" ")
  ))

# Use the CONVERT_TZ() function to
# convert the time zone of the datetime
# value
sql = """
SELECT CONVERT_TZ(
         val_datetime,
         '+00:00',
         '+10:00'
       ) val_utc
  FROM world.t1
 WHERE id = 1"""
cursor.execute(sql)
row = cursor.fetchone()
print("\ndatetime in UTC+10:00: {0}".format(
  row.val_utc.isoformat(" ")))

cursor.close()
db.close()
