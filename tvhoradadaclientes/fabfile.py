from fabric.api import task
from fabric.contrib.project import upload_project
from o2wfab import *


env.BASE_DIR = "/var/www/virtual/tvhoradada.tv/gestioniptv/"
env.REMOTE_DIR = env.BASE_DIR
env.hosts = ['cetus']
