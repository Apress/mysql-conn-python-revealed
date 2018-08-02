import mysql.connector
from mysql.connector import errorcode
from mysql.connector import errors

def connect():
  """Connect to MySQL Server and return
  the connection object."""
  primary_args = {
    "host": "127.0.0.1",
    "port": 3306,
  }
  failover_args = {
    "host": "127.0.0.1",
    "port": 3307,
  }
  db = mysql.connector.connect(
    option_files="my.ini",
    use_pure=True,
    failover=(
      primary_args,
      failover_args,
    )
  )

  return db

def execute(db, wait_for_failure=False):
  """Execute the query and print
  the result."""
  sql = """
SELECT @@global.hostname AS Hostname,
       @@global.port AS Port"""
  
  retry = False
  try:
    cursor = db.cursor(named_tuple=True)
  except errors.OperationalError as err:
    print("Failed to create the cursor."
      + " Error:\n{0}\n".format(err))
    retry = True
  else:
    if (wait_for_failure):
      try:
        input("Shut down primary now to"
          + " fail when executing query."
          + "\nHit Enter to continue.")
      except SyntaxError:
        pass
      print("")

    try:
      cursor.execute(sql)
    except errors.InterfaceError as err:
      print("Failed to execute query"
        + " (InterfaceError)."
        + " Error:\n{0}\n".format(err))
      retry = (err.errno == errorcode.CR_SERVER_LOST)
    except errors.OperationalError as err:
      print("Failed to execute query"
        + " (OperationalError)."
        + " Error:\n{0}\n".format(err))
      retry = (err.errno == errorcode.CR_SERVER_LOST_EXTENDED)
    else:
      print("Result of query:")
      print(cursor.fetchall())
    finally:
      cursor.close()

  return retry

# Execute for the first time This should
# be against the primary instance
db = connect()
retry = True
while retry:
  retry = execute(db)
  if retry:
    # Reconnect
    db = connect()
print("")

# Wait for the primary instance to
# shut down.
try:
  input("Shut down primary now to fail"
      + " when creating cursor."
      + "\nHit Enter to continue.")
except SyntaxError:
  pass
print("")

# Attempt to execute again
retry = True
allow_failure = True
while retry:
  retry = execute(db, allow_failure)
  allow_failure = False
  if retry:
    # Reconnect
    db = connect()

db.close()
