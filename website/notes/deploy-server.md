---
layout: page
title: Deploy Server
---

Tech stack
- Digital Ocean Droplet
- Ubuntu
- Caddy
- rsync


Setting up a Python project on an Ubuntu Digital Ocean Droplet using pipenv

1. Create Droplet with ssh key authentication
2. Save ssh key to 1password
3. Update your ssh config file
4. Download the package index from repositories in `/etc/apt/sources.list` and `/etc/apt/sources.list.d` 
   - `sudo apt update`
5. Install Packages from APT
    - `sudo apt install -y python3-pip pipenv git debian-keyring debian-archive-keyring apt-transport-https`
6. Downloads the GPG key from Cloudsmith's Caddy repository and adds it to your system’s trusted keyring
    - `curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo tee /usr/share/keyrings/caddy-stable-archive-keyring.gpg > /dev/null`
7. Add the Caddy repository to your system's list of package source
    - `curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list`
8. Install Caddy
    - `sudo apt install caddy`
9. Install pipenv
    - `pip3 install pipenv`
10. Setup Caddyfile at `/etc/caddy/Caddyfile`
    - Example:
    ```
   lobbyingintoronto.com {
    reverse_proxy 127.0.0.1:5000
    encode zstd gzip
    tls {
        protocols http/1.1 http/2 http/3
        }
    }
    ```
11. Create a systemd service file
12. sudo systemctl daemon-reload
13. sudo systemctl restart your.service
14. systemctl status your.service


caddy validate --config /etc/caddy/Caddyfile
caddy fmt --overwrite /etc/caddy/Caddyfile