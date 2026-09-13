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
    papers: list[ResearchPaper] = Field(default_factory=list)


class DrugInfo(BaseModel):

    drug_name: str


class ChemicalInformation(BaseModel):

    pubchem: Optional[PubChemData] = None


class DevelopmentInformation(BaseModel):

    chembl: Optional[ChEMBLData] = None


class ResearchPapers(BaseModel):

    pubmed: Optional[ResearchInformation] = None


class DrugResponse(BaseModel):

    drug: DrugInfo

    chemical_information: ChemicalInformation

    development_information: DevelopmentInformation

    research_papers: ResearchPapers