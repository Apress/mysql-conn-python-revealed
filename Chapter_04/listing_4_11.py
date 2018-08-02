import mysql.connector
import pprint

printer = pprint.PrettyPrinter(indent=1)

# Create two connections to MySQL
db1 = mysql.connector.connect(
  option_files="my.ini",
  autocommit=True
)
db2 = mysql.connector.connect(
  option_files="my.ini",
  autocommit=True
)
cursor1 = db1.cursor(dictionary=True)
cursor2 = db2.cursor(dictionary=True)

# Start a transaction
db1.start_transaction()

# Insert a row
cursor1.execute("""
INSERT INTO world.city
VALUES (DEFAULT, 'Camelot', 'GBR',
        'King Arthur County', 2000)"""
)

print("\nin_transaction = {0}".format(
  db1.in_transaction))

id = cursor1.lastrowid
sql = """SELECT *
           FROM world.city
          WHERE id = {0}""".format(id)
cursor1.execute(sql)
cursor2.execute(sql)

# Fetch and print the rows
print("\nResult Set in Connection 1")
print("="*26)
result_set1 = cursor1.fetchall()
printer.pprint(result_set1)

print("\nResult Set in Connection 2")
print("="*26)
result_set2 = cursor2.fetchall()
printer.pprint(result_set2)

db1.rollback()
cursor1.close()
db1.close()

cursor2.close()
db2.close()
