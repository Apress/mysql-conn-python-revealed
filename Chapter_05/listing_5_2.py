from mysql.connector import pooling
from mysql.connector import errors

print(__file__ + " - MySQLConnectionPool():")
print("")

pool = pooling.MySQLConnectionPool(
  option_files="my.ini",
  pool_name="test",
  pool_size=2,
)

# Fetch the first connection
db1 = pool.get_connection()

# Get a second connection in the same pool
db2 = pool.get_connection()

# Attempt to get a third one
try:
  db3 = pool.get_connection()
except errors.PoolError as err:
  print("Unable to fetch connection:\n{0}\n"
    .format(err))

# Save the connection id of db1 and
# return it to the pool, then try 
# fetching db3 again.
db1_connection_id = db1.connection_id
db1.close()

db3 = pool.get_connection()

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
