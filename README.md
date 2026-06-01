# QA Chatbot (LangChain + OpenRouter)

A small command-line question-answering chatbot. You type questions in the terminal; the model answers using **LangChain** and **OpenRouter**. There is no RAG, no vector database, and no uploaded documents—the LLM answers from its own knowledge and the conversation history.

## What the code does

The entire app lives in `main.py`.

1. **Loads configuration from the environment**
   - `OPENROUTER_API_KEY` (required) — your OpenRouter API key.
   - `OPENROUTER_MODEL` (optional) — model id on OpenRouter. Defaults to `google/gemma-2-9b-it:free`.

2. **Creates the chat model**
   - Uses `ChatOpenRouter` from `langchain-openrouter` to call OpenRouter’s API.
   - `temperature=0.7` controls how creative vs. deterministic replies are.

3. **Sets up the conversation**
   - Starts with a **system message** that tells the model to act as a helpful QA assistant.
   - Keeps a `messages` list that grows as you chat so follow-up questions stay in context.

4. **Runs an interactive loop**
   - Prompts you with `You:`.
   - Appends your input as a `HumanMessage`, calls `llm.invoke(messages)`, and prints the reply as `Bot:`.
   - Appends the assistant reply as an `AIMessage` for the next turn.
   - On API errors, it prints the error and removes the failed user message so the history stays valid.
   - Empty lines are ignored. Type `quit`, `exit`, or `q` to stop (or press Ctrl+C).

## Prerequisites

- **Python 3.10+** (recommended)
- An **OpenRouter** account and API key: [https://openrouter.ai/](https://openrouter.ai/)

## Installation

Open a terminal in this project folder and install dependencies:

```bash
pip install langchain-openrouter langchain-core
```

## How to run

### 1. Set your API key

**Windows (PowerShell):**

```powershell
$env:OPENROUTER_API_KEY = "your_openrouter_api_key_here"
```

**Windows (Command Prompt):**

```cmd
set OPENROUTER_API_KEY=your_openrouter_api_key_here
```

**macOS / Linux:**

```bash
export OPENROUTER_API_KEY=your_openrouter_api_key_here
```

### 2. (Optional) Choose a different model

```powershell
$env:OPENROUTER_MODEL = "anthropic/claude-3.5-sonnet"
```

Browse models on [OpenRouter](https://openrouter.ai/models).

### 3. Start the chatbot

```bash
python main.py
```

Example session:

```
QA Chatbot (LangChain + OpenRouter)
Model: google/gemma-2-9b-it:free
Type your question, or 'quit' / 'exit' to leave.

You: What is Python used for?
Bot: Python is widely used for web development, data science, automation, ...

You: quit
Goodbye.
```

## Project structure

```
langchain project/
├── main.py      # Application entry point
└── README.md    # This file
```

## Troubleshooting

| Issue | What to do |
|--------|------------|
| `Error: set OPENROUTER_API_KEY` | Export or set `OPENROUTER_API_KEY` before running `python main.py`. |
| `ModuleNotFoundError` | Run `pip install langchain-openrouter langchain-core`. |
| API / rate-limit errors | Check your key, credits, and model name on OpenRouter. Try another `OPENROUTER_MODEL`. |

## License

Use and modify this project for learning or personal use.
