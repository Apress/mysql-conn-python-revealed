import mysql.connector

# Create connection to MySQL
db = mysql.connector.connect(
  option_files="my.ini")
cursor = db.cursor()

# Initialize the stages (ordered)
stages = [
  "Initial",
  "After CREATE TABLE",
  "After INSERT",
  "After commit()",
  "After SELECT",
]

# Initialize dictionary with one list
# per stage to keep track of whether
# db.in_transaction is True or False
# at each stage.
in_trx = {stage: [] for stage in stages}

for autocommit in [False, True]:
  db.autocommit = autocommit;

  in_trx["Initial"].insert(
    autocommit, db.in_transaction)

  # Create a test table
  cursor.execute("""
CREATE TABLE world.t1 (
  id int unsigned NOT NULL PRIMARY KEY,
  val varchar(10)
)"""
  )

  in_trx["After CREATE TABLE"].insert(
    autocommit, db.in_transaction)

  # Insert a row
  cursor.execute("""
INSERT INTO world.t1
VALUES (1, 'abc')"""
  )

  in_trx["After INSERT"].insert(
    autocommit, db.in_transaction)

  # Commit the transaction
  db.commit()

  in_trx["After commit()"].insert(
    autocommit, db.in_transaction)

  # Select the row
  cursor.execute("SELECT * FROM world.t1")
  cursor.fetchall()

  in_trx["After SELECT"].insert(
    autocommit, db.in_transaction)

  # Commit the transaction
  db.commit()

  # Drop the test table
  cursor.execute("DROP TABLE world.t1")

cursor.close()
db.close()

fmt = "{0:18s}   {1:^8s}   {2:^7s}"
print("{0:18s}   {1:^18s}".format(
  "", "in_transaction"))
print(fmt.format(
  "Stage", "Disabled", "Enabled"))
print("-"*39)
for stage in stages:
  print(fmt.format(
    stage,
    "True" if in_trx[stage][0] else "False",
    "True" if in_trx[stage][1] else "False",
  ))
