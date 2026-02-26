---
layout: page  
title: vi  
---

### Keyboard Shortcuts

#### Normal mode

`G` : Go to bottom of the page

`$` : Go to the end of the line

`0` : Go to the start of the line

`^` : Go to first not blank character of the line

`i` : Enter **insert mode**, where you can start typing text

`10j` : Move down 10 lines

`10k` : Move up 10 lines

`dd` : Delete line

`dG` : Delete from the current line to the end of file

#### Command-line mode

Type `:` from normal mode to enter command-line mode, then the command.

`:w` : Save (but not close) file

`:wq` : Save the file and quit Vi/Vim

`:q` : Quit without saving any changes (will fail if there are unsaved changes)

`:q!` : Quit without saving any changes (will force quit even if there are unsaved changes)

`%` : In command-line mode, expands to the current buffer's filename (e.g., `:!wc %`). Escape with `\%` for a literal `%` (e.g., `:!date "+\%G-w\%V-\%u"`) 

`:!code %` : Open the current file in VS Code/Cursor

### Keyboard Chains

#### Select all, delete, paste, and save file: `ggVG d i CMD+V Esc :wq Enter`
- **gg** to move the cursor to the beginning of the file
- **V** to start linewise visual mode
- **G** to move the cursor to the end of the file, selecting everything in between
- **d** to delete the selected text
- **i** to enter insert mode
- **CMD+V** to paste copied text
- **Esc** to exit insert mode
- **:wq Enter** to save and exit

### Config

- vim config is stored at `~/.vimrc`
