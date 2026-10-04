# W10D2 Execution Evidence

## Project

LangGraph State Machines & Conditional Edges

## Graph Structure

START
↓
Classify
↓
Route
↓
Respond
↓
END

## Features Implemented

- LangGraph StateGraph
- Typed state definition
- Three workflow nodes
- Conditional edges
- Five test inputs
- Human-in-the-loop interrupt
- Pause and resume workflow
- Automated tests

## Five Test Inputs

1. Hello bro
2. How can I learn Python?
3. Write a programming program
4. What is your name?
5. Hey, can you help me?

## Human-in-the-Loop Test

Human input:

APPROVE

Result:

Workflow resumed successfully.

Final Response:

Request approved: Generate a research report

## Automated Tests

Command:

pytest -v W10D2_LangGraph_StateMachines/test_state_machine.py

Expected Result:

4 tests passed successfully.

## Final Result

The W10D2 LangGraph state machine was implemented and tested
with conditional routing, five test inputs, and human-in-the-loop
interrupt functionality.
