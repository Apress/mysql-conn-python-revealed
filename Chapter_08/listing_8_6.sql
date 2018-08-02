DROP PROCEDURE IF EXISTS world.top_cities;
DELIMITER $$
CREATE PROCEDURE world.top_cities(
    IN in_country char(3)
)
SQL SECURITY INVOKER
BEGIN
  SELECT Name, District, Population
    FROM world.city
   WHERE CountryCode = in_country
         AND Population
   ORDER BY Population ASC
   LIMIT 3;

  SELECT Name, District, Population
    FROM world.city
   WHERE CountryCode = in_country
         AND Population
   ORDER BY Population DESC
   LIMIT 3;
END$$
DELIMITER ;
