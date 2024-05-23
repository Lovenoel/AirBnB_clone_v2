#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web-static

from fabric import Connection

with Connection('100.25.16.64') as c:
print(c.run('hostname'))
