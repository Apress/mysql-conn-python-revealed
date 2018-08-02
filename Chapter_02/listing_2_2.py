import mysql.connector

initial_args = {
  "host": "127.0.0.1",
  "port": 3306,
  "user": "pyuser",
  "password": "Py@pp4Demo",
};

# Create initial connection
db = mysql.connector.connect(
  **initial_args
)

print(
  "Initial MySQL connection ID ...: {0}"
  .format(db.connection_id)
)

new_args = {
  "host": "<your_IP_goes_here_in_quotes>",
};

db.config(**new_args)
db.reconnect()

print(
  "New MySQL connection ID .......: {0}"
  .format(db.connection_id)
)

db.close()
