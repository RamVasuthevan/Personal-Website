---
layout: page  
title: VI  
---

### Keyboard Shortcuts

`G` : Go to bottom of the page

`$` : Go to the end of the line

`0` : Go to the start of the line

`i` : Enter **insert mode**, where you can start typing text

`:wq` : Save the file and quit Vi/Vim

`w` : Save (but not close) file

`:q` : Quit without saving any changes

`10j` : Move down 10 lines

`10k` : Move up 10 lines

`dd` : Delete line

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

#### vim-plug
- I am using [vim-plug](https://github.com/junegunn/vim-plug?tab=readme-ov-file) as my Vim plugin manager
- I installed it using [this](https://github.com/junegunn/vim-plug/blob/d80f495fabff8446972b8695ba251ca636a047b0/README.md#unix) command

### Vim Plugins
- I only have [`tpope/vim-sensible`](https://github.com/tpope/vim-sensible) installed right now