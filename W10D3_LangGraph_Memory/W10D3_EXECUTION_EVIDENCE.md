\# W10D3 Execution Evidence



\## Objective

Implement LangGraph persistent conversations using MemorySaver and checkpoints.



\## Components Implemented



\- Three-node graph:

&#x20; - classify

&#x20; - route

&#x20; - respond



\- Conditional routing:

&#x20; - technical

&#x20; - greeting

&#x20; - general



\- Persistent memory:

&#x20; - MemorySaver()

&#x20; - thread\_id support



\- Human-in-the-loop concept:

&#x20; - pause/resume workflow prepared



\## Test Results



\### Input 1

Hello bro



Category:

greeting



Response:

Hello! How can I help you today?



\### Input 2

How can I learn Python?



Category:

technical



Response:

I can help you with Python, programming, and LangGraph.



\### Persistent Memory Verification



Saved state:



user\_input:

How can I learn Python?



category:

technical



response:

I can help you with Python, programming, and LangGraph.



conversation\_count:

1



\## Status



W10D3 completed successfully.

