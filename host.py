#!/usr/bin/python3

from fabric import Connection
# Define a list of hosts
hosts = ['54.237.217.181', '100.25.16.64']

# Loop through each host and execute the script
for host in hosts:
    with Connection(host=host,
                    user='ubuntu',
                    connect_kwargs={
                        "key_filename": "/root/.ssh/school",
                        "passphrase": "betty",
                        },
                    ) as conn:
        conn.put(local='/AirBnB_clone_v2/0-setup_web_static.sh', remote='/home/ubuntu', preserve_mode=True)
