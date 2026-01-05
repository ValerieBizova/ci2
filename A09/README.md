# Assignment A09 - Flask ChEMBL Search with 3D POV-Ray Rendering

## overview:

This project is a single-page chemistry web server that allows users to enter a SMILES string and retrieve:

Compound information from ChEMBL (name, formula, weight, synonyms, etc.)

A 3D image of the molecule generated locally using Open Babel + POV-Ray


## necessary to run:

WSL (Ubuntu recommended) on Windows

Python 3.12

Open Babel (obabel)

POV-Ray (povray)


## cloning my GitHub repository:

$ git clone https://github.com/ValerieBizova/ci2.git

$ cd ci2/A09


## setting up the Linux Environment (Windows WSL):

1. Open PowerShell
2. Run as Administrator
3. wsl --install -d Ubuntu


## moving the project to the Linux Environment (Windows WSL):

$ mkdir -p ~/ci2

$ cp -r /mnt/c/Users/BizovaV/ci2/A09 ~/ci2/

$ cd ~/ci2/A09


## creating a virtual environment:

$ python3 -m venv venv_wsl

$ source venv_wsl/bin/activate


## installing required Python packages:

$ pip install --upgrade pip

$ pip install flask chembl_webresource_client

$ pip install -r requirements.txt


## installing required Linux applications (WSL/Ubuntu):

$ sudo apt update

$ sudo apt install openbabel povray povray-includes


## setting up the static folder and include file:

$ mkdir -p static

$ cp /usr/share/openbabel/*/babel_povray3.inc ./static/


## running the Flask application:

$ python app.py


## using the web application:

    Open web browser and type: http://127.0.0.1:5000

    Enter a SMILES string in the input field (e.g., CCO or C1=CC=CC=C1).

    Click the "Search" button.

-> New Functionality: The page no longer reloads. A JavaScript API request fetches the data and updates the page dynamically.

    View the compound information along with both the 2D Structure (from ChEMBL) and the 3D Rendered Image (created by POV-Ray).


## pushing A09 folder into my GitHub repository:

$ git add A09

$ git commit -m "Add assignment A09: Single-page JS API and POV-Ray 3D rendering"

$ git push origin master


## switching from master to main branch:

$ git checkout main

$ git merge master

$ git push origin main
