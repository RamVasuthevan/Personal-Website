---
layout: page
title: PostgreSQL Variant of SQL
---

1. `->` vs `->>`
    - `->` is used to access the value of a JSON field as a JSON object
    - `->>` is used to access the value of a JSON field as a string
    - See PostgreSQL Documentation [9.16.1. Processing and Creating JSON Data](https://www.postgresql.org/docs/current/functions-json.html#FUNCTIONS-JSON-PROCESSING)