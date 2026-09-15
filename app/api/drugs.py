from fastapi import APIRouter, HTTPException

from app.services.pubchem_services import get_data_from_pubchem

from app.services.chembl_services import (
    get_data_from_chembl,
    get_targets_from_chembl,
    get_bioactivity_from_chembl,
    get_target_details_from_chembl
)

from app.services.pubmed_services import (
    get_research_from_pubmed,
    get_adverse_effect_research_from_pubmed
)

from app.models.drug import DrugResponse


router = APIRouter()


@router.get(
    "/{drug_name}",
    response_model=DrugResponse
)
def get_drug(drug_name: str):

    # PubChem
    pubchem_data = get_data_from_pubchem(drug_name)

    # ChEMBL
    chembl_data = get_data_from_chembl(drug_name)

    # PubMed - General research
    research_data = get_research_from_pubmed(
        drug_name
    )

    # PubMed - Adverse effects
    adverse_effect_data = get_adverse_effect_research_from_pubmed(
        drug_name
    )

    # Biological information
    biological_data = []

    # Target details
    target_details_data = []

    # Bioactivity
    bioactivity_data = []

    if chembl_data and chembl_data.get("chembl_id"):

        chembl_id = chembl_data.get("chembl_id")

        # Targets
        biological_data = get_targets_from_chembl(
            chembl_id
        )

        # Bioactivity
        bioactivity_data = get_bioactivity_from_chembl(
            chembl_id
        )

        # Target details
        for target in biological_data:

            target_id = target.get(
                "target_chembl_id"
            )

            if target_id:

                target_details = get_target_details_from_chembl(
                    target_id
                )

                if target_details:
                    target_details_data.append(
                        target_details
                    )

    # Drug not found
    if (
        pubchem_data is None
        and chembl_data is None
        and research_data is None
    ):
        raise HTTPException(
            status_code=404,
            detail="Drug not found"
        )

    return {

        "drug": {
            "drug_name": drug_name
        },

        "chemical_information": {
            "pubchem": pubchem_data
        },

        "development_information": {
            "chembl": chembl_data
        },

        "biological_information": {

            "targets": biological_data,

            "target_details": target_details_data,

            "bioactivity": bioactivity_data
        },

        "research_papers": {

            "pubmed": research_data,

            "adverse_effects": adverse_effect_data
        }
    }