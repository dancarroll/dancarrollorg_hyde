from fabric.api import *
import os

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
DEPLOY_PATH = os.path.join(ROOT_PATH, 'static')

def clean():
    local('rm -rf ./deploy')

def generate():
    local('hyde gen')

def regen():
    clean()
    generate()

def serve():
    local('hyde serve')

def reserve():
    regen()
    serve()

