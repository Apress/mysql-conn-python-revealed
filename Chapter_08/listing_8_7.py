import mysqlx
from config import connect_args

db = mysqlx.get_session(**connect_args)
sql = db.sql(
  "CALL world.top_cities('USA')")
result = sql.execute()

fmt = "{0:11s}   {1:14s}   {2:10d}"
print("{0:11s}   {1:14s}   {2:10s}"
  .format(
    "City", "State", "Population"
  )
)

more = True
while more:
  print("-"*41)
  row = result.fetch_one()
  while row:
    print(fmt.format(
      row["Name"],
      row["District"],
      row["Population"]
    ))
    row = result.fetch_one()
  more = result.next_result()

db.close()
