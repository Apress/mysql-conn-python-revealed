import mysql.connector

input = "'Sydney' OR True"

# Create connection to MySQL
db = mysql.connector.connect(
  option_files="my.ini")

# Instantiate the cursor
cursor = db.cursor(dictionary=True)

# Execute the query without parameter
sql = """SELECT *
           FROM world.city
          WHERE Name = {0}""".format(input)
cursor.execute(sql)

cursor.fetchall()
print("1: Statement: {0}".format(
  cursor.statement))
print("1: Row count: {0}\n".format(
  cursor.rowcount))


# Execute the query with parameter
sql = """SELECT *
           FROM world.city
          WHERE Name = %(name)s"""
params = {'name': input}
cursor.execute(
  sql,
  params=params
)

cursor.fetchall()
print("2: Statement: {0}".format(
  cursor.statement))
print("2: Row count: {0}".format(
  cursor.rowcount))

cursor.close()
db.close()
