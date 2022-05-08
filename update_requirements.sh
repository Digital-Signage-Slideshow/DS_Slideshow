echo "Sed-ing requirements.txt" &&
pip freeze | sed 's/==/~=/g' >requirements.txt &&
echo "Checking for upgrades on requirements.txt" &&
pip install --upgrade -r requirements.txt &&
echo "Freezing requirements.txt" &&
pip freeze >requirements.txt &&
echo "Done" &&
exit 0
