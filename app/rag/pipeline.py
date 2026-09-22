from app.api.drugs import get_drug

from app.rag.document_builder import build_drug_documents

from app.rag.chunker import chunk_documents

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

    print("\n==============================")
    print("STEP 1: GET DRUG DATA")
    print("==============================")

    drug_data = get_drug(drug_name)

    print("Drug data received successfully")


    # Step 2: Build documents

    print("\n==============================")
    print("STEP 2: BUILD DOCUMENTS")
    print("==============================")

    documents = build_drug_documents(
        drug_data
    )

    print(
        f"Number of documents: {len(documents)}"
    )


    # Step 3: Chunk documents

    print("\n==============================")
    print("STEP 3: CHUNK DOCUMENTS")
    print("==============================")

    chunked_documents = chunk_documents(
        documents
    )

    print(
        f"Number of chunks: {len(chunked_documents)}"
    )


    # Step 4: Create FAISS

    print("\n==============================")
    print("STEP 4: CREATE VECTOR STORAGE")
    print("==============================")

    vector_storage = create_vector_storage(
        chunked_documents
    )

    print(
        f"Number of vectors: "
        f"{vector_storage.index.ntotal}"
    )

    print(
        f"Vector dimensions: "
        f"{vector_storage.index.d}"
    )


    # Step 5: Semantic search

    print("\n==============================")
    print("STEP 5: SEMANTIC SEARCH")
    print("==============================")

    print(
        f"Query: {query}"
    )

    retrieved_documents = search_documents(
        vector_storage,
        query=query,
        k=k
    )

    print(
        f"Retrieved documents: "
        f"{len(retrieved_documents)}"
    )


    # Step 6: Display retrieved documents

    print("\n==============================")
    print("RETRIEVED DOCUMENTS")
    print("==============================")

    for i, document in enumerate(
        retrieved_documents,
        start=1
    ):

        print(
            f"\n--- Document {i} ---"
        )

        print(
            f"Source: "
            f"{document.metadata.get('source')}"
        )

        print(
            f"Type: "
            f"{document.metadata.get('type')}"
        )

        print(
            f"Drug: "
            f"{document.metadata.get('drug_name')}"
        )

        print("\nContent:")

        print(
            document.page_content
        )


    # Step 7: Build context

    context = "\n\n".join(
        document.page_content
        for document in retrieved_documents
    )


    print("\n==============================")
    print("CONTEXT CREATED")
    print("==============================")

    print(context)


    return context