#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web-static

# Install Nginx if not already installed
if ! dpkg -l nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file for testing Nginx configuration
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create or recreate symbolic link
sudo rm -rf /data/web_static/current
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Set ownership of /data/ folder recursively to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve content from /data/web_static/current/
# using alias
sudo sed -i '/location \/hbnb_static\/ {/a \\t\talias /data/web_static/current/;' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart

# Exit with success
exit 0
