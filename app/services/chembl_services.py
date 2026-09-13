import requests


def get_data_from_chembl(drug_name: str):

    url = (
        "https://www.ebi.ac.uk/chembl/api/data/"
        f"molecule/search.json?q={drug_name}"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    molecules = data.get("molecules", [])

    if not molecules:
        return None

    molecule = molecules[0]

    return {
    "chembl_id": molecule.get("molecule_chembl_id"),
    "pref_name": molecule.get("pref_name"),
    "molecule_type": molecule.get("molecule_type"),
    "max_phase": molecule.get("max_phase"),
    "first_approval": molecule.get("first_approval"),
    "black_box_warning": molecule.get("black_box_warning")
}