import re
from flask import Flask, render_template, request
from chembl_webresource_client.new_client import new_client

app = Flask(__name__)

# Filter to handle chemical subscripts in HTML
@app.template_filter('subscript')
def subscript_filter(formula):
    if not formula or formula == 'N/A':
        return 'N/A'
    return re.sub(r'(\d+)', r'<sub>\1</sub>', str(formula))

@app.route("/", methods=["GET", "POST"])
def index():
    compound = None
    error = None

    if request.method == "POST":
        smiles = request.form.get("smiles", "").strip()
        if not smiles:
            error = "Please enter a SMILES string."
        else:
            try:
                molecule_client = new_client.molecule
                res = molecule_client.filter(molecule_structures__canonical_smiles=smiles)
                
                if not res:
                    error = "No compound found for this SMILES."
                else:
                    data = res[0]
                    props = data.get('molecule_properties') or {}
                    structs = data.get('molecule_structures') or {}

                    # Name and Synonyms logic
                    raw_name = data.get('pref_name')
                    name = raw_name.title() if raw_name else 'N/A'
                    
                    synonyms_list = data.get('molecule_synonyms') or []
                    syn_names = [(s.get('synonyms') or s.get('molecule_synonym', '')).title() for s in synonyms_list if s]
                    synonyms_str = (', '.join(syn_names[:3]) + "...") if len(syn_names) > 3 else (', '.join(syn_names) if syn_names else 'N/A')

                    weight_raw = props.get('full_mwt')
                    weight = f"{float(weight_raw):.2f}" if weight_raw else 'N/A'

                    compound = {
                        'chembl_id': data.get('molecule_chembl_id'),
                        'name': name,
                        'synonyms': synonyms_str,
                        'formula': props.get('full_molformula', 'N/A'),
                        'weight': weight,
                        'type': str(data.get('molecule_type', 'N/A')).capitalize(),
                        'smiles': structs.get('canonical_smiles', smiles),
                        'inchi': structs.get('standard_inchi', 'N/A'),
                        'inchikey': structs.get('standard_inchi_key', 'N/A'),
                        'alogp': props.get('alogp', 'N/A'),
                        'hba': props.get('hba', 'N/A'),
                        'hbd': props.get('hbd', 'N/A'),
                        'psa': props.get('psa', 'N/A'),
                        'heavy_atoms': props.get('heavy_atoms', 'N/A'),
                        'ro5_violations': props.get('num_ro5_violations', 'N/A')
                    }
            except Exception as e:
                error = f"Error: {str(e)}"

    return render_template("index.html", compound=compound, error=error)

if __name__ == "__main__":
    app.run(debug=True)