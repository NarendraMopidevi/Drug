import requests


def get_data_from_pubchem(drug_name: str):

    url = (
        "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/"
        f"name/{drug_name}/property/"
        "Title,MolecularFormula,MolecularWeight,ConnectivitySMILES/JSON"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    properties = data["PropertyTable"]["Properties"][0]

    return {
        "name": properties.get("Title"),
        "molecular_formula": properties.get("MolecularFormula"),
        "molecular_weight": properties.get("MolecularWeight"),
        "canonical_smiles": properties.get("ConnectivitySMILES"),
        "isomeric_smiles": properties.get("SMILES"),
        "cid": properties.get("CID")
    }
