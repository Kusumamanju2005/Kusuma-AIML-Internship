# W8D4: Documentation, Testing & Code Review

## Objective

Document and test the Haystack retrieval work completed in W8D3.

## Project Overview

The W8D3 project builds a document retrieval system using Haystack.

Five PDF documents are indexed:

- Python
- Machine Learning
- RAG
- ChromaDB
- LangChain

Two retrieval approaches were evaluated:

1. BM25 Retrieval
2. Dense Retrieval using Sentence Transformers

## Testing

Automated tests were created using pytest.

The tests verify:

- All five PDF files are available.
- All five documents are successfully indexed.
- BM25 retrieval returns a relevant document for a Python-related question.

Run the tests with:

```bash
pytest -v
```
