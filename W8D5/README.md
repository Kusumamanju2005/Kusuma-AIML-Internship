# W8D5: 2M Capstone — Local AI Research Assistant

## Objective

Build a simple local AI research assistant prototype that retrieves
relevant information from a local knowledge base and generates a
structured research report.

## Architecture

The assistant follows a simple retrieval workflow:

1. User enters a research topic.
2. The local knowledge base is loaded.
3. Relevant information is retrieved using keyword matching.
4. Retrieved information is combined into a concise summary.
5. A structured research report is displayed.

## Knowledge Base

The local knowledge base contains information about:

- Artificial Intelligence
- Machine Learning
- Retrieval-Augmented Generation
- Large Language Models
- Vector Embeddings
- AI Research Assistants

## Testing

Automated tests are implemented using pytest.

The tests verify:

- The local knowledge base can be loaded.
- Machine Learning information can be retrieved.
- The generated research report contains the requested topic
  and retrieved information.

Run the tests with:

```bash
pytest -v test_research_assistant.py
```
