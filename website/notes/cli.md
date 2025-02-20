---
layout: page
title: CLI
---

1. `open -e test.txt`
    - Opens test.txt in TextEdit on macOS

2. `python3 -m http.server 9000`
    - Opens a Python web server on port 9000 in the current directory

3. `find . -type d \( -name .git -o -name node_modules -o -name .jekyll-cache \) -prune -o -print | sed -e 's/[^-][^\/]*\//--/g' -e 's/^/   /' -e 's/-/|/'`
    - Prints directory structure, excluding the .git, .jekyll-cache and node_modules directories, in a tree-like format

4. `docker ps -aq | xargs docker rm -f`
    - Kill all Docker containers

6. `lsof -ti :4000 | xargs kill -9`
    - Kill a process running on port 4000
    - **lsof -ti :4000** finds the process ID (PID) using port 4000
    - **xargs kill -9** sends the kill signal to terminate the process

7. `git log --oneline`
    - Lists all commits in the repository in a compact, one-line format

8. `git commit --allow-empty -m "Empty commit"`
    - Creates an empty commit with the message "Empty commit"

9. `gh pr list`
   - List all open PRs in the repo

10. `gh pr view --web`
   - Opens the PR for the branch you are on
