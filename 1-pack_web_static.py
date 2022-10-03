#!/usr/bin/python3
from datetime import datetime
from fabric.api import local

def do_pack():
    """ a Fabric script that generates a .tgz archive from web_static """
    day = datetime.now()
    now = d.strftime('%Y%m%d%H%M%S')

    local("mkdir -p versions")
    local("tar -czvf versions/web_static_{}.tgz web_static".format(now))
