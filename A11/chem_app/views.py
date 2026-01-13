from django.shortcuts import render
from .models import SearchLog
from chembl_webresource_client.new_client import new_client
import os
import subprocess

# PAGE A: Home Page
def home(request):
    """Displays the welcome message and serves as the entry point."""
    return render(request, "home.html")

# PAGE B: ChEMBL Search
def chembl(request):
    """
    Fetches molecule data from ChEMBL.
    REQUIREMENT: Creates a record in the database for every SMILES received.
    """
    data = None
    if request.method == "POST":
        smiles = request.POST.get("smiles", "").strip()
        if smiles:
            # SAVE TO DATABASE: This satisfies the assignment requirement
            SearchLog.objects.create(smiles=smiles)
            
            # Fetch from ChEMBL (Logic transplanted from your A10 app.py)
            res = new_client.molecule.filter(molecule_structures__canonical_smiles=smiles)
            if res:
                mol = res[0]
                props = mol.get('molecule_properties') or {}
                structs = mol.get('molecule_structures') or {}
                
                # Name and Synonyms logic
                raw_name = mol.get('pref_name')
                name = raw_name.title() if raw_name else 'N/A'
                synonyms_list = mol.get('molecule_synonyms') or []
                syn_names = [s.get('synonyms', '').title() for s in synonyms_list if s]
                
                # Data packet for the HTML template
                data = {
                    'chembl_id': mol.get('molecule_chembl_id', 'N/A'),
                    'name': name,
                    'synonyms': ', '.join(syn_names[:3]) if syn_names else 'N/A',
                    'formula': props.get('full_molformula', 'N/A'),
                    'weight': props.get('full_mwt', 'N/A'),
                    'type': str(mol.get('molecule_type', 'N/A')).capitalize(),
                    'smiles': structs.get('canonical_smiles', smiles),
                    'inchi': structs.get('standard_inchi', 'N/A'),
                    'inchikey': structs.get('standard_inchi_key', 'N/A'),
                    'alogp': props.get('alogp', 'N/A'),
                    'hba': props.get('hba', 'N/A'),
                    'hbd': props.get('hbd', 'N/A'),
                    'psa': props.get('psa', 'N/A'),
                    'heavy_atoms': props.get('heavy_atoms', 'N/A'),
                    'ro5_violations': props.get('num_ro5_violations', 'N/A'),
                }
    return render(request, "chembl.html", {"data": data})

# PAGE C: POV-Ray 3D
def povray(request):
    """
    Generates a 3D image using OpenBabel and POV-Ray.
    Integrates the result as a Django static file.
    """
    image_url = None
    if request.method == "POST":
        smiles = request.POST.get("smiles", "").strip()
        if smiles:
            # Use absolute paths so Django can find the files reliably
            static_dir = os.path.join(os.getcwd(), 'static')
            os.makedirs(static_dir, exist_ok=True)
            
            pov_path = os.path.join(static_dir, "mol.pov")
            png_path = os.path.join(static_dir, "mol.png")
            
            # RUN EXTERNAL TOOLS: Logic transplanted from your A10 app.py
            try:
                # Step 1: Generate POV file with OpenBabel
                subprocess.run(["obabel", f"-:{smiles}", "-O", pov_path, "--gen3d"], check=True)
                
                # Step 2: Render PNG with POV-Ray (+L tells POV-Ray where to find .inc files)
                subprocess.run([
                    "povray", f"+I{pov_path}", f"+O{png_path}", 
                    "+W600", "+H400", "+A", f"+L{static_dir}", "-D"
                ], check=True)
                
                image_url = "/static/mol.png"
            except subprocess.CalledProcessError:
                # If POV-Ray fails, image_url remains None
                pass
            
    return render(request, "povray.html", {"image_url": image_url})
