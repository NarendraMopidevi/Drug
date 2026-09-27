import streamlit as st

from app.api.drugs import get_drug
from app.rag.pipeline import run_rag
from app.services.llm.gemini import GeminiProvider


# -----------------------------------
# Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="Drug Discovery Copilot",
    page_icon="💊",
    layout="wide"
)


# -----------------------------------
# Initialize LLM
# -----------------------------------

@st.cache_resource
def get_llm():
    return GeminiProvider()


llm = get_llm()


# -----------------------------------
# Title
# -----------------------------------

st.title("💊 Drug Discovery & Drug Information Copilot")

st.write(
    "Enter a drug name to retrieve scientific information "
    "and ask questions using RAG and an LLM."
)


# -----------------------------------
# Project Warning
# -----------------------------------

st.warning(
    "⚠️ Research & Educational Prototype: "
    "This application is not a medical diagnosis or treatment system. "
    "Information should be verified using authoritative scientific sources "
    "and qualified healthcare or research professionals."
)


# -----------------------------------
# Initialize Chat History
# -----------------------------------

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []


# -----------------------------------
# Drug Search
# -----------------------------------

st.header("1. Search Drug")

drug_name = st.text_input(
    "Enter drug name",
    placeholder="Example: Aspirin"
)

search_button = st.button(
    "Search Drug"
)


# -----------------------------------
# Retrieve Drug Information
# -----------------------------------

if search_button and drug_name:

    with st.spinner("Retrieving drug information..."):

        try:

            drug_data = get_drug(drug_name)

            st.session_state["drug_data"] = drug_data
            st.session_state["drug_name"] = drug_name

            # Optional: clear previous chat when a new drug is selected
            st.session_state["chat_history"] = []

            st.success(
                f"Information retrieved for {drug_name}"
            )

        except Exception as e:

            st.error(
                f"Error retrieving drug information: {e}"
            )


# -----------------------------------
# Display Retrieved Information
# -----------------------------------

