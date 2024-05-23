#!/usr/bin/python3
from fabric import Connection

# Define the host
host = 'ubuntu@100.25.16.64'

# Define the task to deploy your web static files
def deploy_web_static():
    with Connection(host) as conn:
        # Add your deployment commands here
        conn.run('echo "Deploying web static files..."')
        conn.run('echo "Done!"')

# Add more tasks if needed

# Run the script when executed directly
if __name__ == "__main__":
    deploy_web_static()
