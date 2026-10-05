import json
import mlflow

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


DATASET = "../W11D4_Ragas_Evaluation/rag_dataset.txt"
QA_FILE = "../W11D4_Ragas_Evaluation/qa_pairs.json"
CHROMA_DIR = "chroma_db"
MLFLOW_DB = "sqlite:///mlflow.db"


def build_rag():
    loader = TextLoader(DATASET, encoding="utf-8")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50,
    )

    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DIR,
    )

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )

    return retriever, len(chunks)


def main():
    print("========== W11D5 TRACKED RAG PROJECT ==========")

    with open(QA_FILE, "r", encoding="utf-8") as file:
        qa_pairs = json.load(file)

    retriever, chunk_count = build_rag()

    mlflow.set_tracking_uri(MLFLOW_DB)
    mlflow.set_experiment("W11D5_Tracked_Evaluated_RAG")

    with mlflow.start_run(run_name="tracked_rag_pipeline"):

        mlflow.log_params(
            {
                "chunk_size": 300,
                "chunk_overlap": 50,
                "top_k": 3,
                "embedding_model": "all-MiniLM-L6-v2",
                "qa_pairs": len(qa_pairs),
            }
        )

        successful_retrievals = 0

        print(f"Questions: {len(qa_pairs)}")
        print(f"Chunks: {chunk_count}")
        print("Chunk size: 300")
        print("Chunk overlap: 50")
        print("Top-k: 3")
        print("Embedding: all-MiniLM-L6-v2")
        print()

        for number, item in enumerate(qa_pairs, start=1):
            question = item["question"]

            docs = retriever.invoke(question)

            if docs:
                successful_retrievals += 1

            print(
                f"Q{number}: {question}"
            )
            print(
                f"Retrieved chunks: {len(docs)}"
            )
            print()

        mlflow.log_metric(
            "retrieval_success_rate",
            successful_retrievals / len(qa_pairs),
        )

        mlflow.log_metric(
            "questions_processed",
            len(qa_pairs),
        )

        with open(
            "ragas_evaluation_reference.txt",
            "w",
            encoding="utf-8",
        ) as file:
            file.write(
                "W11D5 RAGAS EVALUATION REFERENCE\n"
            )
            file.write(
                "================================\n\n"
            )
            file.write(
                "Ragas evaluation was completed in W11D4.\n\n"
            )
            file.write(
                "Baseline:\n"
            )
            file.write(
                "Faithfulness: NaN\n"
            )
            file.write(
                "Answer relevancy: 0.4805\n"
            )
            file.write(
                "Context precision: 1.0000\n"
            )
            file.write(
                "Context recall: 1.0000\n\n"
            )
            file.write(
                "Optimised:\n"
            )
            file.write(
                "Faithfulness: NaN\n"
            )
            file.write(
                "Answer relevancy: 0.4805\n"
            )
            file.write(
                "Context precision: NaN\n"
            )
            file.write(
                "Context recall: 0.9000\n"
            )

        mlflow.log_artifact(
            "ragas_evaluation_reference.txt"
        )

        print(
            f"Successful retrievals: "
            f"{successful_retrievals}/{len(qa_pairs)}"
        )

        print()
        print("MLflow tracking completed.")
        print("Ragas W11D4 results linked as evaluation evidence.")
        print("W11D5 pipeline completed successfully.")


if __name__ == "__main__":
    main()