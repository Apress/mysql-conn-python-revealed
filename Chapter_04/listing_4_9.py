import mysql.connector

FMT_HEADER = "{0:2s}   {1:30s}   {2:8s}"
FMT_ROW = "{0:2d}   {1:30s}   ({2:8s})"

# Create connection to MySQL
db = mysql.connector.connect(
  option_files="my.ini",
  allow_local_infile=True
)
cursor = db.cursor(dictionary=True)

# Clear the table of any existing rows
cursor.execute("DELETE FROM world.loadtest")

# Define the statement and execute it.
sql = """
LOAD DATA LOCAL INFILE 'testdata.txt'
     INTO TABLE world.loadtest
CHARACTER SET utf8mb4
   FIELDS TERMINATED BY ','
          OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
   IGNORE 1 LINES"""
cursor.execute(sql)

print(
  "Number of rows inserted: {0}".format(
  cursor.rowcount
))
print("")

sql = """
SELECT id, val, LEFT(HEX(val), 8) AS hex
  FROM world.loadtest
 ORDER BY id"""
cursor.execute(sql)

if (cursor.with_rows):
  # Print the rows found
  print(
    FMT_HEADER.format(
      "ID", "Value", "Hex"
    )
  )
  row = cursor.fetchone()
  while (row):
    print(
      FMT_ROW.format(
        row["id"],
        row["val"],
        row["hex"]
      )
    )
    row = cursor.fetchone()

# Commit the transaction
db.commit()
cursor.close()
db.close()
