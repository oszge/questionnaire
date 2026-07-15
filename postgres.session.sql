CREATE TABLE questioned (id SERIAL PRIMARY KEY, age INT , gender VARCHAR(50), planguage VARCHAR (50), favcolor VARCHAR(20) );

SELECT * FROM questioned;

TRUNCATE TABLE questioned RESTART IDENTITY;