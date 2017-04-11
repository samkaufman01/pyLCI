#!/bin/bash
pyreverse -o png -p apps -my apps/ 
pyreverse -o png -p helpers -my helpers/
pyreverse -o png -p input -my input/
pyreverse -o png -p output -my output/
pyreverse -o png -p ui -my ui/ 
pyreverse -o png -p utils -my utils/ 
pyreverse -o png -p combined -my apps/ helpers/ input/ output/ ui/ utils/
mkdir docs/uml_diagrams/
mv classes_*.png docs/uml_diagrams/
mv packages_*.png docs/uml_diagrams/


