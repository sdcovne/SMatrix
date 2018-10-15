#!/bin/bash

python3 -m venv venv && source venv/bin/activate 

pip3 install -r source/requirements/requirements.txt

pip3 install --upgrade setuptools

pyinstaller --onefile --windowed --icon=icon.icns --name SMatrix source/smatrix.py

cd dist/ && mv SMatrix.app /Volumes/Macintosh\ HD/Applications

cd .. && rm -r SMatrix/
