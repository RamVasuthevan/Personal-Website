---
layout: page
title: git
---

1. `git log --oneline`
    - Lists all commits in the repository in a compact, one-line format

2. `git commit --allow-empty -m "Empty commit"`
    - Creates an empty commit with the message "Empty commit"

3. `git commit --allow-empty --allow-empty-message -m ""`
    - Creates an empty commit with an empty message. Creates an empty commit with an empty message. Useful for triggering CI pipelines and allowing for the creation of GitHub pull request

4. `git reset --soft HEAD~1`
    - Resets the current branch to the previous commit, keeping the changes in the staging area

5. `git fetch --prune`
    - Fetches from remote and removes any branches that have been deleted on the remote

6. `git diff main..HEAD`
    - See diff for changes on your branch but not on main (one way)

7. `git diff main...HEAD`  
    - See diff for change between your brnach and main (two way)
