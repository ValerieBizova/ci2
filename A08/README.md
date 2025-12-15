# Assignment A08 - Flask ChEMBL Search



## cloning my GitHub repository:

```
$ git clone https://github.com/ValerieBizova/ci2.git
$ cd ci2/A08
```



## creating a virtual environment:

```
$ python -m venv .venv
$ .venv\Scripts\Activate.ps1
```



## installing required packages:

```
$ pip install -r requirements.txt
```

this will install Flask, chembl-webresource-client, and Werkzeug



## running the Flask application:

```
$ python app.py
```

the server will start on http://localhost:5000
```


## using the web application:

open web browser and navigate to http://localhost:5000

enter SMILES notation in the input field (e.g., OC(=O)CC(O)C(=O)O for malic acid)

click "Search ChEMBL Database" button

view compound information displayed on the page

perform new searches by entering different SMILES strings



## example output for "malic acid":

SMILES input: OC(=O)CC(O)C(=O)O


ChEMBL ID: CHEMBL225986

Preferred Name: N/A

Molecule Type: Small molecule

Max Phase: N/A

Molecular Formula: C4H6O5

Molecular Weight: 134.09

ALogP: -1.09

H-Bond Acceptors: 3

H-Bond Donors: 3

Polar Surface Area: 94.83

Rotatable Bonds: 3

Ro5 Violations: 0

Synonyms: N/A

Canonical SMILES: O=C(O)C[C@@H](O)C(=O)O

InChI Key: BJEPYKJPYRNKOW-UWTATZPHSA-N

Standard InChI: InChI=1S/C4H6O5/c5-2(4(8)9)1-3(6)7/h2,5H,1H2,(H,6,7)(H,8,9)/t2-/m1/s1



## pushing A08 folder into my GitHub repository:

```
$ git add A08
$ git commit -m "Add assignment A08"
$ git push origin main
```
