from pathlib import Path

from haystack import Pipeline
from haystack.components.converters import PyPDFToDocument
from haystack.components.writers import DocumentWriter
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.components.retrievers.in_memory import InMemoryBM25Retriever


PDF_FOLDER = PDF_FOLDER = Path("W8D3/pdfs")


def build_document_store():
    """Create a document store and index all W8D3 PDF files."""

    document_store = InMemoryDocumentStore()

    converter = PyPDFToDocument()

    writer = DocumentWriter(
        document_store=document_store
    )

    pipeline = Pipeline()

    pipeline.add_component(
        "converter",
        converter
    )

    pipeline.add_component(
        "writer",
        writer
    )

    pipeline.connect(
        "converter.documents",
        "writer.documents"
    )

    pdf_files = list(
        PDF_FOLDER.glob("*.pdf")
    )

    pipeline.run(
        {
            "converter": {
                "sources": pdf_files
            }
        }
    )

    return document_store


def test_pdf_files_exist():
    """Verify that all five PDF documents are available."""

    pdf_files = list(
        PDF_FOLDER.glob("*.pdf")
    )

    assert len(pdf_files) == 5


def test_documents_are_indexed():
    """Verify that all PDF documents are indexed."""

    document_store = build_document_store()

    assert document_store.count_documents() == 5


def test_bm25_retriever_returns_documents():
    """Verify that BM25 returns relevant documents."""

    document_store = build_document_store()

    retriever = InMemoryBM25Retriever(
        document_store=document_store
    )

    result = retriever.run(
        query="What is Python?",
        top_k=3
    )

    documents = result["documents"]

    assert len(documents) > 0

    first_file = Path(
        documents[0].meta["file_path"]
    ).name

    assert first_file == "python.pdf"