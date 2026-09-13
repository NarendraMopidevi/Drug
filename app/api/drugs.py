from fastapi import APIRouter, HTTPException

from app.services.pubchem_services import get_data_from_pubchem
# chemical information
from app.services.chembl_services import get_data_from_chembl
# development information
from app.services.pubmed_services import get_research_from_pubmed
# research papers informatio

from app.models.drug import DrugResponse


router = APIRouter()


@router.get(
    "/{drug_name}",
    response_model=DrugResponse
)
def get_drug(drug_name: str):

    pubchem_data = get_data_from_pubchem(drug_name)

    chembl_data = get_data_from_chembl(drug_name)

    research_data = get_research_from_pubmed(drug_name)

    if (
        pubchem_data is None
        and chembl_data is None
        and research_data is None
    ):
        raise HTTPException(
            status_code=404,
            detail="Drug not found"
        )

    # return {
    #     "drug_name": drug_name,
    #     "pubchem": pubchem_data,
    #     "chembl": chembl_data,
    #     "research_information": research_data
    # }
    return{
        "drug": {
            "drug_name" : drug_name
        },
        "chemical_information": {
            "pubchem" : pubchem_data,
        },
        "development_information": {
            "chembl" : chembl_data
        },
        "research_papers" : {
            "pubmed" : research_data
        }
    }
