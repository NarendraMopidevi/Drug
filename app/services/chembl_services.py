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


def get_targets_from_chembl(chembl_id: str):

    url = (
        "https://www.ebi.ac.uk/chembl/api/data/"
        f"mechanism.json?molecule_chembl_id={chembl_id}"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return []

    data = response.json()

    mechanisms = data.get("mechanisms", [])

    targets = []

    for mechanism in mechanisms:
        targets.append({
            "target_chembl_id": mechanism.get("target_chembl_id"),
            "mechanism_of_action": mechanism.get("mechanism_of_action"),
            "action_type": mechanism.get("action_type")
        })

    return targets


def get_bioactivity_from_chembl(chembl_id: str):

    url = (
        "https://www.ebi.ac.uk/chembl/api/data/"
        f"activity.json?molecule_chembl_id={chembl_id}"
        "&limit=20"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return []

    data = response.json()

    activities = data.get("activities", [])

    bioactivity = []

    for activity in activities:
        bioactivity.append({
            "activity_id": activity.get("activity_id"),
            "target_chembl_id": activity.get("target_chembl_id"),
            "assay_chembl_id": activity.get("assay_chembl_id"),
            "standard_type": activity.get("standard_type"),
            "standard_value": activity.get("standard_value"),
            "standard_units": activity.get("standard_units"),
            "activity_comment": activity.get("activity_comment")
        })

    return bioactivity

def get_target_details_from_chembl(target_chembl_id: str):

    url = (
        "https://www.ebi.ac.uk/chembl/api/data/"
        f"target/{target_chembl_id}.json"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    return {
        "target_chembl_id": data.get("target_chembl_id"),
        "target_type": data.get("target_type"),
        "pref_name": data.get("pref_name"),
        "organism": data.get("organism")
    }