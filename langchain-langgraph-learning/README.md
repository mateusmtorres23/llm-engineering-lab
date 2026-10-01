# My First AI Agents with LangChain and LangGraph

## Introduction

The idea behind this project was to build my first AI agents, and for that, I chose the LangChain and LangGraph libraries. This repository documents my learning experience through three distinct Jupyter Notebooks. The project was created to follow along with a 3-day workshop, with each notebook focusing on a specific class and feature of these libraries.

---

### 1. `agent_creation.ipynb`

In this notebook, I took my first steps in agent development. The primary goal was to understand the fundamentals: how to instantiate a model, define an agent's specific behavior through a detailed system prompt, and process inputs to get structured outputs.

* **Key Learning:** I created a "Service Desk Triage" agent for a fictional company.
* **Implementation:** I wrote a system prompt that instructed the agent to classify user requests into categories like `AUTO_RESOLVER` or `ABRIR_CHAMADO` and determine their urgency. I also used LangChain's `with_structured_output` functionality with a Pydantic class to ensure the agent's responses were always in a reliable JSON format.

---

### 2. `agent_RAG.ipynb`

This notebook focuses on implementing a core AI pattern: Retrieval-Augmented Generation (RAG). I learned how to build an agent that can answer questions based on a private knowledge base, which in this case were the PDF files located in the `text_docs/` directory.

* **Key Learning:** I built a complete RAG pipeline from scratch.
* **Implementation:** The process involved loading documents, splitting them into smaller chunks for processing, and creating vector embeddings using Google's `gemini-embedding-001` model. These embeddings were then stored in a `FAISS` vector store, which the agent uses as a retriever to find relevant information before generating an answer.

---

### 3. `agent_orchestration.ipynb`

In the final notebook, I integrated the knowledge from the previous two to build a more complex, multi-step agent using LangGraph. This is where the concept of orchestration comes into play, creating a complete and autonomous structure of nodes.

* **Key Learning:** I learned how to use LangGraph to build a stateful agent with conditional logic, where the agent can make decisions on how to proceed.
* **Implementation:** I defined an `AgentState` to hold information as it flows through the graph. I then created different functions to act as nodes in the graph (e.g., `triage_node`, `self_resolve_node`, `open_ticket_node`). Finally, I connected these nodes with conditional edges, allowing the agent to decide whether to answer a question using its RAG capabilities, ask for more information, or open a service ticket. The resulting graph provides a powerful and visual way to represent the agent's reasoning process.