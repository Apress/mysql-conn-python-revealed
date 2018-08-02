import mysql.connector

db = mysql.connector.connect(
  option_files = [
    "my_shared.ini",
    "my_app_specific.ini"
  ],
  option_groups = [
    "client",
    "connector_python"
  ]
)

print(__file__ + " - two config files:")
print(
  "MySQL connection ID for db: {0}"
  .format(db.connection_id)
)

db.close()
