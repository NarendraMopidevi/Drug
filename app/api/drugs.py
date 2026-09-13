from fastapi import APIRouter, HTTPException

from app.services.pubchem_services import get_data_from_pubchem
# chemical information
from app.services.chembl_services import get_data_from_chembl
# development information
from app.services.pubmed_services import get_research_from_pubmed
# research papers informatio

router = APIRouter()

@router.get("/{drug_name}")

def get_drug(drug_name :str):
    pubchem_drug_data = get_data_from_pubchem(drug_name)
    chembl_drug_data = get_data_from_chembl(drug_name)
    pubmed_research_data = get_research_from_pubmed(drug_name)
    if pubchem_drug_data is None and chembl_drug_data is None:
        raise HTTPException(
            status_code = 404,
            details = "Drug not foudn in PubChem"
        )
    return{
        "drug": {
            "drug_name" : drug_name
        },
        "chemical_information": {
            "pubchem" : pubchem_drug_data,
        },
        "development_information": {
            "chembal" : chembl_drug_data
        },
        "research_papers" : {
            "pubmed" : pubmed_research_data
        }
    }
