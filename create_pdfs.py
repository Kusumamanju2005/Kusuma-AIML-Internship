from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from pathlib import Path


output_folder = Path("pdfs")
output_folder.mkdir(exist_ok=True)


documents = {
    "python.pdf": """
Python is a high-level, interpreted programming language.
It is widely used for web development, automation, data science,
artificial intelligence, machine learning, and scripting.

Python uses simple and readable syntax. It supports multiple
programming styles including procedural, object-oriented, and
functional programming.

Python provides many built-in libraries and also has a large
collection of third-party packages.
""",

    "machine_learning.pdf": """
Machine Learning is a branch of Artificial Intelligence.

It allows computers to learn patterns from data and make
predictions or decisions without being explicitly programmed
for every individual task.

The three common types of machine learning are supervised
learning, unsupervised learning, and reinforcement learning.

Supervised learning uses labelled data. Unsupervised learning
finds patterns in data without labelled outputs. Reinforcement
learning learns through rewards and penalties.
""",

    "rag.pdf": """
Retrieval-Augmented Generation, commonly called RAG, combines
information retrieval with text generation.

A RAG system first retrieves relevant documents from a knowledge
base. The retrieved documents are then provided as context to
a language model.

The language model uses the retrieved context to generate an
answer. RAG can help ground responses in external information
and reduce unsupported answers.

RAG is commonly used for document question answering and
knowledge-based AI applications.
""",

    "chromadb.pdf": """
ChromaDB is a vector database commonly used in AI applications.

It stores vector embeddings that represent documents or pieces
of text. Applications can search these embeddings using semantic
similarity.

In a RAG system, ChromaDB can store document embeddings and
retrieve relevant chunks for a user's question.

Vector databases are useful when traditional keyword matching
is not enough to find semantically related information.
""",

    "langchain.pdf": """
LangChain is a framework for developing applications powered
by language models.

It provides components for prompts, document processing,
retrievers, vector stores, chains, and agents.

LangChain can connect language models with external data
sources and tools.

It is commonly used to build question-answering systems,
RAG applications, conversational applications, and AI agents.
"""
}


def create_pdf(filename, text):
    file_path = output_folder / filename

    pdf = canvas.Canvas(str(file_path), pagesize=A4)

    width, height = A4
    x = 50
    y = height - 50

    pdf.setFont("Helvetica", 11)

    for paragraph in text.strip().split("\n"):
        paragraph = paragraph.strip()

        if not paragraph:
            y -= 15
            continue

        words = paragraph.split()
        line = ""

        for word in words:
            test_line = line + word + " "

            if pdf.stringWidth(test_line, "Helvetica", 11) < width - 100:
                line = test_line
            else:
                pdf.drawString(x, y, line.strip())
                y -= 16
                line = word + " "

                if y < 50:
                    pdf.showPage()
                    pdf.setFont("Helvetica", 11)
                    y = height - 50

        if line:
            pdf.drawString(x, y, line.strip())
            y -= 16

    pdf.save()

    print(f"Created: {file_path}")


for filename, text in documents.items():
    create_pdf(filename, text)

print("\n✅ All 5 PDF documents created successfully!")