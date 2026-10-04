\# W10D1 Self Review — LangGraph Stateful Agent



\## Project



LangGraph — Stateful Agent Graphs



\## Implementation Checklist



\- \[x] Created LangGraph state

\- \[x] Created classify node

\- \[x] Created route node

\- \[x] Created respond node

\- \[x] Added conditional routing

\- \[x] Tested with 5 inputs

\- \[x] Added human-in-the-loop interrupt

\- \[x] Tested pause and resume

\- \[x] Created automated tests

\- \[x] All tests passed

\- \[x] Added execution evidence



\## Test Result



4/4 tests passed successfully.



\## Key Learning



Learned how LangGraph manages state, nodes, conditional

routing, and human-in-the-loop workflow interruptions.



\## Viva Preparation



\### 1. What did I build?



I built a three-node stateful LangGraph agent with classification,

conditional routing, response generation, and human-in-the-loop

interrupt functionality.



\### 2. What was the hardest part?



The hardest part was implementing the interrupt and resume

workflow. I solved it using LangGraph's `interrupt()` and

`Command(resume=...)` with a memory checkpointer.



\### 3. What would I improve?



I would add more categories, more advanced routing logic,

and connect the graph to an LLM for dynamic responses.



\## Final Status



W10D1 implementation and testing completed successfully.

