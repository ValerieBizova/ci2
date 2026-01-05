# Assignment A08 - Flask ChEMBL Search

## cloning my GitHub repository:
$ git clone https://github.com/ValerieBizova/ci2.git

$ cd ci2/A08

## creating a virtual environment:
$ python -m venv venv

$ source venv/Scripts/activate

## installing required Python packages:
$ pip install flask chembl_webresource_client

## freezing dependencies:
$ pip freeze > requirements.txt

## running the Flask application:
$ python app.py

## using the web application:

1. open web browser and type http://127.0.0.1:5000
2. enter SMILES in the input field
3. click the "Search" button

-> compound information is now displayed on the page

4. perform new searches by entering different SMILES in the input field

## example output for "malic acid":

SMILES input: O=C(O)CC(O)C(=O)O

General Information

    ChEMBL ID: CHEMBL1455497
    Name: Malic Acid
    Synonyms: Apple Acid, D,L-Malic Acid, Dl-Malic Acid...
    Molecular Formula: C4H6O5
    Molecular Weight: 134.09
    Molecule Type: Small molecule

Identifiers

    SMILES: O=C(O)CC(O)C(=O)O
    InChI: InChI=1S/C4H6O5/c5-2(4(8)9)1-3(6)7/h2,5H,1H2,(H,6,7)(H,8,9)
    InChIKey: BJEPYKJPYRNKOW-UHFFFAOYSA-N

Calculated Properties

    LogP (ALogP): -1.09
    H-Bond Acceptors: 3
    H-Bond Donors: 3
    Polar Surface Area: 94.83
    Heavy Atoms: 9
    Rule of 5 Violations: 0

Structure

## pushing A08 folder into my GitHub repository:
$ git add A08

$ git commit -m "Add assignment A08"

$ git push origin main
