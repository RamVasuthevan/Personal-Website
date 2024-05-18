---
layout: page
title: Code Snippets
---

1. `open -e test.txt`
    - Open file in TextEdit

2. `python3 -m http.server 9000`
    - Opens simple pythin webserver on port 9000 in XXX

3. `find . -type f  ! -path "./.git/*" ! -path "./node_modules/*" > test.txt`
    - XXX

4. `docker ps -aq | xargs docker rm -f`
    - Kill all Docker containers

5. `find . -not -path '*/.git*' -print | sed 's|[^/]*/|   |g;s|\(.*\)/\(.*\)|\1|--\2|'`
    - 