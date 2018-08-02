import mysql.connector
from mysql.connector import errors
from mysql.connector.errorcode \
  import ER_NO_DB_ERROR

# Define the custom exception class
class MyError(errors.Error):
  def __init__(
    self, msg=None, errno=None,
    values=None, sqlstate=None):

    import sys
    super(MyError, self).__init__(
      msg, errno, values, sqlstate)
    print("MyError: {0} ({1}): {2}"
      .format(self.errno,
              self.sqlstate,
              self.msg
      ), file=sys.stderr)

# Register the class
errors.custom_error_exception(
  ER_NO_DB_ERROR,
  MyError
)

# Now cause the exception to be raised
db = mysql.connector.connect(
  option_files="my.ini")

cursor = db.cursor()
try:
  cursor.execute("SELECT * FROM city")
except MyError as e:
  print("Msg .........: {0}"
    .format(e.msg))
  print("Errno .......: {0}"
    .format(e.errno))
  print("SQL State ...: {0}"
    .format(e.sqlstate))

db.close()
