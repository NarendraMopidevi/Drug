from langchain_core.documents import Document


def build_drug_documents(drug_data: dict):

    documents = []

    drug_name = drug_data.get(
        "drug", {}
    ).get(
        "drug_name",
        "Unknown Drug"
    )

    # --------------------------------
    # PubChem
    # --------------------------------

    pubchem = drug_data.get(
        "chemical_information",
        {}
    ).get(
        "pubchem"
    )

    if pubchem:

        content = f"""
Drug: {drug_name}

Source: PubChem

Chemical Information:
Name: {pubchem.get("name")}
Molecular Formula: {pubchem.get("molecular_formula")}
Molecular Weight: {pubchem.get("molecular_weight")}
Canonical SMILES: {pubchem.get("canonical_smiles")}
Isomeric SMILES: {pubchem.get("isomeric_smiles")}
PubChem CID: {pubchem.get("cid")}
"""

        documents.append(
            Document(
                page_content=content.strip(),
                metadata={
                    "source": "PubChem",
                    "drug_name": drug_name
                }
            )
        )

    # --------------------------------
    # ChEMBL - Drug Information
    # --------------------------------

    chembl = drug_data.get(
        "development_information",
        {}
    ).get(
        "chembl"
    )

    if chembl:

        content = f"""
Drug: {drug_name}

Source: ChEMBL

Drug Development Information:
ChEMBL ID: {chembl.get("chembl_id")}
Preferred Name: {chembl.get("pref_name")}
Molecule Type: {chembl.get("molecule_type")}
Maximum Phase: {chembl.get("max_phase")}
First Approval: {chembl.get("first_approval")}
Black Box Warning: {chembl.get("black_box_warning")}
"""

        documents.append(
            Document(
                page_content=content.strip(),
                metadata={
                    "source": "ChEMBL",
                    "drug_name": drug_name
                }
            )
        )

    # --------------------------------
    # ChEMBL - Targets
    # --------------------------------

    biological = drug_data.get(
        "biological_information",
        {}
    )

    targets = biological.get(
        "targets",
        []
    )

    for target in targets:

        content = f"""
Drug: {drug_name}

Source: ChEMBL

Biological Target:
Target ChEMBL ID: {target.get("target_chembl_id")}
Mechanism of Action: {target.get("mechanism_of_action")}
Action Type: {target.get("action_type")}
"""

        documents.append(
            Document(
                page_content=content.strip(),
                metadata={
                    "source": "ChEMBL",
                    "type": "target",
                    "drug_name": drug_name,
                    "target_chembl_id": target.get(
                        "target_chembl_id"
                    )
                }
            )
        )

    # --------------------------------
    # ChEMBL - Target Details
    # --------------------------------

    target_details = biological.get(
        "target_details",
        []
    )

    for target in target_details:

        content = f"""
Drug: {drug_name}

Source: ChEMBL

Target Details:
Target ChEMBL ID: {target.get("target_chembl_id")}
Target Type: {target.get("target_type")}
Target Name: {target.get("pref_name")}
Organism: {target.get("organism")}
"""

        documents.append(
            Document(
                page_content=content.strip(),
                metadata={
                    "source": "ChEMBL",
                    "type": "target_details",
                    "drug_name": drug_name,
                    "target_chembl_id": target.get(
                        "target_chembl_id"
                    )
                }
            )
        )

    # --------------------------------
    # ChEMBL - Bioactivity
    # --------------------------------

    bioactivity = biological.get(
        "bioactivity",
        []
    )

    for activity in bioactivity:

        content = f"""
Drug: {drug_name}

Source: ChEMBL

Bioactivity:
Activity ID: {activity.get("activity_id")}
Target ChEMBL ID: {activity.get("target_chembl_id")}
Assay ChEMBL ID: {activity.get("assay_chembl_id")}
Standard Type: {activity.get("standard_type")}
Standard Value: {activity.get("standard_value")}
Standard Units: {activity.get("standard_units")}
Activity Comment: {activity.get("activity_comment")}
"""

        documents.append(
            Document(
                page_content=content.strip(),
                metadata={
                    "source": "ChEMBL",
                    "type": "bioactivity",
                    "drug_name": drug_name,
                    "target_chembl_id": activity.get(
                        "target_chembl_id"
                    )
                }
            )
        )

    # --------------------------------
    # PubMed - General Research
    # --------------------------------

    research = drug_data.get(
        "research_papers",
        {}
    ).get(
        "pubmed"
    )

    if research:

        for paper in research.get(
            "papers",
            []
        ):

            content = f"""
Drug: {drug_name}

Source: PubMed

Research Paper:
PMID: {paper.get("pmid")}
Title: {paper.get("title")}
Authors: {", ".join(paper.get("authors", []))}
Journal: {paper.get("journal")}
Publication Year: {paper.get("publication_year")}
DOI: {paper.get("doi")}

Abstract:
{paper.get("abstract")}
"""

            documents.append(
                Document(
                    page_content=content.strip(),
                    metadata={
                        "source": "PubMed",
                        "type": "research",
                        "drug_name": drug_name,
                        "pmid": paper.get("pmid")
                    }
                )
            )

    # --------------------------------
    # PubMed - Adverse Effects
    # --------------------------------

    adverse_effects = drug_data.get(
        "research_papers",
        {}
    ).get(
        "adverse_effects"
    )

    if adverse_effects:

        for paper in adverse_effects.get(
            "papers",
            []
        ):

            content = f"""
Drug: {drug_name}

Source: PubMed

Adverse Effect Research:
PMID: {paper.get("pmid")}
Title: {paper.get("title")}

Abstract:
{paper.get("abstract")}
"""

            documents.append(
                Document(
                    page_content=content.strip(),
                    metadata={
                        "source": "PubMed",
                        "type": "adverse_effects",
                        "drug_name": drug_name,
                        "pmid": paper.get("pmid")
                    }
                )
            )

    return documents