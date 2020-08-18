#!/usr/bin/python3
""" Script for full deploy """
from fabric.api import *
import os.path
import os import path

env.hosts = ['34.75.128.100', '54.91.111.249']
env.user = ['ubuntu']


def deploy():
    """ function for full deployment """
    pack = run("do_pack()")
    if pack.failed:
        return False
    """ somehow store newly created folder into a variable?"""

    return(run("do_deploy(archive)"))