if "drug_data" in st.session_state:

    drug_data = st.session_state["drug_data"]

    st.header("2. Retrieved Drug Information")


    # -----------------------------------
    # Drug
    # -----------------------------------

    drug = drug_data.get(
        "drug",
        {}
    )

    st.subheader("Drug")

    st.write(
        f"**Name:** {drug.get('drug_name')}"
    )


    # -----------------------------------
    # PubChem
    # -----------------------------------

    chemical = drug_data.get(
        "chemical_information",
        {}
    )

    pubchem = chemical.get(
        "pubchem"
    )

    if pubchem:

        st.subheader("🧪 Chemical Information")

        col1, col2 = st.columns(2)

        with col1:

            st.write(
                f"**Name:** {pubchem.get('name')}"
            )

            st.write(
                f"**Molecular Formula:** "
                f"{pubchem.get('molecular_formula')}"
            )

            st.write(
                f"**Molecular Weight:** "
                f"{pubchem.get('molecular_weight')}"
            )

        with col2:

            st.write(
                f"**PubChem CID:** "
                f"{pubchem.get('cid')}"
            )

            st.write(
                f"**Canonical SMILES:** "
                f"{pubchem.get('canonical_smiles')}"
            )

            st.write(
                f"**Isomeric SMILES:** "
                f"{pubchem.get('isomeric_smiles')}"
            )


    # -----------------------------------
    # ChEMBL
    # -----------------------------------

    development = drug_data.get(
        "development_information",
        {}
    )

    chembl = development.get(
        "chembl"
    )

    if chembl:

        st.subheader("🔬 ChEMBL Information")

        col1, col2 = st.columns(2)

        with col1:

            st.write(
                f"**ChEMBL ID:** "
                f"{chembl.get('chembl_id')}"
            )

            st.write(
                f"**Preferred Name:** "
                f"{chembl.get('pref_name')}"
            )

            st.write(
                f"**Molecule Type:** "
                f"{chembl.get('molecule_type')}"
            )

        with col2:

            st.write(
                f"**Maximum Phase:** "
                f"{chembl.get('max_phase')}"
            )

            st.write(
                f"**First Approval:** "
                f"{chembl.get('first_approval')}"
            )

            st.write(
                f"**Black Box Warning:** "
                f"{chembl.get('black_box_warning')}"
            )


    # -----------------------------------
    # Biological Information
    # -----------------------------------

    biological = drug_data.get(
        "biological_information",
        {}
    )


    # -----------------------------------
    # Targets
    # -----------------------------------

    targets = biological.get(
        "targets",
        []
    )

    if targets:

        st.subheader("🎯 Biological Targets")

        for target in targets:

            with st.expander(
                target.get(
                    "target_chembl_id",
                    "Target"
                )
            ):

                st.write(
                    f"**Target ID:** "
                    f"{target.get('target_chembl_id')}"
                )

                st.write(
                    f"**Mechanism of Action:** "
                    f"{target.get('mechanism_of_action')}"
                )

                st.write(
                    f"**Action Type:** "
                    f"{target.get('action_type')}"
                )


    # -----------------------------------
    # Target Details
    # -----------------------------------

    target_details = biological.get(
        "target_details",
        []
    )

    if target_details:

        st.subheader("🧬 Target Details")

        for target in target_details:

            with st.expander(
                target.get(
                    "pref_name",
                    "Target Details"
                )
            ):

                st.write(
                    f"**Target ID:** "
                    f"{target.get('target_chembl_id')}"
                )

                st.write(
                    f"**Target Type:** "
                    f"{target.get('target_type')}"
                )

                st.write(
                    f"**Target Name:** "
                    f"{target.get('pref_name')}"
                )

                st.write(
                    f"**Organism:** "
                    f"{target.get('organism')}"
                )


    # -----------------------------------
    # Bioactivity
    # -----------------------------------

    bioactivity = biological.get(
        "bioactivity",
        []
    )

    if bioactivity:

        st.subheader("🧪 Bioactivity")

        for activity in bioactivity:

            with st.expander(
                f"Activity {activity.get('activity_id')}"
            ):

                st.write(
                    f"**Target:** "
                    f"{activity.get('target_chembl_id')}"
                )

                st.write(
                    f"**Assay:** "
                    f"{activity.get('assay_chembl_id')}"
                )

                st.write(
                    f"**Standard Type:** "
                    f"{activity.get('standard_type')}"
                )

                st.write(
                    f"**Value:** "
                    f"{activity.get('standard_value')}"
                )

                st.write(
                    f"**Units:** "
                    f"{activity.get('standard_units')}"
                )

                st.write(
                    f"**Comment:** "
                    f"{activity.get('activity_comment')}"
                )


    # -----------------------------------
    # PubMed Research
    # -----------------------------------

    research_papers = drug_data.get(
        "research_papers",
        {}
    )

    pubmed = research_papers.get(
        "pubmed"
    )

    if pubmed:

        st.subheader("📚 Research Papers")

        st.write(
            f"**Total Results:** "
            f"{pubmed.get('total_results')}"
        )

        for paper in pubmed.get(
            "papers",
            []
        ):

            with st.expander(
                paper.get(
                    "title",
                    "Research Paper"
                )
            ):

                st.write(
                    f"**PMID:** "
                    f"{paper.get('pmid')}"
                )

                st.write(
                    f"**Authors:** "
                    f"{', '.join(paper.get('authors', []))}"
                )

                st.write(
                    f"**Journal:** "
                    f"{paper.get('journal')}"
                )

                st.write(
                    f"**Year:** "
                    f"{paper.get('publication_year')}"
                )

                st.write(
                    f"**DOI:** "
                    f"{paper.get('doi')}"
                )

                st.write(
                    "**Abstract:**"
                )

                st.write(
                    paper.get(
                        "abstract"
                    )
                )


    # -----------------------------------
    # Adverse Effects Research
    # -----------------------------------

    adverse_effects = research_papers.get(
        "adverse_effects"
    )

    if adverse_effects:

        st.subheader("⚠️ Adverse Effect Research")

        st.write(
            f"**Total Results:** "
            f"{adverse_effects.get('total_results')}"
        )

        for paper in adverse_effects.get(
            "papers",
            []
        ):

            with st.expander(
                paper.get(
                    "title",
                    "Adverse Effect Paper"
                )
            ):

                st.write(
                    f"**PMID:** "
                    f"{paper.get('pmid')}"
                )

                st.write(
                    paper.get(
                        "abstract"
                    )
                )


    # -----------------------------------
    # Question Answering
    # -----------------------------------

    st.header("3. Ask Questions")

    question = st.text_input(
        "Ask a question about this drug",
        placeholder="Example: What is the mechanism of action?"
    )

    ask_button = st.button(
        "Ask Question"
    )


    # -----------------------------------
    # Generate Answer
    # -----------------------------------

    if ask_button and question:

        drug_name = st.session_state[
            "drug_name"
        ]

        with st.spinner(
            "Searching scientific information..."
        ):

            try:

                # Retrieve relevant context
                context = run_rag(
                    drug_name,
                    question,
                    k=3
                )


                # -----------------------------------
                # Guardrailed Prompt
                # -----------------------------------

                prompt = f""" You are Drug Copilot, a scientific drug information assistant. Answer the user's question using the retrieved context below. You can also use your general scientific and pharmaceutical knowledge. Use the retrieved context when it contains relevant drug-specific information. Use your own knowledge to explain concepts, definitions, mechanisms, terminology, and general scientific information. Do not make up specific experimental results, numerical values, citations, drug properties, targets, or database records. If the context does not contain enough information for a specific drug-related answer, use your general knowledge where appropriate. If the information cannot be answered reliably, say that the available information is insufficient. Only answer questions related to drugs, pharmaceuticals, pharmacology, drug discovery, drug development, medicinal chemistry, bioactivity, drug targets, mechanisms of action, adverse effects, clinical research, and related life-science topics. If the user asks about something unrelated to drugs, pharmaceuticals, or the above scientific topics, politely say that you can only help with drug and pharmaceutical-related questions. Retrieved Context: {context} User Question: {question} Provide a clear, natural, and concise answer. """

                # Generate Gemini response
                answer = llm.generate(
                    prompt
                )


                # -----------------------------------
                # Save Chat History
                # -----------------------------------

                st.session_state["chat_history"].append({
                    "drug_name": drug_name,
                    "question": question,
                    "answer": answer
                })


                # -----------------------------------
                # Display Current Answer
                # -----------------------------------

                st.subheader(
                    "🤖 Drug Copilot"
                )

                st.write(
                    answer
                )


            except Exception as e:

                st.error(
                    f"Error generating answer: {e}"
                )


    # -----------------------------------
    # Chat History
    # -----------------------------------

    if st.session_state["chat_history"]:

        st.header("💬 Chat History")

        for index, chat in enumerate(
            st.session_state["chat_history"],
            start=1
        ):

            with st.expander(
                f"Conversation {index} — {chat['drug_name']}"
            ):

                st.markdown(
                    f"**👤 You:** {chat['question']}"
                )

                st.markdown(
                    f"**🤖 Drug Copilot:** {chat['answer']}"
                )


        # -----------------------------------
        # Clear Chat History
        # -----------------------------------

        if st.button(
            "🗑️ Clear Chat History"
        ):

            st.session_state["chat_history"] = []

            st.rerun()