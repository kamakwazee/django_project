#!/bin/bash
#Starts the django server

source env/bin/activate
python my_django_project/manage.py runserver 0.0.0.0:8000
deactivate

