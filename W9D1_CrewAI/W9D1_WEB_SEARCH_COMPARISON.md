# W9D1 Web Search Comparison

## Objective

The CrewAI research crew was enhanced by adding a web search tool to the Researcher agent.

## Before Web Search

The original Researcher agent generated information using the configured Gemini LLM without an external web search tool.

### Limitations

- Information depended only on the model's existing knowledge.
- No external web sources were retrieved during execution.
- Recent information could not be directly verified.

## After Web Search

A `SerperDevTool` was added to the Researcher agent.

The Researcher can now perform web searches and use retrieved information while completing the research task.

### Improvements

- Access to current web information.
- Better support for research tasks requiring recent information.
- Researcher can retrieve external information before passing findings to the Writer.
- The Writer and Reviewer continue to process the Researcher's output sequentially.

## Crew Workflow

```text
Researcher
    |
    |-- Web Search Tool
    |
    v
Research Findings
    |
    v
Writer
    |
    v
Reviewer
    |
    v
Final Research Output
```
