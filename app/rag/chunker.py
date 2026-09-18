from langchain_text_splitters import RecursiveCharacterTextSplitter

# def chunk_documents(documents):

#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size = 500,
#         chunk_overlap = 50
#     )
#     chunks = text_splitter.split_documents(documents)
#     return chunks


def chunk_documents(documents):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )

    chunks = []

    for document in documents:

        # Keep short sections as a single chunk
        if len(document.page_content) <= 1000:

            chunks.append(document)

        # Split only long sections
        else:

            section_chunks = text_splitter.split_documents(
                [document]
            )

            chunks.extend(section_chunks)

    return chunks