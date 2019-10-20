# Profiles REST API

aprendiendo DJANGO REST.

generating keys

check if there is a key

ls ~/.ssh

if not lets create a key

ssh-keygen -t rsa -b 4096 -C "cristian.torres19@hotmail.com"
it creates keys

again to check

ls~/.ssh

go to github and settings/ssh keys

cat ~/.ssh/id_rsa.pub

sudo apt-get install python3-venv
python3 -m venv ~/env

activate a virtual enviorement in python
source ~/env/bin/activate

deactivate a virtual enviorement in python
deactivate

start project
django-admin.py startproject project .

create an app
python3 manage.py startapp profiles_api


add apps in settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'profiles_api',
]

test our changes
make sure is connected to vagrant and python virtual enviorement

python3 manage.py runserver 0.0.0:8000


vagrant reload










