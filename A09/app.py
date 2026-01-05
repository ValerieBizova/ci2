import os
import subprocess
import re
from flask import Flask, render_template, request, jsonify
from chembl_webresource_client.new_client import new_client

app = Flask(__name__)

# Setup paths
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_FOLDER = os.path.join(BASE_DIR, 'static')

if not os.path.exists(STATIC_FOLDER):
    os.makedirs(STATIC_FOLDER)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    data_in = request.get_json()
    smiles = data_in.get("smiles", "").strip()
    
    if not smiles:
        return jsonify({"error": "Please enter a SMILES string."}), 400

    try:
        molecule_client = new_client.molecule
        res = molecule_client.filter(molecule_structures__canonical_smiles=smiles)
        
        if not res:
            return jsonify({"error": "No compound found for this SMILES."}), 404
        
        data = res[0]
        props = data.get('molecule_properties') or {}
        structs = data.get('molecule_structures') or {}

        # Name and Synonyms logic from your previous version
        raw_name = data.get('pref_name')
        name = raw_name.title() if raw_name else 'N/A'
        
        synonyms_list = data.get('molecule_synonyms') or []
        syn_names = [(s.get('synonyms') or s.get('molecule_synonym', '')).title() for s in synonyms_list if s]
        synonyms_str = (', '.join(syn_names[:3]) + "...") if len(syn_names) > 3 else (', '.join(syn_names) if syn_names else 'N/A')

        # 3D Rendering Logic
        pov_path = os.path.join(STATIC_FOLDER, "mol.pov")
        png_path = os.path.join(STATIC_FOLDER, "mol.png")
        
        # Step A: obabel
        subprocess.run(["obabel", f"-:{smiles}", "-O", pov_path, "--gen3d"], check=True)
        # Step B: povray (+L allows finding the .inc file in static)
        subprocess.run(["povray", f"+I{pov_path}", f"+O{png_path}", "+W600", "+H400", "+A", f"+L{STATIC_FOLDER}", "-D"], check=True)

        # Prepare full data packet
        return jsonify({
            'name': name,
            'chembl_id': data.get('molecule_chembl_id'),
            'synonyms': synonyms_str,
            'formula': props.get('full_molformula', 'N/A'),
            'weight': f"{float(props.get('full_mwt')):.2f}" if props.get('full_mwt') else 'N/A',
            'type': str(data.get('molecule_type', 'N/A')).capitalize(),
            'smiles': structs.get('canonical_smiles', smiles),
            'inchi': structs.get('standard_inchi', 'N/A'),
            'inchikey': structs.get('standard_inchi_key', 'N/A'),
            'alogp': props.get('alogp', 'N/A'),
            'hba': props.get('hba', 'N/A'),
            'hbd': props.get('hbd', 'N/A'),
            'psa': props.get('psa', 'N/A'),
            'heavy_atoms': props.get('heavy_atoms', 'N/A'),
            'ro5_violations': props.get('num_ro5_violations', 'N/A'),
            'image_url': '/static/mol.png'
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
