import mysql.connector
from mysql.connector.constants import ClientFlag

connect_args = {
  "host": "127.0.0.1",
  "port": 3306,
  "user": "pyuser",
  "password": "Py@pp4Demo",
  "client_flags": [
    ClientFlag.INTERACTIVE,
    -ClientFlag.CAN_HANDLE_EXPIRED_PASSWORDS
  ]
};

db = mysql.connector.connect(
  **connect_args
)

print(__file__ + " - Client flags:")
print(
  "MySQL connection ID for db: {0}"
  .format(db.connection_id)
)

db.close()
