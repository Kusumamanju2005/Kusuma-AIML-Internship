from pathlib import Path

from haystack import Pipeline
from haystack.components.converters import PyPDFToDocument
from haystack.components.writers import DocumentWriter
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack_integrations.components.embedders.sentence_transformers import (
    SentenceTransformersDocumentEmbedder,
    SentenceTransformersTextEmbedder,
)
from haystack.components.retrievers.in_memory import InMemoryEmbeddingRetriever

from questions import questions


# Expected PDF for each question
expected_files = [
    "python.pdf",
    "python.pdf",
    "machine_learning.pdf",
    "machine_learning.pdf",
    "rag.pdf",
    "rag.pdf",
    "chromadb.pdf",
    "chromadb.pdf",
    "langchain.pdf",
    "langchain.pdf",
]


# Create document store
document_store = InMemoryDocumentStore(
    embedding_similarity_function="cosine"
)


# Create document embedder
document_embedder = SentenceTransformersDocumentEmbedder(
    model="sentence-transformers/all-MiniLM-L6-v2"
)

document_embedder.warm_up()


# Create converter and writer
converter = PyPDFToDocument()

writer = DocumentWriter(
    document_store=document_store
)


# Build indexing pipeline
indexing_pipeline = Pipeline()

indexing_pipeline.add_component(
    "converter",
    converter
)

indexing_pipeline.add_component(
    "embedder",
    document_embedder
)

indexing_pipeline.add_component(
    "writer",
    writer
)


indexing_pipeline.connect(
    "converter.documents",
    "embedder.documents"
)

indexing_pipeline.connect(
    "embedder.documents",
    "writer.documents"
)


# Find PDFs
pdf_files = list(
    Path("pdfs").glob("*.pdf")
)

print(f"Found {len(pdf_files)} PDF files")


# Index documents
indexing_pipeline.run(
    {
        "converter": {
            "sources": pdf_files
        }
    }
)


print(
    f"Indexed documents: "
    f"{document_store.count_documents()}"
)


# Create text embedder
text_embedder = SentenceTransformersTextEmbedder(
    model="sentence-transformers/all-MiniLM-L6-v2"
)

text_embedder.warm_up()


# Create dense retriever
retriever = InMemoryEmbeddingRetriever(
    document_store=document_store
)


print("\n========== DENSE RETRIEVAL EVALUATION ==========")


precisions = []


for i, question in enumerate(questions):

    # Convert question into embedding
    query_embedding = text_embedder.run(
        text=question
    )["embedding"]


    # Retrieve documents
    result = retriever.run(
        query_embedding=query_embedding,
        top_k=3
    )


    retrieved_documents = result["documents"]

    relevant_count = 0


    print(f"\nQ{i + 1}: {question}")
    print(f"Expected: {expected_files[i]}")


    for j, document in enumerate(
        retrieved_documents,
        start=1
    ):

        file_path = document.meta.get(
            "file_path",
            ""
        )

        file_name = Path(
            file_path
        ).name


        print(
            f"  {j}. {file_name}"
        )


        if file_name == expected_files[i]:
            relevant_count += 1


    # Precision = relevant documents / retrieved documents
    precision = (
        relevant_count / len(retrieved_documents)
        if retrieved_documents
        else 0
    )


    precisions.append(precision)


    print(
        f"Precision: {precision:.2f}"
    )


# Calculate average precision
average_precision = sum(precisions) / len(
    precisions
)


print("\n==========================================")
print(
    f"Dense Average Precision: "
    f"{average_precision:.2f}"
)
print("==========================================")