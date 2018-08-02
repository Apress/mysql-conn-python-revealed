import mysql.connector

# Create connection to MySQL
db = mysql.connector.connect(
  option_files="my.ini", autocommit=True)
cursor = db.cursor()

queries = [
  """UPDATE world.city
        SET Population = Population + 1
      WHERE ID = 130""",
  """UPDATE world.country
        SET Population = Population + 1
      WHERE Code = 'AUS'""",
]

db.start_transaction()
tests = cursor.execute(
  ";".join(queries), multi=True)
for test in tests:
  # Do something or pass if no action
  # is required.
  pass
db.rollback();

cursor.close()
db.close()
