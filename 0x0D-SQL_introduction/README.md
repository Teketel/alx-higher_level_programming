0x0D. SQL - Introduction tasks and solutions
====

## Solution files

| Question | Solution files |
| ------   | ------         |
|1. Write a script that lists all databases of your MySQL server. | `0-list_databases.sql` |
|2. Write a script that creates the database hbtn_0c_0 in your MySQL server. | `1-create_database_if_missing.sql`
|3. Write a script that deletes the database hbtn_0c_0 in your MySQL server. If the database hbtn_0c_0 doesn’t exist, your script should not fail
You are not allowed to use the SELECT or SHOW statements | `2-remove_database.sql`
|4. Write a script that lists all the tables of a database in your MySQL server. The database name will be passed as argument of mysql command (in the following example: mysql is the name of the database) | `3-list_tables.sql`
|5. Write a script that creates a table called first_table in the current database in your MySQL server. | `4-first_table.sql`
|6. Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server. | `5-full_table.sql`
|7. Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server. | `6-list_values.sql`
|8. Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server. | `7-insert_value.sql`
|9.Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server. | `8-count_89.sql`
|10. Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows. | `9-full_creation.sql`
|11. Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server. | `10-top_score.sql`
|12. Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server. | `11-best_score.sql`
|13. Write a script that updates the score of Bob to 10 in the table second_table. | `12-no_cheating.sql`
|14. Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server. | `13-change_class.sql`
|15. Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server. | `14-average.sql`
|16. Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server. | `15-groups.sql`
|17. Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server. | `16-no_link.sql`
|18. Write a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server. You need to convert all of the following to UTF8: | `100-move_to_utf8.sql`
|19. Import in hbtn_0c_0 database this table dump: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql). Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending). | `101-avg_temperatures.sql`
|20. Import in hbtn_0c_0 database this table dump: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql) (same as Temperatures #0). Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending) | `102-top_city.sql`
|21. Import in hbtn_0c_0 database this table dump: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql) (same as Temperatures #0). Write a script that displays the max temperature of each state (ordered by State name). | `103-max_state.sql`