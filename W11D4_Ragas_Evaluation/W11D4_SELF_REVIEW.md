\# W11D4 Self Review



\## Completion Checklist



\- \[x] Built RAG pipeline using LangChain and ChromaDB

\- \[x] Created 20-paragraph knowledge dataset

\- \[x] Created 10 Q\&A benchmark pairs

\- \[x] Evaluated RAG pipeline using Ragas

\- \[x] Evaluated faithfulness

\- \[x] Evaluated answer relevancy

\- \[x] Evaluated context precision

\- \[x] Evaluated context recall

\- \[x] Identified the lowest valid baseline metric

\- \[x] Changed chunk size and retrieval top-k

\- \[x] Re-evaluated the optimised configuration

\- \[x] Recorded baseline and optimised results

\- \[x] Documented NaN results honestly

\- \[x] Added execution evidence



\## Baseline



\- Chunk size: 300

\- Chunk overlap: 50

\- Top-k: 3

\- Answer relevancy: 0.4805

\- Context precision: 1.0000

\- Context recall: 1.0000

\- Faithfulness: NaN



\## Optimised



\- Chunk size: 200

\- Chunk overlap: 40

\- Top-k: 2

\- Answer relevancy: 0.4805

\- Context precision: NaN

\- Context recall: 0.9000

\- Faithfulness: NaN



\## Review



The optimisation experiment was completed, but the tested configuration

did not improve answer relevancy. Context recall decreased, so the

optimised configuration was not better than the baseline.



The NaN values were preserved exactly as produced by Ragas.



\## CIA



CIA Full Stack Mentor Mode was not available through the current

integration, so no CIA interaction was fabricated.



