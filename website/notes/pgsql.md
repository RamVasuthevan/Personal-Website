---
layout: page
title: SQL (PostgreSQL Variant)
---

- `date_part(field, source)`
    - Get the component of a `date`
    - date_part was a Postgresql-specific wrapper around the SQL standard `extract()`. Starting with PostgreSQL 14, `EXTRACT()` was changed to return type `numeric` instead of `float8` to avoid loss-of-precision issues (See [StackOverflow](https://stackoverflow.com/a/38444997) and [PostgreSQL 14.0 Release Notes](https://www.postgresql.org/docs/release/14.0/#:~:text=Change%20EXTRACT(),date%20data%20type.) 
    - See [Neon PostgreSQL Tutorial: DATE_PART() Function](https://neon.tech/postgresql/postgresql-date-functions/postgresql-date_part)

- `alter table table_name rename to new_table_name;`
    - Rename a table
    - See [Neon PostgreSQL Tutorial:PostgreSQL Rename Table](https://neon.tech/postgresql/postgresql-tutorial/postgresql-rename-table)

- `agg_func(<expr>) FILTER (WHERE <condition>)`
    - Aggregate values which match a condition
    - Could also be done with a `case` statement
    - [Crunchy Data: Using Postgres FILTER](https://www.crunchydata.com/blog/using-postgres-filter#using-filter)
    <!-- https://chatgpt.com/c/68134931-99a8-8013-9b83-0e70f13c3b6a -->

- Sleep Functions
    - `pg_sleep_for(interval)` - Sleep for a specified interval (e.g., '5 minutes', '1.5 seconds')
    - `pg_sleep(seconds)` - Sleep for a specified number of seconds (can be fractional)
    - `pg_sleep_until(timestamp)` - Sleep until a specific timestamp
    - Useful for testing, debugging, or adding delays in scripts
    - See [PostgreSQL Date/Time Functions - Delaying Execution](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-DELAY)

- Division of integers
    - By default, the division of two integers is integer division
    - To do floating point division, you need to cast at least of the integers to numeric
    - See [PostgreSQL Numeric Division](https://www.postgresql.org/docs/current/functions-math.html#:~:text=numeric_type%20/%20numeric_type%20%E2%86%92%20numeric_type)

To do:
    - Add `Using`
    - Add `Distinct on`
