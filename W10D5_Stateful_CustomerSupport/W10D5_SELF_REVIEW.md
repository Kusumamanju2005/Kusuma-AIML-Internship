\# W10D5 Self Review



\## Project

Stateful Customer Support Agent



\## What I Built

I built a stateful customer support agent using LangGraph.



The agent:

\- Classifies customer queries.

\- Routes sensitive requests for human review.

\- Generates support responses.

\- Stores conversation history.

\- Uses MemorySaver for state persistence.

\- Uses human interrupt and resume for approval.



\## Testing

I tested five different customer scenarios:

\- Refund

\- Payment

\- Account

\- Order

\- General support



All five tests completed successfully.



\## What Went Well

The LangGraph workflow executed correctly and the human review flow worked as expected.



\## Challenge

The main challenge was handling the human review interruption and resuming the graph correctly.



\## How I Solved It

I used LangGraph `interrupt()` to pause the workflow and `Command(resume=...)` to continue it after the human decision.



\## Improvement

With more time, I would add a real LLM response generator, persistent database storage, monitoring, and automated evaluation.



\## Final Status

W10D5 implementation and testing completed successfully.

