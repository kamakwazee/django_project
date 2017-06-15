#!/bin/bash

source env/bin/activate
python my_django_project/manage.py dbshell
deactivate

