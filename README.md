# zabbix-scripts

<!-- TOC -->

- [zabbix-scripts](#zabbix-scripts)
- [About](#about)
- [Contributing](#contributing)
  - [Updating the Docker image](#updating-the-docker-image)
  - [Publishing the image](#publishing-the-image)
- [Developers](#developers)
- [License](#license)

<!-- TOC -->

# About

My custom Docker image with [Zabbix](https://www.zabbix.com) scripts.

# Contributing

* See the [REQUIREMENTS.md](REQUIREMENTS.md) file.
* See the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## Updating the Docker image

* Change the content of scripts.

* Change the value of the ``VERSION`` variable in ``zabbix-scripts/Makefile`` file.

* Commands to build the image:

```bash
cd zabbix-scripts

make image
```

Commands to run a container:

```bash
cd zabbix-scripts

make container
```

More information about docker run command: https://docs.docker.com/engine/reference/run/

## Publishing the image

* Create or access your account in Docker Hub and create the repository for custom image. Example: https://hub.docker.com/r/DOCKER_HUB_ACCOUNT/zabbix-scripts

* Commands to publish the image:

```bash
cd zabbix-scripts

make publish
```

# Developers

* Aécio Pires --> [Linkedin](https://www.linkedin.com/in/aeciopires/) | [Github](https://github.com/aeciopires)

# License

* See the [LICENSE](LICENSE) file.
