from mysql.connector import pooling

pool = pooling.MySQLConnectionPool(
  option_files="my.ini",
  pool_name="test",
  pool_size=2,
)

print("{0:18s}: {1:3s}   {2:3s}".format(
  "Stage", "db1", "db2"
))
print("-"*29)
fmt = "{0:18s}: {1:3d}   {2:3d}"
db1 = pool.get_connection()
db2 = pool.get_connection()
print(
  fmt.format(
    "Initially",
    db1.connection_id,
    db2.connection_id
  )
)

# Return one of the connections before
# the reconfiguration
db2.close()

# Reconfigure the connections
pool.set_config(user="pyuser")

# Fetch db2 again
db2 = pool.get_connection()
print(
  fmt.format(
    "After set_config()",
    db1.connection_id,
    db2.connection_id
  )
)

# Return the db1 connection to the pool
# and refetch it.
db1.close()
db1 = pool.get_connection()
print(
  fmt.format(
    "After refetching",
    db1.connection_id,
    db2.connection_id
  )
)

db1.close()
db2.close()
