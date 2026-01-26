#!/bin/bash
if [ -z "$1" ]
then
    echo "Usage: ./create_app.sh <app_name>"
    exit 1
fi

mkdir $1
python3 manage.py startapp $1 $1
