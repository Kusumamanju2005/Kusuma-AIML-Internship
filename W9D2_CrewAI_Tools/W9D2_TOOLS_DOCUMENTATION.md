# W9D2 CrewAI Tools Documentation

## Objective

The CrewAI research crew was enhanced with external web search and a custom Python calculation tool.

## Agents

### Researcher

- Uses SerperDevTool for web search.
- Uses Python Calculator for basic calculations.
- Collects information for the research task.

### Writer

- Converts the research findings into a clear article.
- Uses the Researcher's output.

### Reviewer

- Checks the article for accuracy, clarity, completeness, and structure.
- Provides suggestions for improvement.

## Tools

### 1. SerperDevTool

The web search tool allows the Researcher agent to retrieve information from the web.

### 2. Python Calculator

A custom CrewAI tool was created to perform basic arithmetic calculations.

Example:

```text
((75 - 50) / 50) * 100 = 50%
```
