---
layout: page
title: psql
---


## Commands

1. `\dn` 
    - List all schemas

2. `\dt schema_name.*`
    - List all tables in a schema

3. `SHOW transaction_read_only;`
    - Check if the current transaction is read only

## Snippets

### Set Role to `Postgres` and Then Set Role Back to Current User

```bash

select current_user;

\set my_user :USER

set role postgres;

select current_user;

create table ram.my_table (
    my_table_id bigserial primary key,
    created_at timestamp with time zone default now()
);

select format('set role %I;', :'my_user')
\gexec
select current_user;
```

## Useful Links

- Use `\gset` [Luca Ferrari: Using psql Variables to Introspect Your Script](https://fluca1978.github.io/2023/10/23/PostgreSQLPSQLVariablesToMonitorTransactions.html)