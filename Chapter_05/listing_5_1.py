import mysql.connector
from mysql.connector.errors import PoolError

print(__file__ + " - connect():")
print("")

# Create a pool and return the first
# connection
db1 = mysql.connector.connect(
  option_files="my.ini",
  pool_size=2,
  pool_name="test",
)

# Get a second connection in the same pool
db2 = mysql.connector.connect(
  pool_name="test")

# Attempt to get a third one
try:
  db3 = mysql.connector.connect(
    pool_name="test")
except PoolError as err:
  print("Unable to fetch connection:\n{0}\n"
    .format(err))

# Save the connection id of db1 and
# return it to the pool, then try 
# fetching db3 again.
db1_connection_id = db1.connection_id
db1.close()

db3 = mysql.connector.connect(
  pool_name="test")

print("Connection IDs:\n")
print("db1   db2   db3")
print("-"*15)
print("{0:3d}   {1:3d}   {2:3d}".format(
    db1_connection_id,
    db2.connection_id,
    db3.connection_id
  )
)

db2.close()
db3.close()
