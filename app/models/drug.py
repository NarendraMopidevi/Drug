from pydantic import BaseModel, Field
from typing import Optional


class PubChemData(BaseModel):

    name: Optional[str] = None
    molecular_formula: Optional[str] = None
    molecular_weight: Optional[str] = None
    canonical_smiles: Optional[str] = None
    isomeric_smiles: Optional[str] = None
    cid: Optional[int] = None


class ChEMBLData(BaseModel):

    chembl_id: Optional[str] = None
    pref_name: Optional[str] = None
    molecule_type: Optional[str] = None
    max_phase: Optional[float] = None
    first_approval: Optional[int] = None
    black_box_warning: Optional[int] = None


class ChEMBLTarget(BaseModel):

    target_chembl_id: Optional[str] = None
    mechanism_of_action: Optional[str] = None
    action_type: Optional[str] = None


class ChEMBLBioactivity(BaseModel):

    activity_id: Optional[int] = None
    target_chembl_id: Optional[str] = None
    assay_chembl_id: Optional[str] = None
    standard_type: Optional[str] = None
    standard_value: Optional[str] = None
    standard_units: Optional[str] = None
    activity_comment: Optional[str] = None


class ChEMBLTargetDetails(BaseModel):

    target_chembl_id: Optional[str] = None
    target_type: Optional[str] = None
    pref_name: Optional[str] = None
    organism: Optional[str] = None


class ResearchPaper(BaseModel):

    pmid: Optional[str] = None
    title: Optional[str] = None
    authors: list[str] = Field(default_factory=list)
    journal: Optional[str] = None
    publication_year: Optional[str] = None
    abstract: Optional[str] = None
    doi: Optional[str] = None


class ResearchInformation(BaseModel):

    total_results: Optional[str] = None
    papers: list[ResearchPaper] = Field(
        default_factory=list
    )


class AdverseEffectResearch(BaseModel):

    total_results: Optional[str] = None
    papers: list[ResearchPaper] = Field(
        default_factory=list
    )


class DrugInfo(BaseModel):

    drug_name: str


class ChemicalInformation(BaseModel):

    pubchem: Optional[PubChemData] = None


class DevelopmentInformation(BaseModel):

    chembl: Optional[ChEMBLData] = None


class BiologicalInformation(BaseModel):

    targets: list[ChEMBLTarget] = Field(
        default_factory=list
    )

    target_details: list[ChEMBLTargetDetails] = Field(
        default_factory=list
    )

    bioactivity: list[ChEMBLBioactivity] = Field(
        default_factory=list
    )


class ResearchPapers(BaseModel):

    pubmed: Optional[ResearchInformation] = None

    adverse_effects: Optional[AdverseEffectResearch] = None


class DrugResponse(BaseModel):

    drug: DrugInfo

    chemical_information: ChemicalInformation

    development_information: DevelopmentInformation

    biological_information: BiologicalInformation

    research_papers: ResearchPapers