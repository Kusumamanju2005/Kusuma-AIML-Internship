\# W11D4 Execution Evidence



\## RAG Pipeline



\- Dataset: `rag\_dataset.txt`

\- Knowledge paragraphs: 20

\- Q\&A pairs evaluated: 10

\- Vector database: ChromaDB

\- Embedding model: `sentence-transformers/all-MiniLM-L6-v2`



\## Baseline Evaluation



Configuration:



\- Chunk size: 300

\- Chunk overlap: 50

\- Top-k: 3

\- Evaluator: Ollama `llama3.2:1b`



Results:



```text

{'faithfulness': nan, 'answer\_relevancy': 0.4805, 'context\_precision': 1.0000, 'context\_recall': 1.0000}

