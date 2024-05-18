---
layout: page
title: Code Snippets
---

1. `open -e test.txt`
    - Open file in TextEdit

2. `python3 -m http.server 9000`
    - Opens a simple Python web server on port 9000 in the current directory

3. `find . -type f  ! -path "./.git/*" ! -path "./node_modules/*" -print | sed 's|[^/]*/|   |g;s|\(.*\)/\(.*\)|\1/--\2|'`
    - Finds all files in the current directory, excluding .git and node_modules directories, and prints them in a tree-like format

4. `docker ps -aq | xargs docker rm -f`
    - Kill all Docker containers
