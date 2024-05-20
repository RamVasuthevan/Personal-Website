---
layout: page
title: Code Snippets
---

1. `open -e test.txt`
    - Open test.txt in TextEdit on macOS

2. `python3 -m http.server 9000`
    - Opens a simple Python web server on port 9000 in the current directory

3. `find . -type f  ! -path "./.git/*" ! -path "./node_modules/*" -print | sed 's|[^/]*/|   |g;s|\(.*\)/\(.*\)|\1/--\2|'`
    - Finds all files in the current directory, excluding .git and node_modules directories, and prints them in a tree-like format

4. `docker ps -aq | xargs docker rm -f`
    - Kill all Docker containers

5. `ggVG d i Cmd+V Esc :wq Enter`
    - In vi, select all, delete, paste and save file
    - **gg** to move the cursor to the beginning of the file
    - **V** to start linewise visual mode
    - **G** to move the cursor to the end of the file, selecting everything in between
    - **d** to delete the selected text
    - **i** to enter insert mode
    - **Cmd+V** to paste copied text
    - **Esc** to exit insert mode
    - **:wq Enter** to save and exit
