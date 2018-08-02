import mysql.connector

db1 = mysql.connector.connect(
  option_files="my.ini",
  database="world",
  autocommit=False
)
db2 = mysql.connector.connect(
  option_files="my.ini",
  database="world",
)
cursor1 = db1.cursor()
cursor2 = db2.cursor()

sql = """
SELECT Population
  FROM city
 WHERE ID = 130"""

cursor1.execute("""
UPDATE city
   SET Population = 5000000
 WHERE ID = 130""")

cursor1.execute(sql)
row1 = cursor1.fetchone()
print("Connection 1: {0}"
  .format(row1[0]))

cursor2.execute(sql)
row2 = cursor2.fetchone()
print("Connection 2: {0}"
  .format(row2[0]))

db1.close()
db2.close()
