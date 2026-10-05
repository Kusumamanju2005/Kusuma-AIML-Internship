# W10D2 Self Review — LangGraph State Machines

## Project

LangGraph State Machines & Conditional Edges

## Implementation Checklist

- [x] Created LangGraph StateGraph
- [x] Defined agent state
- [x] Created classify node
- [x] Created route node
- [x] Created respond node
- [x] Added conditional edges
- [x] Tested with 5 inputs
- [x] Added human-in-the-loop interrupt
- [x] Tested pause and resume
- [x] Created automated tests

## Test Result

4 automated tests completed successfully.

## Key Learning

Learned how LangGraph uses state, nodes, edges, and conditional
routing to control the flow of an agent workflow.

Also learned how human-in-the-loop interrupts can pause a workflow
and resume it after receiving human input.

## Viva Preparation

### 1. What is a StateGraph?

A StateGraph is a LangGraph workflow where nodes read and update
shared state during execution.

### 2. What are conditional edges?

Conditional edges decide which node should execute next based on
the current state.

### 3. What did I build?

I built a three-node LangGraph state machine containing classify,
route, and respond nodes with conditional routing.

### 4. How did you implement human-in-the-loop?

I used LangGraph's `interrupt()` to pause the workflow and
`Command(resume=...)` to continue it after human approval.

### 5. What would I improve?

I would add more categories, more complex routing logic, and
connect the workflow to an LLM for dynamic responses.

## Final Status

W10D2 implementation and testing completed successfully.
