# docker-discord-bot

This is a fun project that allows you to containerize your dicsord bot as a docker container. I run this on a Raspberry Pi 4 Model B.

# Screenshots
<details>
<summary>Install Discord Python dependency</summary>
<br>

![bot-flip](https://github.com/permach-tech/docker-discord-bot/images/bot-flip.png)

</details>
## Features

- Docker for containerization
- Lightweight container running on a Raspberry Pi (or any pc of your choosing)
- No cloud costs

## Requirements

- Python 3.9 or higher
- Docker
- Device such as a RaspBerry Pi, mini PC, NUC, Laptop, etc.
- linux OS such as Ubuntu (I am using Ubuntu 24.04.2 LTS)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/permach-tech/docker-discord-bot.git
    cd docker-discord-bot
    ```
2. Install prequisites:
    <details>
    <summary>Discord Developer Portal</summary>
    <br>
    1. Got to and login with your Discord credentials: https://discord.com/developers/applications <br>
    2. Select <b>New Application</b> button on the top right, name your bot whatever you like <br>
    3. Go to the <b>installation</b> tab <br>
    4. <b>Installation Contexts:</b> Guild Install <br>
        <b>Default Install Settings:</b>
        - Scopes: applications.commands, bot
        - Permissions: Send Messages <br>
    5. Copy the link, paste it in your browser, and invite the Bot to your Discord server
    </details> 

   <details>
    <summary>Install Docker on Ubuntu</summary>
    <br>
    
    # Add Docker's official GPG key:
   ```bash
    sudo apt-get update
    sudo apt-get install ca-certificates curl gnupg
    sudo install -m 0755 -d /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    sudo chmod a+r /etc/apt/keyrings/docker.gpg
    ```
   
    # Add the repository to Apt sources:
   ```bash
    echo \
      "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
      "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
      sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update
    ```
   
    # Install the latest version
    ```bash
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    ```

   # Check Installed Version
    ```bash
    docker -v
    ```

    # Check Docker Compose

    ```bash
    docker compose
    ```

    # Check runtime

    ```bash
    sudo docker run hello-world
    ```

    # **Use Docker without sudo**

    ```bash
    sudo usermod -aG docker $USER
    ```
    </details>
    
    <details>
    <summary>Install Discord Python dependency</summary>
    <br>

   ```bash
    pip install discord.py
    ```
    </details>
## Usage

## API Endpoints

## Docker