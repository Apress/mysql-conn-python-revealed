import mysql.connector

db = mysql.connector.connect(
  option_files="my.ini")

print(__file__ + " - single config file:")
print(
  "MySQL connection ID for db: {0}"
  .format(db.connection_id)
)

db.close()
