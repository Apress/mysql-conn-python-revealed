import mysqlx
from config import connect_args

db = mysqlx.get_session(**connect_args)
schema = db.get_schema("py_test_db")
city_col = schema.get_collection("city")

# Get the location of Sydney
statement = city_col.find("Name = :city")
statement.fields(
  "Geography.Location AS Location")
statement.bind("city", "Sydney")
result = statement.execute()
sydney = result.fetch_one()

# Define the formula for converting
# the location in GeoJSON format to
# the binary format used in MySQL
to_geom = "ST_GeomFromGeoJSON({0})"
sydney_geom = to_geom.format(
  sydney["Location"])
other_geom = to_geom.format(
  "Geography.Location")
distance = "ST_Distance({0}, {1})".format(
  sydney_geom, other_geom)

statement = city_col.find("Name != 'Sydney'")
statement.fields(
    "Name",
    "Geography.State AS State",
    distance + " AS Distance"
)
statement.sort(distance)
result = statement.execute()

cities = result.fetch_all()
print("{0:14s}   {1:28s}   {2:8s}"
  .format("City", "State", "Distance"))
print("-"*56)
for city in cities:
  # Convert the distance to kilometers
  distance = city["Distance"]/1000
  print("{Name:14s}   {State:28s}"
    .format(**city)
    + "     {0:4d}"
    .format(int(distance))
  )

db.close()
