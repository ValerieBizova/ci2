# Assignment A10 - Automated Testing with Playwright

## overview:

This project is an extension of the chemical web server. It implements automated UI testing to verify the full pipeline: SMILES input, remote API data retrieval, and local 3D rendering (Open Babel + POV-Ray).


## necessary to run:

WSL (Ubuntu recommended) on Windows

Python 3.12

Open Babel (obabel)

POV-Ray (povray)

Playwright & Pytest (for automated testing)


## cloning my GitHub repository - Git Bash:

$ git clone https://github.com/ValerieBizova/ci2.git

$ cd ci2/A10


## moving the project to the Linux Environment - Windows WSL:

$ mkdir -p ~/ci2

$ cp -r /mnt/c/Users/BizovaV/ci2/A10 ~/ci2/

$ cd ~/ci2/A10


## creating a virtual environment:

$ python3 -m venv venv_wsl

$ source venv_wsl/bin/activate


## installing required Python packages:

$ pip install -r requirements.txt

$ pip install pytest-playwright

$ playwright install

-> there may be many libraries missing, necessary to install them:

$ sudo apt install -y \
	...


## installing required Linux applications (WSL/Ubuntu):

$ sudo apt update

$ sudo apt install openbabel povray


## recording with Codegen:

1st WSL window:

$ python app.py


2nd WSL window (also necessary to be in virtual environment and have all the packages installed):

$ playwright codegen http://127.0.0.1:5000

1. Enter a SMILES string in the input field (e.g. CCO)
2. Click the "Search" button
3. Save the code from the Playwright Inspector Window:

$ cat > tests/test_web.py


## editing the code to make it more robust:

- Parametrization: Added @pytest.mark.parametrize to test multiple molecules (Ethanol, Benzene, Aspirin) in one execution.

- Dynamic Verification: Implemented re.compile assertions to verify that ChEMBL IDs and names appear correctly, even if naming varies (e.g., "Alcohol" vs "Ethanol").

- Timing Controls: Increased the expect timeout to 30 seconds to ensure the test waits for the backend POV-Ray rendering process to complete before checking for the image.


## running the pytest:

1st WSL window:

$ python app.py


2nd WSL window:

$ pytest tests/test_web.py

-> if successful:

tests/test_web.py ...                                                                                                       [100%]

======================================================== 3 passed in Xs ========================================================


## pushing A10 folder into my GitHub repository:

$ git add A10

$ git commit -m "Add assignment A10: Automated Testing with Playwright"

$ git push origin main
