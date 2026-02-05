---
layout: page  
title: vi  
---

### Keyboard Shortcuts

`G` : Go to bottom of the page

`$` : Go to the end of the line

`0` : Go to the start of the line

`i` : Enter **insert mode**, where you can start typing text

`:wq` : Save the file and quit Vi/Vim

`w` : Save (but not close) file

`:q` : Quit without saving any changes (will fail if there are unsaved changes)

`:q!` : Quit without saving any changes (will force quit even if there are unsaved changes)

`10j` : Move down 10 lines

`10k` : Move up 10 lines

`dd` : Delete line

`dG` : Delete from the current line to the end of file

### Keyboard Chains

#### Select all, delete, paste, and save file: `ggVG d i ⌘V ⎋ :wq ↩`
- **gg** to move the cursor to the beginning of the file
- **V** to start linewise visual mode
- **G** to move the cursor to the end of the file, selecting everything in between
- **d** to delete the selected text
- **i** to enter insert mode
- **⌘V** to paste copied text
- **⎋** to exit insert mode
- **:wq ↩** to save and exit

### Config

- vim config is stored at `~/.vimrc`
