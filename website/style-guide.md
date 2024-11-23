---
layout: page
title: Ram's Style Guide
---

This page is a work in progress. But as I polish the sections that already exist, I am adding more rough draft sections. This pushes the page further from being merge-ready and risks leaving it in feature-branch purgatory forever. In theory, I could have feature branches on feature branches, but I don't like that.

## Dates

- Dates should whenever possible be written YYYY-MM-DD. See [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6) `full-date`

## Python

### Dependency Management
- I almost always use pipenv and PipFile (But maybe I [should](https://til.simonwillison.net/python/pyproject) be using poetry and pyproject.toml)

### Libraries

| Purpose               | Preferred                        |
|-----------------------|----------------------------------|
| Web Scraping          | BS4        |
| HTTP Requests         | requests                         |
| SQLite frontend      | datasette                        |
| SQLite ORM     | sqlite-utils (for simple SQLite) |


## Licence
- I prefer the MIT licence because it is the default permissive licence


