#!/bin/bash

python3 -m venv venv && source venv/bin/activate

pip3 install -r source/requirements/requirements.txt

pip3 install --upgrade setuptools

pyinstaller --onefile --windowed --name SMatrix source/smatrix.py

mv  dist/SMatrix  /usr/local/bin/

mv  icon.pgn /usr/local/bin

mv  smatrix.desktop  /usr/share/applications/
