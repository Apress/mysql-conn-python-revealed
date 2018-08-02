DELIMITER $$
CREATE PROCEDURE world.min_max_cities(
    IN in_country char(3),
    INOUT inout_min int,
    OUT out_max int
)
SQL SECURITY INVOKER
BEGIN
  SELECT MIN(Population),
         MAX(Population)
    INTO inout_min, out_max
    FROM world.city
   WHERE CountryCode = in_country
         AND Population >= inout_min;

  SELECT *
    FROM world.city
   WHERE CountryCode = in_country
         AND Population >= inout_min
   ORDER BY Population ASC
   LIMIT 3;

  SELECT *
    FROM world.city
   WHERE CountryCode = in_country
         AND Population >= inout_min
   ORDER BY Population DESC
   LIMIT 3;
END$$
DELIMITER ;
