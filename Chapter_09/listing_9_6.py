import mysql.connector
from mysql.connector import errors
from mysql.connector.errorcode import *

db = mysql.connector.connect(
  option_files="my.ini")

cursor = db.cursor()
try:
  cursor.execute("SELECT * FROM city")
except errors.ProgrammingError as e:
  print("Msg .........: {0}"
    .format(e.msg))
  print("Errno .......: {0}"
    .format(e.errno))
  print("SQL State ...: {0}"
    .format(e.sqlstate))
  print("")
  if e.errno == ER_NO_DB_ERROR:
    print("Errno is ER_NO_DB_ERROR")

db.close()
