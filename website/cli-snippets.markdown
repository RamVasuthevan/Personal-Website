---
layout: page
title: CLI Snippets
---

1. `open -e test.txt`
    - Opens test.txt in TextEdit on macOS

2. `python3 -m http.server 9000`
    - Opens a Python web server on port 9000 in the current directory

3. `find . -type f ! -path "./.git/*" -print | sed 's|[^/]*/|   |g;s|\(.*\)/\(.*\)|\1/--\2|'`
    - Finds all files in the current directory, excluding .git directory, and prints them in a tree-like format

4. `docker ps -aq | xargs docker rm -f`
    - Kill all Docker containers

5. `ggVG d i CMD+V Esc :wq Enter`
    - In vi, select all, delete, paste and save file
    - **gg** to move the cursor to the beginning of the file
    - **V** to start linewise visual mode
    - **G** to move the cursor to the end of the file, selecting everything in between
    - **d** to delete the selected text
    - **i** to enter insert mode
    - **CMD+V** to paste copied text
    - **Esc** to exit insert mode
    - **:wq Enter** to save and exit

6. `lsof -ti :4000 | xargs kill -9`
    - Kill a process running on port 4000
    - **lsof -ti :4000** finds the process ID (PID) using port 4000
    - **xargs kill -9** sends the kill signal to terminate the process
