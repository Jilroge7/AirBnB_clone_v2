#!/usr/bin/env bash
# Prepare web server for web_static deployment

sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test
sudo echo "Simple Content!" | sudo tee /data/web_static/releases/test/index.html
CURR="/data/web_static/current"
sudo rm -f $CURR
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
FILE="/etc/nginx/sites-available/default"
sudo sed -i "53a location /hbnb_static/ {\n\talias /data/web_static/current/;\n\tautoindex off;\n\t}" $FILE
sudo service nginx restart
