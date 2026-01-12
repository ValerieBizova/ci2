import re
import pytest
from playwright.sync_api import Page, expect

# Requirement 3 & 4: Refined and robust test suite
@pytest.mark.parametrize("smiles, name_regex", [
    ("CCO", "Alcohol|Ethanol"),
    ("c1ccccc1", "Benzene"),
    ("CC(=O)Oc1ccccc1C(=O)O", "Aspirin|Acetylsalicylic")
])
def test_molecule_pipeline(page: Page, smiles, name_regex):
    # 1. Open the application (Recorded by codegen)
    page.goto("http://127.0.0.1:5000/")

    # 2. Interact with the SMILES input (Uses the role-based selector found by codegen)
    molecule_input = page.get_by_role("textbox", name="Enter SMILES string (e.g., CCO)")
    molecule_input.fill(smiles)

    # 3. Submit the search (Recorded by codegen)
    page.get_by_role("button", name="Search").click()

    # 4. ROBUSTNESS: Wait for the result area to become visible
    # We increased the timeout to 30s to allow for POV-Ray rendering
    result_wrapper = page.locator("#resultWrapper")
    expect(result_wrapper).to_be_visible(timeout=30000)

    # 5. VERIFICATION: Verify ChEMBL data using Regex
    # This ensures the API returned a valid molecule
    expect(page.locator("#resID")).to_contain_text(re.compile(r"CHEMBL\d+"))
    expect(page.locator("#resName")).to_contain_text(re.compile(name_regex, re.IGNORECASE))

    # 6. VERIFICATION: Verify 3D image display
    # This proves POV-Ray successfully generated the PNG
    img_3d = page.locator("#img3D")
    expect(img_3d).to_be_visible()
    expect(img_3d).to_have_attribute("src", re.compile(r"/static/mol.png"))

    print(f"\n✅ Successfully verified molecule: {smiles}")
