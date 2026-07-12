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
    - Fetches from remote and removes stale remote-tracking refs (`origin/*` bookmarks) for branches deleted on the remote — local branches are never touched
    - Prune without fetching: `git remote prune origin`
    - After pruning, `git branch -vv` marks local branches whose remote is gone with `[origin/...: gone]` — usually means the PR was merged (squash merges hide this from `git branch -d`, so `-D` is needed)
    - Make every fetch/pull auto-prune: `git config --global fetch.prune true`

6. `git diff main..HEAD`
    - See diff for changes on your branch but not on main (one way)

7. `git diff main...HEAD`  
    - See diff for change between your brnach and main (two way)

8. `git difftool --staged --tool=code`
    - Opens the staged changes with the `code` diff tool 
    - Needs to be setup with:
        - `git config --global difftool.code.cmd 'code --wait --diff --reuse-window "$LOCAL" "$REMOTE"'` (Set code as a diff tool)
        - `git config --global diff.tool code` (Set code as the default diff tool)
        - `git config --global difftool.prompt false` (Disable the per file diff permission) 

9. `git add --intent-to-add .` (or `git add -N .`)
    - Marks untracked files as known to git without staging
    - By default, untracked files don't show up in `git diff`

10. `git log @{u}..HEAD --oneline`
    - Lists unpushed commits: commits on the current branch that aren't on its upstream (`@{u}`)
    - Branch-agnostic — works on any branch without hardcoding `main`
    - Alternative: `git cherry -v` also detects patch-equivalent commits (`+` = unpushed, `-` = already upstream in some form)
