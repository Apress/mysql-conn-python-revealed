import mysql.connector
import datetime

# Create connection to MySQL
db = mysql.connector.connect(
  option_files="my.ini")

# Instantiate the cursor
cursor = db.cursor()

# Create a temporary table
sql = """
CREATE TEMPORARY TABLE world.tmp_person (
  Name varchar(50) NOT NULL,
  Birthday date NOT NULL,
  PRIMARY KEY (Name)
)"""
cursor.execute(sql)

sql = """
INSERT INTO world.tmp_person
VALUES (%s, %s)
"""
params = (
  "John Doe",
  datetime.date(1970, 10, 31)
)
cursor.execute(sql,params=params)

print("Statement:\n{0}".format(
  cursor.statement))

cursor.close()
db.close()
