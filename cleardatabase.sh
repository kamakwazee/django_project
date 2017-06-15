#!/bin/bash
#Clears the django database

source env/bin/activate
python my_django_project/manage.py flush
deactivate

