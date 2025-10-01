---
layout: page
title: SQL (PostgreSQL Variant)
---

## Functions

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

## Client Instructions

- `set` vs `set local`
    - `set` changes configuration parameters for the entire session (connection)
    - `set local` changes configuration parameters only for the current transaction
    - `set local` settings are automatically reverted when the transaction commits or rolls back. For this reason, it must be executed within a transaction block.

- `plpgsql.extra_errors`
    - Controls additional error checking in PL/pgSQL stored procedures and functions
    - Possible values: `'none'` (default), `'all'`, or comma-separated list of specific checks
    - Available checks: `'shadowed_variables'`, `'strict_multi_assignment'`, `'too_many_rows'`
    - `'strict_multi_assignment'` ensures variable count matches value count in assignments
    - `'shadowed_variables'` warns about variable name conflicts in nested scopes
    - `'too_many_rows'` raises errors when SELECT INTO returns multiple rows
    - `'all'` enables all available checks
    - Generally used during development to catch potential bugs early
    - See [PostgreSQL PL/pgSQL Extra Checks](https://www.postgresql.org/docs/current/plpgsql-development-tips.html#PLPGSQL-EXTRA-CHECKS)

- `client_min_messages`
    - Controls which message types are sent from the server to the client
    - Possible values (from lowest to highest): `debug5`, `debug4`, `debug3`, `debug2`, `debug1`, `log`, `notice` (default), `warning`, `error`
    - Setting to `warning` means only WARNING, ERROR, FATAL, and PANIC messages are shown
    - Lower settings show more verbose output, higher settings show fewer messages
    - See [PostgreSQL Client Connection Defaults](https://www.postgresql.org/docs/current/runtime-config-client.html#GUC-CLIENT-MIN-MESSAGES)

- `statement_timeout`
    - Sets a maximum execution time limit for individual SQL statements
    - Possible values: time intervals (e.g., `'10ms'`, `'1s'`, `'5min'`) or `0` (no timeout, default)
    - Any statement that runs longer than the specified time will be automatically cancelled
    - See [PostgreSQL Statement Timeout](https://www.postgresql.org/docs/current/runtime-config-client.html#GUC-STATEMENT-TIMEOUT)

- `transaction_timeout`
    - Sets a maximum execution time limit for entire transactions (added in PostgreSQL 17)
    - Possible values: time intervals (e.g., `'1min'`, `'5min'`, `'1h'`) or `0` (no timeout, default)
    - Terminates any session with a transaction that runs longer than the specified time
    - Applies to both explicit transactions (BEGIN/COMMIT) and implicit single-statement transactions
    - See [PostgreSQL Transaction Timeout](https://www.postgresql.org/docs/current/runtime-config-client.html#GUC-TRANSACTION-TIMEOUT)

To do:
    - Add `Using`
    - Add `Distinct on`
