---
layout: page
title: git
---

## List Commits in a Compact Format

`git log --oneline`

Lists all commits in the repository in a compact, one-line format.

## Create an Empty Commit

`git commit --allow-empty -m "Empty commit"`

Creates an empty commit with the message "Empty commit".

## Create an Empty Commit with an Empty Message

`git commit --allow-empty --allow-empty-message -m ""`

Useful for triggering CI pipelines and allowing for the creation of GitHub pull requests.

## Undo the Last Commit, Keeping Changes Staged

`git reset --soft HEAD~1`

Resets the current branch to the previous commit, keeping the changes in the staging area.

## Remove Stale Remote-Tracking Refs

`git fetch --prune`

Fetches from remote and removes stale remote-tracking refs (`origin/*` bookmarks) for branches deleted on the remote. Local branches are never touched. To prune without fetching, use `git remote prune origin`.

After pruning, `git branch -vv` marks local branches whose remote is gone with `[origin/...: gone]`. This usually means the PR was merged. Squash merges hide this from `git branch -d`, so `-D` is needed.

To make every fetch and pull auto-prune:

```bash
git config --global fetch.prune true
```

## See Diff for Changes on Your Branch but Not on Main (One Way)

`git diff main..HEAD`

## See Diff for Changes Between Your Branch and Main (Two Way)

`git diff main...HEAD`

## Open Staged Changes in the VS Code Diff Tool

`git difftool --staged --tool=code`

Needs to be set up with:

```bash
git config --global difftool.code.cmd 'code --wait --diff --reuse-window "$LOCAL" "$REMOTE"' # Set code as a diff tool
git config --global diff.tool code             # Set code as the default diff tool
git config --global difftool.prompt false      # Disable the per file diff permission
```

## Mark Untracked Files as Known to Git Without Staging

`git add --intent-to-add .` (or `git add -N .`)

By default, untracked files don't show up in `git diff`.

## List Unpushed Commits

`git log @{u}..HEAD --oneline`

Lists commits on the current branch that aren't on its upstream (`@{u}`). Branch-agnostic, so it works on any branch without hardcoding `main`.

`git cherry -v` is an alternative that also detects patch-equivalent commits (`+` = unpushed, `-` = already upstream in some form).
