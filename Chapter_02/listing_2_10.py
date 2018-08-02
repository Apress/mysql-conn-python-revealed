import mysql.connector

db = mysql.connector.MySQLConnection()

# Print banner and initial settings
print(
  "{0:<9s}   {1:<7s}   {2:<18s}".format(
    "Stage", "charset", "collation"
  )
)
print("-" * 40)
print(
  "{0:<9s}   {1:<7s}   {2:<18s}".format(
    "Initial", db.charset, db.collation
  )
)

# Create the connection
connect_args = {
  "host": "127.0.0.1",
  "port": 3306,
  "user": "pyuser",
  "password": "Py@pp4Demo"
};

db.connect(**connect_args)

# The connection does not change the
# settings
print(
  "{0:<9s}   {1:<7s}   {2:<18s}".format(
    "Connected",
    db.charset, db.collation
  )
)

# Change only the character set
db.set_charset_collation(
  charset = "utf8mb4"
)
print(
  "{0:<9s}   {1:<7s}   {2:<18s}".format(
    "Charset", db.charset, db.collation
  )
)

# Change only the collation
db.set_charset_collation(
  collation = "utf8mb4_unicode_ci"
)
print(
  "{0:<9s}   {1:<7s}   {2:<18s}".format(
    "Collation",
    db.charset, db.collation
  )
)

# Change both the character set and
# collation
db.set_charset_collation(
  charset   = "latin1",
  collation = "latin1_general_ci"
)
print(
  "{0:<9s}   {1:<7s}   {2:<18s}".format(
    "Both", db.charset, db.collation
  )
)

db.close()
