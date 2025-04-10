---
layout: page
title: git
---

1. `git log --oneline`
    - Lists all commits in the repository in a compact, one-line format

2. `git commit --allow-empty -m "Empty commit"`
    - Creates an empty commit with the message "Empty commit"

3. `git commit --allow-empty --allow-empty-message`
    - Creates an empty commit with an empty message. Useful for triggering CI pipelines allowing the creation of GH PR

4. `git reset --soft HEAD~1`
    - Resets the current branch to the previous commit, keeping the changes in the staging area