---
layout: page
title: cli
---

1. `open -e test.txt`
    - Opens test.txt in TextEdit on macOS

2. `python3 -m http.server 9000`
    - Opens a Python web server on port 9000 in the current directory

3. `find . -type d \( -name .git -o -name node_modules -o -name .jekyll-cache -o -name venv \) -prune -o -print | sed -e 's/[^-][^\/]*\//--/g' -e 's/^/ /' -e 's/-/|/'`
    - Prints directory structure, excluding the .git, .jekyll-cache, venv and node_modules directories, in a tree-like format

4. `docker ps -aq | xargs docker rm -f`
    - Kill all Docker containers

6. `lsof -ti :4000 | xargs kill -9`
    - Kill a process running on port 4000
    - **lsof -ti :4000** finds the process ID (PID) using port 4000
    - **xargs kill -9** sends the kill signal to terminate the process

7. `sw_vers`
    - Displays the macOS version, including the ProductName, ProductVersion, and BuildVersion. See [sw_vers man page](https://keith.github.io/xcode-man-pages/sw_vers.1.html).

8. `system_profiler SPHardwareDataType`
    - Shows detailed system hardware information including processor, memory, and serial number. See [system_profiler man page](https://keith.github.io/xcode-man-pages/system_profiler.8.html).

9. `system_profiler`
    - Provides a comprehensive overview of all system specifications, including hardware, software, and other components. See [system_profiler man page](https://keith.github.io/xcode-man-pages/system_profiler.8.html).

10. `history`
    - See history of fish shell commands
    - History is stored at `~/.local/share/fish/fish_history`

11. `cp -r (ls -1d -- */| tail -1) (today)-daily-journal`
    - Copy the last directory in the current directory to the (today)-daily-journal directory

12. `date "+%G-w%V-%u"`
    - Prints the [iso week date](https://en.wikipedia.org/wiki/ISO_week_date)