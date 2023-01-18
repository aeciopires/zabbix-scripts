<!-- TOC -->

- [General Packages](#general-packages)
- [Docker](#docker)

<!-- TOC -->

Requirements to develop/test in this project

# General Packages

Install the follow packages in your operating system:

* ``git``
* ``make``
* ``python3``

# Docker

Follow the instructions on the page to install Docker.

* Ubuntu: https://docs.docker.com/engine/install/ubuntu/
* Debian: https://docs.docker.com/engine/install/debian/
* CentOS: https://docs.docker.com/engine/install/centos/
* MacOS: https://docs.docker.com/desktop/install/mac-install/

Start the Docker service, configure Docker to boot with the operating system and add your user to the Docker group.

```bash
# Start the Docker service
sudo systemctl start docker

# Configure Docker to boot up with the OS
sudo systemctl enable docker

# Add your user to the Docker group
sudo usermod -aG docker $USER
sudo setfacl -m user:$USER:rw /var/run/docker.sock
```

Reference: https://docs.docker.com/engine/install/linux-postinstall/#configure-docker-to-start-on-boot
