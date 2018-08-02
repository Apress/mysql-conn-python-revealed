import mysql.connector

connect_args = {
  "host": "127.0.0.1",
  "port": 3306,
  "user": "pyuser",
  "password": "Py@pp4Demo",
  "charset": "utf8mb4",
  "collation": "utf8mb4_unicode_ci",
  "use_unicode": True
};

db = mysql.connector.connect(
  **connect_args)

print(__file__ + " - Setting character set:")
print(
  "MySQL connection ID for db: {0}"
  .format(db.connection_id)
)

db.close()
