<div align="center">

# Developer Tools Research Agent

**An agentic AI system that discovers, researches, and compares developer tools from the web.**

Built with Python, LangGraph, Firecrawl, LangChain, OpenRouter, and Pydantic.

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![LangGraph](https://img.shields.io/badge/Orchestration-LangGraph-1C3C3C)](https://www.langchain.com/langgraph)
[![Firecrawl](https://img.shields.io/badge/Web%20Research-Firecrawl-FF6B35)](https://www.firecrawl.dev/)
[![OpenRouter](https://img.shields.io/badge/LLM-OpenRouter-6B46C1)](https://openrouter.ai/)
[![Pydantic](https://img.shields.io/badge/Data%20Validation-Pydantic-E92063)](https://docs.pydantic.dev/)

</div>

---

## Overview

Choosing the right developer tool can mean comparing products across dozens of websites, documentation pages, and pricing pages. This project explores how an AI agent can automate that research process.

The **Developer Tools Research Agent** takes a natural-language query, discovers relevant tools and services, researches their official websites, extracts structured technical and commercial information, and produces a concise recommendation.

Rather than relying on a single LLM response, the application uses a **multi-step LangGraph workflow** to separate discovery, research, and recommendation generation.

## What it does

Given a query such as:

> I need a backend platform for a Python application. What are the best alternatives?

The workflow:

1. **Discovers relevant tools** — searches the web for articles and pages related to the query.
2. **Extracts candidate products** — uses an LLM to identify specific developer tools and services from the retrieved content.
3. **Researches each candidate** — searches for its official website and scrapes page content.
4. **Structures the findings** — uses Pydantic models and structured LLM output to capture comparable information.
5. **Generates a recommendation** — produces a short, practical summary based on the researched candidates.

If candidate extraction does not return results, the research step falls back to a direct web search.

## Information collected

For each researched tool, the agent attempts to extract:

| Attribute | Description |
|---|---|
| Website | Official website URL |
| Description | Short explanation of the product |
| Pricing model | Free, Premium, Paid, Enterprise, or Unknown |
| Open source | Whether the product is open source, where identifiable |
| Tech stack | Relevant languages, frameworks, databases, and technologies |
| API availability | Whether an API, SDK, or programmatic access is indicated |
| Language support | Programming languages supported |
| Integrations | Other tools and platforms it integrates with |

The final recommendation is designed to highlight the most suitable option, pricing considerations, and its main technical advantage.

> **Note:** Results are generated from web content and LLM analysis. They should be independently verified, especially for pricing, licensing, API availability, and other details that can change.

## Architecture

The workflow is implemented as a sequential LangGraph state graph:

```text
                 User query
                     |
                     v
          +----------------------+
          |   Extract Tools      |
          |                      |
          | Firecrawl web search |
          | Page scraping        |
          | LLM tool extraction  |
          +----------------------+
                     |
                     v
          +----------------------+
          |       Research       |
          |                      |
          | Search official site |
          | Scrape page content  |
          | Structured analysis |
          +----------------------+
                     |
                     v
          +----------------------+
          |       Analyze        |
          |                      |
          | Aggregate findings   |
          | Generate recommendation
          +----------------------+
                     |
                     v
               Final results
```

### Workflow state

A Pydantic `ResearchState` object carries information between workflow steps:

- `query` — the original user query.
- `extracted_tools` — candidate tools identified during discovery.
- `companies` — structured research results for each candidate.
- `search_results` — field available for storing search-result data.
- `analysis` — the final recommendation.

### Design choices

- **LangGraph** provides explicit workflow orchestration and shared state between steps.
- **Firecrawl** handles web search and extracts page content in Markdown.
- **OpenRouter** provides access to the `openai/gpt-4o-mini` model used for extraction, analysis, and recommendations.
- **Pydantic** defines structured output models so research results can be represented consistently.
- **Prompt separation** keeps tool extraction, tool analysis, and recommendation instructions in a dedicated module.

## Tech stack

| Technology | Role |
|---|---|
| Python 3.11+ | Core application |
| LangGraph | Multi-step workflow orchestration |
| LangChain | LLM messages and model integration |
| OpenRouter | LLM API access (`openai/gpt-4o-mini`) |
| Firecrawl | Web search and website scraping |
| Pydantic | Structured data models and validation |
| python-dotenv | Environment variable management |
| uv | Dependency and environment management |

## Project structure

```text
AI-Agent/
├── src/
│   └── advanced_agent/
│       ├── __init__.py
│       ├── firecrawl.py       # Web search and website scraping
│       ├── models.py          # Pydantic research-state and output models
│       ├── prompts.py         # Extraction, analysis, and recommendation prompts
│       └── workflow.py        # LangGraph workflow and processing steps
├── main.py                    # Interactive command-line entry point
├── pyproject.toml             # Project metadata and dependencies
├── uv.lock                    # Locked dependency versions
├── .python-version
├── .gitignore
└── README.md
```

## Getting started

### Prerequisites

- Python 3.11 or newer
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- A [Firecrawl API key](https://www.firecrawl.dev/)
- An [OpenRouter API key](https://openrouter.ai/)

### 1. Clone the repository

```bash
git clone https://github.com/fardinAhmed285/AI-Agent.git
cd AI-Agent
```

### 2. Install dependencies

This project uses `uv` and includes a `uv.lock` file.

```bash
uv sync
```

### 3. Configure API keys

Create a `.env` file in the project root:

```env
FIRECRAWL_API_KEY=your_firecrawl_api_key
OPENROUTER_API_KEY=your_openrouter_api_key
```

Keep this file private. Do not commit API keys or other secrets to Git.

### 4. Run the agent

```bash
uv run python main.py
```

Enter a developer-tools research query when prompted:

```text
Developer Tools Research Agent

🔍 Developer Tools Query: best alternatives to Supabase for a Python backend
```

To stop the application, enter:

```text
exit
```

You can also use `quit`.

## Example use cases

Try queries such as:

- `Compare open-source alternatives to Firebase.`
- `What developer tools provide API access for Python applications?`
- `Find backend platforms suitable for a small SaaS project.`
- `Compare developer tools based on pricing, integrations, and language support.`
- `Which tools offer a free tier and support TypeScript?`

These are example prompts, not precomputed results. The agent performs live research when run with valid API credentials.

## Current scope and limitations

This repository is an evolving project. The current implementation is a command-line research workflow, not a hosted web application.

- Research quality depends on the search results and the content available on the pages retrieved.
- Some websites may block scraping or expose incomplete information.
- Pricing, licensing, and feature claims should be checked against official documentation.
- API usage may incur charges or be subject to provider rate limits.
- The workflow currently runs its discovery, research, and recommendation steps sequentially.

## Roadmap

Potential next improvements:

- [ ] Add source URLs alongside each extracted attribute.
- [ ] Improve evidence traceability for LLM-generated claims.
- [ ] Add retry handling and more detailed error reporting.
- [ ] Add automated tests for individual workflow steps.
- [ ] Support configurable models and research depth.
- [ ] Add result export to Markdown or JSON.
- [ ] Explore parallel research of candidate tools.
- [ ] Add a simple web interface for interactive research.

## Author

**Fardin Ahmed**

Computer Science graduate | Master's student in Artificial Intelligence

Interested in Agentic AI, LLM applications, machine learning, and software engineering.

- GitHub: [@fardinAhmed285](https://github.com/fardinAhmed285)
- Project: [AI-Agent](https://github.com/fardinAhmed285/AI-Agent)

---

<div align="center">

**Built to explore practical applications of agentic AI and LLM-powered research.**

</div>
