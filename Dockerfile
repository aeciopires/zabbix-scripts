FROM python:3.11.1-slim

LABEL maintainer="Aecio Pires" \
      date_create="17/01/2023" \
      version="0.1.0" \
      description="Zabbix scripts" \
      licensce="GPLv3"

# References:
# See the README.md file in the About section

#---------------------------------#
# Variables
#---------------------------------#


#-------- End - Variables --------#

# User context change
USER root

# Copy files
COPY scripts /scripts

# Installation of packages necessary to use the scripts.
RUN apt-get update \
    # Clean packages
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    # Create user to run application e adjustments to the permissions required for execution.
    && adduser --disabled-password --shell /sbin/nologin --gecos "" zabbix-scripts \
    && chown zabbix-scripts:zabbix-scripts /scripts \
    # Configure permissions
    && chmod -R +x /scripts

# User context change
USER zabbix-scripts

# Installation of packages necessary to use the scripts.
RUN pip install zabbix_api

# Directory context change
WORKDIR /scripts

# Executing the command to start the application.
CMD bash
