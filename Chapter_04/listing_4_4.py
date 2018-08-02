import mysql.connector

# Create connection to MySQL
db = mysql.connector.connect(
  option_files="my.ini"
)
cursor = db.cursor()

# Create a temporary table for this
# example
cursor.execute("""
  CREATE TEMPORARY TABLE world.t1 (
    id int unsigned NOT NULL,
    val varchar(10),
    PRIMARY KEY (id)
  )""")

# Definte the query template and the
# parameters to submit with it.
sql = """
INSERT INTO world.t1 VALUES (%s, %s)"""

params = (
  (1, "abc"),
  (2, "def"),
  (3, "ghi")
)

# Get the previous number of questions
# asked to MySQL by the session
cursor.execute("""
  SELECT VARIABLE_VALUE
    FROM performance_schema.session_status
   WHERE VARIABLE_NAME = 'Questions'""")
tmp = cursor.fetchone()
questions_before = int(tmp[0])

# Execute the query
cursor.executemany(sql, params)
print("Row count = {0}".format(
  cursor.rowcount))
print("Last statement: {0}".format(
  cursor.statement
))

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

cursor.close()
db.close()
