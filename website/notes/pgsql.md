---
layout: page
title: SQL (PostgreSQL Variant)
---

<!-- Add Using and Distinct on -->

- `DATE_PART(field, source)`
    - Get the component of a `date`
    - See [Neon PostgreSQL Tutorial: DATE_PART() Function](https://neon.tech/postgresql/postgresql-date-functions/postgresql-date_part)

- `ALTER TABLE table_name RENAME TO new_table_name;`
    - Rename a table
    - See [Neon PostgreSQL Tutorial:PostgreSQL Rename Table](https://neon.tech/postgresql/postgresql-tutorial/postgresql-rename-table)
- `agg_func(<expr>) FILTER (WHERE <condition>)
    - Aggregate values which match a condition
    - Could also be done with a `case` statment
    - [Crunchy Data: Using Postgres FILTER](https://www.crunchydata.com/blog/using-postgres-filter#using-filter)
    <!-- https://chatgpt.com/c/68134931-99a8-8013-9b83-0e70f13c3b6a -->
