#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
#+------------------------------------------------------------------------------+
# Description: Update host interface of zabbix-server
#
# Author: Aecio Pires <https://blog.aeciopires.com/sobre/>
# Date: 17-Jan-2023
#
# Example:
#   python updateZabbixServerHostInterface
#
# To access Zabbix API create the follow environment variables (change the values ​​as needed):
#
# export ZABBIX_WEB_URL="http://localhost:8888"
# export ZABBIX_WEB_LOGIN="Admin"
# export ZABBIX_WEB_PASS="zabbix"
# export ZABBIX_AGENT_ADDRESS="zabbix-zabbix-agent.monitoring.svc.cluster.local"
#
# PS.: Developed and tested using Python (3.8.10 and 3.11.1) and Zabbix (6.0.12 and 6.2.6)
#
#+------------------------------------------------------------------------------+

# References:
#
# https://www.zabbix.com/documentation/current/en/manual/api/reference/hostinterface/object
# https://www.zabbix.com/documentation/current/en/manual/api/reference/host/get
# https://www.zabbix.com/documentation/current/en/manual/api/reference/host/update
# https://support.zabbix.com/browse/ZBX-13589
# https://stackoverflow.com/questions/40697845/what-is-a-good-practice-to-check-if-an-environmental-variable-exists-or-not
# https://stackoverflow.com/questions/9079036/how-do-i-detect-the-python-version-at-runtime



from zabbix_api import ZabbixAPI
import os, sys


#------------------------
# Variables
#------------------------
ENABLE_DEBUG         = True
ZABBIX_WEB_URL       = os.getenv('ZABBIX_WEB_URL')
ZABBIX_WEB_LOGIN     = os.getenv('ZABBIX_WEB_LOGIN')
ZABBIX_WEB_PASS      = os.getenv('ZABBIX_WEB_PASS')
ZABBIX_AGENT_ADDRESS = os.getenv('ZABBIX_AGENT_ADDRESS')


#------------------------
#------------------------
# Main
#------------------------
#------------------------

# Required environment variables
MANDATORY_ENV_VARS = ['ZABBIX_WEB_URL', 'ZABBIX_WEB_LOGIN', 'ZABBIX_WEB_PASS', 'ZABBIX_AGENT_ADDRESS']

# Checking if required environment variables exist
for var in MANDATORY_ENV_VARS:
    if var not in os.environ:
        raise EnvironmentError("[ERROR] Failed because the enviroment variable {} is not set.".format(var))

# Displaying the value of required environment variables
if ENABLE_DEBUG:
    print('\n [DEBUG] ', sys.version)
    print(
        '\n ZABBIX_WEB_URL: ', ZABBIX_WEB_URL,
        '\n ZABBIX_WEB_LOGIN: ', ZABBIX_WEB_LOGIN,
        '\n ZABBIX_WEB_PASS: ', ZABBIX_WEB_PASS,
        '\n ZABBIX_AGENT_ADDRESS: ', ZABBIX_AGENT_ADDRESS,
    )

# Accessing Zabbix API
zapi = ZabbixAPI(server=ZABBIX_WEB_URL, timeout=120)
zapi.login(ZABBIX_WEB_LOGIN,ZABBIX_WEB_PASS)

# Getting informations of Zabbix Server host
hosts = zapi.host.get({
    "selectInterfaces": ["interfaceid"],
    "filter": {
        "host": [
            "Zabbix server"
        ]
    }
})

# Getting hostid from Zabbix Server
if ENABLE_DEBUG:
    print(
        '\n [DEBUG] Informations of Zabbix Server', hosts
    )

    print(
        '\n [DEBUG]',
        '\n HOSTID: ', hosts[0]["hostid"],
        '\n HOSTNAME: ', hosts[0]["name"],
        '\n INTERFACEID', hosts[0]["interfaces"][0]["interfaceid"]
    )

# Updating Zabbix Server host interface IP address
hosts = zapi.host.update({
    "hostid": hosts[0]["hostid"],
    "status": 0,
    "interfaces": [
        {
            "type": 1,
            "interfaceid": hosts[0]["interfaces"][0]["interfaceid"],
            "main": 1,
            "useip": 0,
            "ip": "127.0.0.1",
            "dns": ZABBIX_AGENT_ADDRESS,
            "port": 10050
        }
    ]
})

# Logout Zabbix API
zapi.logout()
