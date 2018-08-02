import mysql.connector
from math import ceil

# The SQL UPDATE statement that will be
# used in cursor2.
SQL_UPDATE = """
  UPDATE world.city
     SET Population = %(new_population)s
   WHERE ID = %(city_id)s"""

# Function to increase the population
# with 10%
def new_population(old_population):
  return int(ceil(old_population * 1.10))


# Create connection to MySQL
db = mysql.connector.connect(
  option_files="my.ini")

# Instantiate the cursors
cursor1 = db.cursor(
  buffered=True, dictionary=True)
cursor2 = db.cursor()

# Execute the query to get the
# Australian cities
cursor1.execute(
  """SELECT ID, Population
       FROM world.city
      WHERE CountryCode = %s""",
  params=("AUS",)
)

city = cursor1.fetchone()
while (city):
  old_pop = city["Population"]
  new_pop = new_population(old_pop)
  print("ID, Old => New: "
    + "{0}, {1} => {2}".format(
    city["ID"], old_pop, new_pop
  ))
  cursor2.execute(
    SQL_UPDATE,
    params={
      "city_id": city["ID"],
      "new_population": new_pop
    }
  )
  print("Statement: {0}".format(
    cursor2.statement))
  city = cursor1.fetchone()

db.rollback()
cursor1.close()
cursor2.close()
db.close()
