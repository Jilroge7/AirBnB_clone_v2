#!/usr/bin/python3
""" script that generates .tgz archive frm contents of web_static """
from fabric.api import *
import time


def do_pack():
    """function to generate the .tgz """
    local("mkdir -p versions")
    created = (time.strftime("%Y%m%d%H%M%S"))
    if created.succeeded:
        return local("tar -cvzf versions/web_static_{} web_static"
                     .format(created))
    else:
        return None
