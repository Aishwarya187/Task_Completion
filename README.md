# Task_Completion
##Agentic AI Task Completion Assistant

An autonomous task assistant that understands commands, decomposes them, and executes subtasks using LLaMA3 and LangChain.

## Features
- Accepts natural language tasks
- Breaks down into subtasks (agentic decomposition)
- Executes tasks and tracks memory in JSON
- LLaMA 3 integration via Ollama
- Built with React (UI) + FastAPI (backend)

## Examples
> “Plan my weekend schedule”  
> “Generate 5 startup ideas and create a summary report”

## Tech Stack
- **Frontend:** React.js
- **Backend:** FastAPI
- **LLM Engine:** LLaMA3 via Ollama
- **Memory Storage:** JSON-based memory store
- **LangChain:** Plan-and-Execute agent integration (local mode)

## Architecture
1. User input → Backend parses command
2. LLM via LangChain decomposes into subtasks
3. Subtasks are executed & logged
4. Progress shown on UI

