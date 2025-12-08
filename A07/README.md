\# Assignment A07 - POV-Ray



\## cloning my GitHub repository:

$ git clone git@github.com:ValerieBizova/ci2.git

$ cd ci2



\## creating the SMILES file:

$ echo "CCO" > etoh.smi



\## converting SMILES file to POV-Ray format:

$ obabel etoh.smi -O etoh.pov --gen3D



\## editing etoh.pov file:

necessary to delete the final line mol\_0 - otherwise it will create a seventh ethanol in the middle of the haxagon



\## creating etoh6.pov in nano:

$ nano etoh6.pov

writing down the code



\## creating etoh6.png:

etoh6.pov is ready to be rendered by POV-Ray - will show six molecules of ethanol placed at the vertices of a regular hexagon

etoh.pov rendered by POV-Ray - will show empty file



\## pushing A07 folder into my GitHub repository:

$ git add A07

$ git commit -m "Add assignment A07"

$ git push

