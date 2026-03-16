-- Lists all records from second_table where name has a value.
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
