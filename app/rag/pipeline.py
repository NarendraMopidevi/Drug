from app.api.drugs import get_drug

from app.rag.document_builder import build_drug_documents

from app.rag.retriever import (
    create_vector_storage,
    search_documents
)


def run_rag(
    drug_name: str,
    query: str,
    k: int = 3
):

    # Step 1: Get drug data
    drug_data = get_drug(drug_name)

    # Step 2: Convert drug data into LangChain documents
    documents = build_drug_documents(
        drug_data
    )

    # Step 3: Create FAISS vector storage
    vector_storage = create_vector_storage(
        documents
    )

    # Step 4: Search for relevant documents
    retrieved_documents = search_documents(
        vector_storage,
        query=query,
        k=k
    )

    # Step 5: Build context from retrieved documents
    context = "\n\n".join(
        document.page_content
        for document in retrieved_documents
    )

    # Step 6: Return context
    return context


# Test
if __name__ == "__main__":

    drug_name = "Aspirin"

    query = "What chemical formula of aspirin?"

    context = run_rag(
        drug_name,
        query,
        k=3
    )

    print("\nRetrieved Context:\n")

    print(context)