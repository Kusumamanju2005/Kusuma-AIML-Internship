# W9D3 Design Notes

## Project

Multi-Agent Research Crew using CrewAI.

## Agents

### 1. Researcher

- Searches the web for current information.
- Collects relevant and organized findings.
- Uses SerperDevTool.

### 2. Writer

- Uses the research findings.
- Converts the information into a clear article.
- Uses simple and structured language.

### 3. Reviewer

- Checks the generated article.
- Reviews accuracy, clarity, completeness, and logical flow.
- Suggests improvements.

## Pipeline

Researcher → Writer → Reviewer

A sequential process was selected because each stage depends on the output of the previous stage.

## LLM

Gemini was configured as the language model for the agents.

## Web Search

SerperDevTool was integrated so the Researcher can collect current information from the web.

## Viva Answers

### Q1. What did you build?

I built a CrewAI multi-agent research pipeline with three agents: Researcher, Writer, and Reviewer. The Researcher collects information, the Writer creates an article, and the Reviewer checks the final content.

### Q2. What was the hardest part?

The main challenge was configuring the LLM and web search tools correctly. I solved it by configuring the required API keys and using the working Gemini model with SerperDevTool.

### Q3. What would you improve?

I would add better source citations, fact verification, error handling, automated evaluation, and multiple research agents working in parallel.
