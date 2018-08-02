CREATE USER 'pyuser'@'localhost' IDENTIFIED BY 'Py@pp4Demo';
GRANT ALL PRIVILEGES ON world.* TO 'pyuser'@'localhost';
GRANT ALL PRIVILEGES ON py_test_db.* TO 'pyuser'@'localhost';
GRANT ALL PRIVILEGES ON world_x.* TO 'pyuser'@'localhost';
