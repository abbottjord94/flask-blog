#!/bin/bash

if [ "$1" == "--external" ] || [ "$1" == "-e" ]
then
	sudo FLASK_APP=app.py flask run --host='0.0.0.0' --port=80
else
	sudo FLASK_APP=app.py flask run
fi
