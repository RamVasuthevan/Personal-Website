---
layout: page
title: Fish Shell
---

1. `string upper`
    - Converts a string to uppercase

2. `string lower`
    - Converts a string to lowercase

3. `~/.config/fish/config.fish`
    - Contains the configuration for the Fish shell
    - See the [Fish Tutorial](https://fishshell.com/docs/current/tutorial.html#tut-config) for more information

4. `~/.config/fish/functions`
    - Store functions in this directory

5. `~/.local/share/fish/fish_history`
    - YAML file with fish history [↗](https://fishshell.com/docs/current/cmds/history.html#customizing-the-name-of-the-history-file)

6. `exec fish`
    - Restarts the shell by replacing the current process with a fresh fish session
    - Useful after installing new CLI tools to reload PATH without opening a new terminal tab