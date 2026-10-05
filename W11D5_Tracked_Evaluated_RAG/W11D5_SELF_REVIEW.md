\# W11D5 Self Review



\## Completion Checklist



\- \[x] Built a working RAG pipeline

\- \[x] Used ChromaDB for vector retrieval

\- \[x] Used HuggingFace embeddings

\- \[x] Processed 10 benchmark questions

\- \[x] Integrated MLflow experiment tracking

\- \[x] Logged RAG configuration

\- \[x] Logged retrieval performance

\- \[x] Linked Ragas evaluation evidence from W11D4

\- \[x] Tested the complete pipeline

\- \[x] Created output evidence

\- \[x] Documented limitations honestly



\## Key Design Decisions



ChromaDB was used for semantic retrieval and HuggingFace embeddings

were selected to keep the pipeline local.



MLflow was used to track important RAG configuration and retrieval

performance.



Ragas evaluation was performed in W11D4 and its results were reused

as evaluation evidence for the integrated Week 11 project.



\## Hardest Part



The hardest part was running Ragas locally with the Ollama evaluator.

Some evaluation jobs timed out because the local 1B model was slow.

The issue was handled by stopping the long-running evaluation and

using the completed W11D4 evaluation results as evidence.



\## One More Day



With one more day, I would improve the generation model, run a larger

evaluation benchmark, add automated tests, and connect the project

to a complete CI/CD workflow.



\## CIA



CIA Full Stack Mentor Mode was not available through the current

integration, so no CIA interaction was fabricated.

