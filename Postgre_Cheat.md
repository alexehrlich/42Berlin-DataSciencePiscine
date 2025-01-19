# PostgreSQL Cheat Sheet

---

## **Basic Commands**

### Connection & Database Management
```sql
-- Connect to a database
\c database_name;

-- List all databases
\l

-- Create a database
CREATE DATABASE database_name;

-- Drop a database
DROP DATABASE database_name;

-- List tables in the current database
\dt

-- Describe a table
\d table_name;

-- Load data from a .sql file which contains create command
\i /path/to/file.sql

```
---

## **Table Management**

### Creating and Dropping Tables
```sql
-- Create a table
CREATE TABLE table_name (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Drop a table
DROP TABLE table_name;
```

### Altering Tables
```sql
-- Add a column
ALTER TABLE table_name ADD COLUMN email VARCHAR(100);

-- Drop a column
ALTER TABLE table_name DROP COLUMN email;

-- Rename a column
ALTER TABLE table_name RENAME COLUMN old_name TO new_name;

-- Change data type of a column
ALTER TABLE table_name ALTER COLUMN age TYPE BIGINT;
```

---

## **Data Manipulation**

### Insert, Update, and Delete
```sql
-- Insert data
INSERT INTO table_name (name, age) VALUES ('John', 30);

-- Update data
UPDATE table_name SET age = 31 WHERE name = 'John';

-- Delete data
DELETE FROM table_name WHERE name = 'John';
```

### Select Queries
```sql
-- Select all columns
SELECT * FROM table_name;

-- Select specific columns
SELECT name, age FROM table_name;

-- Filter results
SELECT * FROM table_name WHERE age > 25;

-- Sorting results
SELECT * FROM table_name ORDER BY age DESC;

-- Limit results
SELECT * FROM table_name LIMIT 5;

-- Pattern matching
SELECT * FROM table_name WHERE name LIKE 'J%';

-- Range filtering
SELECT * FROM table_name WHERE age BETWEEN 20 AND 30;

-- Specific values
SELECT * FROM table_name WHERE age IN (25, 30, 35);

-- Eliminate duplicates
SELECT DISTINCT name FROM table_name;

-- Count rows matching a condition
SELECT COUNT(*) FROM table_name WHERE age > 25;

-- Having
SELECT country_of_birth, COUNT(*) FROM person GROUP BY country_of_birth HAVING COUNT(*) > 5 ORDER BY country_of_birth;
```

---

## **Joins**
```sql
-- Inner Join
SELECT a.id, a.name, b.order_id
FROM customers a
INNER JOIN orders b ON a.id = b.customer_id;

-- Left Join
SELECT a.id, a.name, b.order_id
FROM customers a
LEFT JOIN orders b ON a.id = b.customer_id;

-- Right Join
SELECT a.id, a.name, b.order_id
FROM customers a
RIGHT JOIN orders b ON a.id = b.customer_id;
```

---

## **Aggregate Functions**
```sql
-- Count rows
SELECT COUNT(*) FROM table_name;

-- Sum of a column
SELECT SUM(amount) FROM sales;

-- Average value
SELECT AVG(age) FROM table_name;

-- Maximum value
SELECT MAX(age) FROM table_name;

-- Minimum value
SELECT MIN(age) FROM table_name;
SELECT car_name, MIN(prince) FROM cars ORDER BY car_name;

-- Grouping
SELECT department, COUNT(*) FROM employees GROUP BY department;
```

---

## **Indexes**
```sql
-- Create an index
CREATE INDEX index_name ON table_name (column_name);

-- Drop an index
DROP INDEX index_name;
```

---

## **Transactions**
```sql
-- Start a transaction
BEGIN;

-- Commit a transaction
COMMIT;

-- Rollback a transaction
ROLLBACK;
```

---

## **Views**
```sql
-- Create a view
CREATE VIEW view_name AS
SELECT name, age FROM table_name WHERE age > 30;

-- Drop a view
DROP VIEW view_name;
```

---

## **User Management**
```sql
-- Create a new user
CREATE USER username WITH PASSWORD 'password';

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE database_name TO username;

-- Revoke privileges
REVOKE ALL PRIVILEGES ON DATABASE database_name FROM username;

-- Drop a user
DROP USER username;
```

---

## **Backup & Restore**
```bash
-- Backup database
pg_dump database_name > backup.sql

-- Restore database
psql database_name < backup.sql
```

---

## **Common Meta Commands**
```sql
-- Quit psql
\q

-- Show current database
\conninfo

-- Show query execution time
\timing

-- List all schemas
\dn

-- Show all sequences
\ds
```

---

