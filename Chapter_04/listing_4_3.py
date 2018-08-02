import mysql.connector

# Create connection to MySQL
db = mysql.connector.connect(
  option_files="my.ini", use_pure=True)
cursor = db.cursor()

# Definte the query template and the
# parameters to submit with it.
sql = """
UPDATE world.city
   SET Population = %(population)s
 WHERE Name = %(name)s
       AND CountryCode = %(country)s
       AND District = %(district)s"""

params = (
  {
    "name": "Dimitrovgrad",
    "country": "RUS",
    "district": "Uljanovsk",
    "population": 150000
  },
  {
    "name": "Lower Hutt",
    "country": "NZL",
    "district": "Wellington",
    "population": 100000
  },
  {
    "name": "Wuhan",
    "country": "CHN",
    "district": "Hubei",
    "population": 5000000
  },
)

# Get the previous number of questions
# asked to MySQL by the session
cursor.execute("""
  SELECT VARIABLE_VALUE
    FROM performance_schema.session_status
   WHERE VARIABLE_NAME = 'Questions'""")
tmp = cursor.fetchone()
questions_before = int(tmp[0])

# Execute the queries
cursor.executemany(sql, params)
print("Row count: {0}".format(
  cursor.rowcount))
print("Last statement: {0}".format(
  cursor.statement))

# Get the previous number of questions
# asked to MySQL by the session
cursor.execute("""
  SELECT VARIABLE_VALUE
    FROM performance_schema.session_status
   WHERE VARIABLE_NAME = 'Questions'""")
tmp = cursor.fetchone()
questions_after = int(tmp[0])

print("Difference in number of"
  + " questions: {0}".format(
    questions_after-questions_before
))

db.rollback()
cursor.close()
db.close()
