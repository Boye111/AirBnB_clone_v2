#!/usr/bin/env bash
# Sets up servers for deployment of web static

apt update

apt install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

printf "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tAlx-school\n\t</body>\n</html>\n"

ln -fs /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

loc_header="location \/hbnb\_static\/ {"
loc_content="alias \/data\/web\_static\/current\/;"
new_location="\n\t$loc_header\n\t\t$loc_content\n\t}\n"
sed -i "37s/$/$new_location/" /etc/nginx/sites-available/default

service nginx restart
