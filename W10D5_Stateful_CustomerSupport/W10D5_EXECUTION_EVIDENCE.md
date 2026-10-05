\# W10D5 Execution Evidence



\## Project

Stateful Customer Support Agent



\## Objective

Implemented a stateful customer support agent using LangGraph with

conversation memory, query classification, routing, and human review.



\## Implementation

\- Customer queries are classified into categories.

\- Sensitive refund and payment requests require human review.

\- Account, order, and general queries are handled automatically.

\- LangGraph MemorySaver is used for state persistence.

\- Conversation history is stored after each interaction.

\- Human approval is handled using LangGraph interrupt and resume.



\## Testing

Five customer support scenarios were tested:



1\. Refund request

2\. Payment issue

3\. Account/password issue

4\. Order tracking request

5\. General support request



All 5 tests completed successfully.



\## Evidence

Execution output is saved in:



`W10D5\_OUTPUT.txt`



\## Result

W10D5 stateful customer support agent successfully executed and tested.

