---
layout: page  
title: VI Snippet  
---

# Keyboard Shortcuts

`G` : Go to bottom of the page

`$` : Go to the end of the line

`i` : Enter **insert mode**, where you can start typing text

`:wq` : Save the file and quit Vi/Vim

`:q!` : Quit without saving any changes

`10j` : Move down 10 lines

`10k` : Move up 10 lines

`dd` : Delete line

# Keyboard Chains

`ggVG d i CMD+V Esc :wq Enter`
- In vi, select all, delete, paste, and save file
- **gg** to move the cursor to the beginning of the file
- **V** to start linewise visual mode
- **G** to move the cursor to the end of the file, selecting everything in between
- **d** to delete the selected text
- **i** to enter insert mode
- **CMD+V** to paste copied text
- **Esc** to exit insert mode
- **:wq Enter** to save and exit
