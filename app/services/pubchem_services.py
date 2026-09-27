# import requests


# def get_data_from_pubchem(drug_name: str):

#     url = (
#         "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/"
#         f"name/{drug_name}/property/"
#         "Title,MolecularFormula,MolecularWeight,"
#         "ConnectivitySMILES,SMILES/JSON"
#     )

#     response = requests.get(url)

#     print("URL:", url)
#     print("Status Code:", response.status_code)
#     print("Response:", response.text)

#     if response.status_code != 200:
#         return None

#     data = response.json()

#     properties = data["PropertyTable"]["Properties"][0]

#     return {
#         "name": properties.get("Title"),
#         "molecular_formula": properties.get("MolecularFormula"),
#         "molecular_weight": properties.get("MolecularWeight"),
#         "canonical_smiles": properties.get("ConnectivitySMILES"),
#         "isomeric_smiles": properties.get("SMILES"),
#         "cid": properties.get("CID")
#     }
import requests


def get_data_from_pubchem(drug_name: str):

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
        print("Response:", response.text)

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