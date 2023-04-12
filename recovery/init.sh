#!/bin/sh

echo "-------------------------------------"
echo "install depedendancies python with pip"
pip install -r requirements.txt

echo "-------------------------------------"
echo "Add variable en flask"
export FLASK_DEBUG=1
export FLASK_ENV=development

echo "-------------------------------------"
echo "init data base "
python3 model.py
