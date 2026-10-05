\# W10D4 Self Review



\## What I Built



I built a LangGraph workflow that classifies user requests, routes them based on category, generates a response, and pauses for human approval before completing the workflow.



\## What I Learned



\- How to create nodes using LangGraph.

\- How to use conditional edges for routing.

\- How `interrupt()` pauses graph execution.

\- How `Command(resume=...)` continues execution.

\- How `MemorySaver` maintains graph state during interruptions.



\## Hardest Part



The hardest part was understanding how the graph pauses at the human approval step and resumes after receiving the human decision.



\## How I Solved It



I used LangGraph's `interrupt()` function to pause execution and `Command(resume="yes")` to continue the graph after approval.



\## Improvement



In the future, I can add different human decisions such as approval, rejection, or requesting additional information.



\## Final Status



W10D4 Human-in-the-Loop implementation completed successfully.

