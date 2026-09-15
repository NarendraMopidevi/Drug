from langchain_community.vectorstores import FAISS

from app.rag.embeddings import get_embedding_model


def create_vector_storage(documents):

    embedding_model = get_embedding_model()
    vector_storage = FAISS.from_documents(
        documents,
        embedding_model
    )
    return vector_storage

def search_documents(
        vector_storage,
        query: str,
        k: int = 3
):
    result = vector_storage.similarity_search(query, k = k)

    return result