# A05 - CDXML to CSV Converter

## Description

This assignment creates a Python script (cdxml2csv.py) that converts ChemDraw XML (.cdxml) files to CSV format with semicolon separators. The script also creates an excel file that has the data formated in a nicer way.
The script:

- Reads molecular structures from .cdxml files
- Generates SMILES notation for each molecule
- Calculates MACCS fingerprints (166-bit molecular descriptors)
- Outputs data in both CSV and formatted Excel formats
- Identifies the molecule with the most MACCS bits set

The output CSV contains three columns:
- **name**: Filename of the .cdxml file
- **smiles**: SMILES notation (without explicit hydrogens)
- **maccs**: List of bit indices (0-165) where MACCS fingerprint bits are set to 1

## Solution

The script uses RDKit library to:
1. Parse CDXML files using XML parsing
2. Build molecular structures from atoms and bonds
3. Generate canonical SMILES notation
4. Calculate MACCS fingerprints
5. Export results to CSV and formatted Excel

Special handling is implemented for molecules with unusual valence (e.g., aluminum compounds with non-standard bonding).

## Commands to Verify Functionality

After cloning the repository, execute the following commands in Git Bash:

### 1. Cloning the Repository

```bash
git clone https://github.com/ValerieBizova/ci2.git
cd ci2/A05
```

### 2. Creating and Activating Virtual Environment

```bash
python -m venv .venv
source .venv/Scripts/activate
```

### 3. Installing Required Packages

```bash
pip install rdkit openpyxl
```

### 4. Runing the Script

```bash
python cdxml2csv.py rx00005.cdxml rx00153.cdxml rx00249.cdxml rx00252.cdxml rx00253.cdxml rx00254.cdxml rx00256.cdxml rx00259.cdxml rx00260.cdxml
```

### 5. Verifying Output

The script will:
- Generate `cdxml2csv.csv` with molecular data
- Generate `cdxml2csv.xlsx` with formatted output (bold headers, column borders)
- Print to console: "Molecule with the most MACCS bits: rx00252.cdxml (36 bits set)"

Check the generated files:
- `cdxml2csv.csv` should contain 9 molecules with their SMILES and MACCS fingerprints
- `cdxml2csv.xlsx` should have formatted headers and borders

## Expected Results

- **Total molecules processed**: 9 files
- **Molecule with most MACCS bits**: rx00252.cdxml (36 bits)
- **Format**: CSV with semicolon separators
- **SMILES**: Without explicit hydrogen atoms (except rx00260 which has structural anomalies)

## 6. Submitting to GitHub

After completing the assignment, push your changes to GitHub:

```bash
git add .
git commit -m "Complete A05 assignment"
git push origin main

## Requirements

- Python 3.10 or higher
- rdkit
- openpyxl


```

Then submit the README.md content to Moodle.