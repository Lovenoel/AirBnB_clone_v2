#!/usr/bin/python3
-- Create or use the test database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create or update the test user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant privileges
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
