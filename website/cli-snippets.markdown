---
layout: page
title: CLI Snippets
---

1. `open -e test.txt`
    - Opens test.txt in TextEdit on macOS

2. `python3 -m http.server 9000`
    - Opens a Python web server on port 9000 in the current directory

3. `find . -type d \( -name .git -o -name node_modules -o -name .jekyll-cache \) -prune -o -print | sed -e 's/[^-][^\/]*\//--/g' -e 's/^/   /' -e 's/-/|/'`
    - Prints directory structure, excluding the .git, .jekyll-cache, and node_modules directories, in a tree-like format

4. `docker ps -aq | xargs docker rm -f`
    - Kill all Docker containers

5. `ggVG d i CMD+V Esc :wq Enter`
    - In vi, select all, delete, paste and save file
    - **gg** to move the cursor to the beginning of the file
    - **V** to start linewise visual mode
    - **G** to move the cursor to the end of the file, selecting everything in between
    - **d** to delete the selected text
    - **i** to enter insert mode
    - **CMD+V** to paste copied text
    - **Esc** to exit insert mode
    - **:wq Enter** to save and exit

6. `lsof -ti :4000 | xargs kill -9`
    - Kill a process running on port 4000
    - **lsof -ti :4000** finds the process ID (PID) using port 4000
    - **xargs kill -9** sends the kill signal to terminate the process

7. `git log --oneline`
    - Lists all commits in the repository in a compact, one-line format

8. `git commit --allow-empty -m "Empty commit"`
    - Creates an empty commit with the message "Empty commit"

9. Copy and paste from the CLI
   - `cat main.py | pbcopy` copies the contents of pbcopy
   - `pbpaste > main.py` pastes into main.py 

10. macOS Version and System Specs  
    - `sw_vers`  
      Displays the macOS version, including the ProductName, ProductVersion, and BuildVersion.  
      ```
      ram@Rams-MacBook-Air ~/c/Personal-Website (macos-version-and-system-specs-cli)> sw_vers
      ProductName:		macOS
      ProductVersion:		14.6.1
      BuildVersion:		23G93
      ```  
      For more information, see the [sw_vers man page](https://keith.github.io/xcode-man-pages/sw_vers.1.html).

    - `system_profiler SPHardwareDataType`  
      Shows detailed system hardware information including processor, memory, and serial number.  
      ```
      ram@Rams-MacBook-Air ~/c/Personal-Website (macos-version-and-system-specs-cli)> system_profiler SPHardwareDataType

      Hardware:

        Hardware Overview:

          Model Name: MacBook Air
          Model Identifier: Mac14,15
          Model Number: MQKP3LL/A
          Chip: Apple M2
          Total Number of Cores: 8 (4 performance and 4 efficiency)
          Memory: 8 GB
          System Firmware Version: 10151.140.19
          OS Loader Version: 10151.140.19
          Serial Number (system): XXXXXXXXXXXX
          Hardware UUID: XXXXXXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
          Provisioning UDID: 00008112-001624D02688C01E
          Activation Lock Status: Disabled
      ```

    - `system_profiler`  
      Provides a comprehensive overview of all system specifications, including hardware, software, and other components.  
      For more information, see the [system_profiler man page](https://keith.github.io/xcode-man-pages/system_profiler.8.html).
