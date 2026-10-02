from pathlib import Path

from haystack import Pipeline
from haystack.components.converters import PyPDFToDocument
from haystack.components.writers import DocumentWriter
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.components.retrievers.in_memory import InMemoryBM25Retriever

from questions import questions


# ==========================================
# Expected relevant PDF for each question
# ==========================================

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


# ==========================================
# Create DocumentStore
# ==========================================

document_store = InMemoryDocumentStore()


# ==========================================
# PDF Converter
# ==========================================

converter = PyPDFToDocument()


# ==========================================
# Document Writer
# ==========================================

writer = DocumentWriter(
    document_store=document_store
)


# ==========================================
# Indexing Pipeline
# ==========================================

indexing_pipeline = Pipeline()

indexing_pipeline.add_component(
    "converter",
    converter
)

indexing_pipeline.add_component(
    "writer",
    writer
)

indexing_pipeline.connect(
    "converter.documents",
    "writer.documents"
)


# ==========================================
# Find PDFs
# ==========================================

pdf_files = list(
    Path("pdfs").glob("*.pdf")
)

print(f"Found {len(pdf_files)} PDF files")


# ==========================================
# Index PDFs
# ==========================================

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


# ==========================================
# BM25 Retriever
# ==========================================

retriever = InMemoryBM25Retriever(
    document_store=document_store
)


# ==========================================
# Evaluate BM25
# ==========================================

print("\n========== BM25 EVALUATION ==========")

precisions = []


for i, question in enumerate(
    questions
):

    result = retriever.run(
        query=question,
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

    precision = (
        relevant_count / len(retrieved_documents)
        if retrieved_documents
        else 0
    )

    precisions.append(precision)

    print(
        f"Precision: {precision:.2f}"
    )


# ==========================================
# Average Precision
# ==========================================

average_precision = sum(precisions) / len(
    precisions
)

print("\n==========================================")
print(
    f"BM25 Average Precision: "
    f"{average_precision:.2f}"
)
print("==========================================")