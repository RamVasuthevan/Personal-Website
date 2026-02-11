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

#### Select all, delete, paste, and save file: `ggVG d i CMD+V Esc :wq Enter`
- **gg** to move the cursor to the beginning of the file
- **V** to start linewise visual mode
- **G** to move the cursor to the end of the file, selecting everything in between
- **d** to delete the selected text
- **i** to enter insert mode
- **CMD+V** to paste copied text
- **Esc** to exit insert mode
- **:wq Enter** to save and exit

### Special Characters in Command-Line Mode

#### `%` — Current Filename

In Neovim/Vim's command line (after `:`), `%` expands to the current buffer's filename. This is useful for shell commands that operate on the file you're editing:

- `:!wc %` — word count of current file
- `:!chmod +x %` — make current file executable
- `:!git diff %` — diff current file

If you need a literal `%` (e.g., in a `date` format string), escape it with a backslash:

`:!date "+\%G-w\%V-\%u"` — without escaping, `%G`, `%V`, `%u` would each expand to the filename

See `:help cmdline-special` and `:help :!`

### Inserting Command Output

`:r !command` — read the output of a shell command into the buffer at the cursor position. For example:

`:r !date "+\%G-w\%V-\%u"` — inserts the ISO week date (e.g., `2026-w07-2`) into the buffer

In insert mode, `<C-r>=strftime("%G-w%V-%u")<CR>` evaluates a Vimscript expression and inserts the result. This uses Vim's built-in `strftime()`, so no `%` escaping is needed. See `:help i_CTRL-R` and `:help expression-register`.

### Buffers

A buffer is the in-memory representation of a file. The current buffer is whichever file is active in the current window. The file on disk is not changed until you `:w`.

- `:ls` or `:buffers` — list all open buffers (`%` marks the current one, `a` means active, `h` means hidden)
- `:echo @%` — show the current buffer's filename
- `:file` — show filename plus status info

### Config

- vim config is stored at `~/.vimrc`
