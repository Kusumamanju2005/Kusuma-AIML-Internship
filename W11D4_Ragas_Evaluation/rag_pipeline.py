from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
HuggingFaceEmbeddings
from langchain_chroma import Chroma

DATASET = "rag_dataset.txt"
CHROMA_DIR = "chroma_db"


def build_vector_store(chunk_size=300, chunk_overlap=50):
    loader = TextLoader(DATASET, encoding="utf-8")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DIR
    )

    print("========== RAG PIPELINE ==========")
    print(f"Documents loaded: {len(documents)}")
    print(f"Chunks created: {len(chunks)}")
    print(f"Chunk size: {chunk_size}")
    print(f"Chunk overlap: {chunk_overlap}")
    print("ChromaDB vector store created successfully.")

    return vector_store


if __name__ == "__main__":
    build_vector_store()