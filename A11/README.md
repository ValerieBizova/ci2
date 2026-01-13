# Assignment A11 - Django Chemical Portal & Database Logging

## overview:

This project transitions the chemical web server from Flask to Django. It implements a three-page portal that retrieves molecule data from the ChEMBL API, generates 3D renders using POV-Ray, and logs every search query into a local SQLite database using Django's ORM.


## necessary to run:

- WSL (Ubuntu recommended) on Windows

- Python 3.12+

- Open Babel (obabel)

- POV-Ray (povray)

- Django & ChEMBL Webresource Client


## cloning my GitHub repository (Git Bash):

$ git clone https://github.com/ValerieBizova/ci2.git

$ mkdir A11


## moving the project to the Linux environment (Ubuntu):

$ cp -r /mnt/c/Users/BizovaV/ci2 ~/

$ cd ~/ci2/A11


## creating a virtual environment:

$ python3 -m venv venv_django

$ source venv_django/bin/activate


## installing required Python packages:

$ pip install django chembl_webresource_client


## installing required Linux applications:

$ sudo apt update

$ sudo apt install openbabel povray


## project Setup & Database Initialization:

$ django-admin startproject chemical_project .

$ python manage.py startapp chem_app


## setting up necessary directories:

$ mkdir static

$ mkdir templates


## creating .html files in templates using the nano command:

$ nano home.html
...


## copying the babel_povray3.inc file from A10:

$ cp ~/ci2/A10/static/babel_povray3.inc ~/ci2/A11/static/


## database configuration:

$ python manage.py makemigrations

$ python manage.py migrate


## running the application:

$ python manage.py runserver

-> Access the portal at: http://127.0.0.1:8000


## to view the logged data in the admin panel:

$ python manage.py createsuperuser

-> Follow prompts to set username and password

-> Access the portal at: http://127.0.0.1:8000/admin  # while the application is running

-> Log in to view the "Search logs" table


## pushing A11 folder into my GitHub repository:

$ git add A11

$ git commit -m "Add assignment A11: Django Chemical Portal & Database Logging"

$ git push origin main


