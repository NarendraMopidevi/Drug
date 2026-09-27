# # import requests


# # def get_data_from_pubchem(drug_name: str):

# #     url = (
# #         "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/"
# #         f"name/{drug_name}/property/"
# #         "Title,MolecularFormula,MolecularWeight,"
# #         "ConnectivitySMILES,SMILES/JSON"
# #     )

# #     response = requests.get(url)

# #     print("URL:", url)
# #     print("Status Code:", response.status_code)
# #     print("Response:", response.text)

# #     if response.status_code != 200:
# #         return None

# #     data = response.json()

# #     properties = data["PropertyTable"]["Properties"][0]

# #     return {
# #         "name": properties.get("Title"),
# #         "molecular_formula": properties.get("MolecularFormula"),
# #         "molecular_weight": properties.get("MolecularWeight"),
# #         "canonical_smiles": properties.get("ConnectivitySMILES"),
# #         "isomeric_smiles": properties.get("SMILES"),
# #         "cid": properties.get("CID")
# #     }
# import requests


# def get_data_from_pubchem(drug_name: str):

#     url = (
#         "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/"
#         f"name/{drug_name}/property/"
#         "Title,MolecularFormula,MolecularWeight,"
#         "ConnectivitySMILES,SMILES/JSON"
#     )

#     try:
#         response = requests.get(url, timeout=15)

#         print("URL:", url)
#         print("Status Code:", response.status_code)
#         print("Response:", response.text)

#         if response.status_code != 200:
#             print("PubChem request failed.")
#             return None

#         data = response.json()

#         properties = data["PropertyTable"]["Properties"][0]

#         return {
#             "name": properties.get("Title"),
#             "molecular_formula": properties.get("MolecularFormula"),
#             "molecular_weight": properties.get("MolecularWeight"),
#             "canonical_smiles": properties.get("ConnectivitySMILES"),
#             "isomeric_smiles": properties.get("SMILES"),
#             "cid": properties.get("CID")
#         }

#     except requests.exceptions.ConnectionError as e:
#         print("Could not connect to PubChem.")
#         print("Network/DNS error:", e)
#         return None

#     except requests.exceptions.Timeout:
#         print("PubChem request timed out.")
#         return None

#     except requests.exceptions.RequestException as e:
#         print("PubChem request error:", e)
#         return None

#     except (KeyError, IndexError, ValueError) as e:
#         print("Unexpected PubChem response:", e)
#         return None

import requests


# Temporary hardcoded chemical information
HARDCODED_DRUGS = {
    "aspirin": {
        "name": "Aspirin",
        "molecular_formula": "C9H8O4",
        "molecular_weight": 180.16,
        "canonical_smiles": "CC(=O)OC1=CC=CC=C1C(=O)O",
        "isomeric_smiles": "CC(=O)OC1=CC=CC=C1C(=O)O",
        "cid": 2244
    },

    "paracetamol": {
        "name": "Paracetamol",
        "molecular_formula": "C8H9NO2",
        "molecular_weight": 151.16,
        "canonical_smiles": "CC(=O)NC1=CC=C(C=C1)O",
        "isomeric_smiles": "CC(=O)NC1=CC=C(C=C1)O",
        "cid": 1983
    },

    "ibuprofen": {
        "name": "Ibuprofen",
        "molecular_formula": "C13H18O2",
        "molecular_weight": 206.28,
        "canonical_smiles": "CC(C)CC1=CC=C(C=C1)[COOH](C)C(=O)O",
        "isomeric_smiles": "CC(C)CC1=CC=C(C=C1)[COOH](C)C(=O)O",
        "cid": 3672
    },

    "metformin": {
        "name": "Metformin",
        "molecular_formula": "C4H11N5",
        "molecular_weight": 129.16,
        "canonical_smiles": "CN(C)C(=N)NC(=N)N",
        "isomeric_smiles": "CN(C)C(=N)NC(=N)N",
        "cid": 4091
    },

    "amoxicillin": {
        "name": "Amoxicillin",
        "molecular_formula": "C16H19N3O5S",
        "molecular_weight": 365.40,
        "canonical_smiles": "CC1(C(N2C(S1)C(C2=O)NC(=O)CO)C)C3=CC=C(C=C3)N",
        "isomeric_smiles": "CC1(C(N2C(S1)C(C2=O)NC(=O)CO)C)C3=CC=C(C=C3)N",
        "cid": 3365
    }
}


def get_data_from_pubchem(drug_name: str):

    drug_name = drug_name.lower().strip()

    # Use hardcoded data first
    if drug_name in HARDCODED_DRUGS:
        print(f"Using hardcoded data for: {drug_name}")

        return HARDCODED_DRUGS[drug_name]

    # PubChem API for other drugs
    url = (
        "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/"
        f"name/{drug_name}/property/"
        "Title,MolecularFormula,MolecularWeight,"
        "ConnectivitySMILES,SMILES/JSON"
    )

    try:
        response = requests.get(url, timeout=15)

        print("URL:", url)
        print("Status Code:", response.status_code)

        if response.status_code != 200:
            print("PubChem request failed.")
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

    except requests.exceptions.ConnectionError as e:
        print("Could not connect to PubChem.")
        print("Network/DNS error:", e)
        return None

    except requests.exceptions.Timeout:
        print("PubChem request timed out.")
        return None

    except requests.exceptions.RequestException as e:
        print("PubChem request error:", e)
        return None

    except (KeyError, IndexError, ValueError) as e:
        print("Unexpected PubChem response:", e)
        return None