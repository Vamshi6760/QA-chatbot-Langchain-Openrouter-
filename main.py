"""
QA chatbot — LangChain + OpenRouter (direct LLM answers, no RAG).

Setup:
  pip install langchain-openrouter langchain-core
  set OPENROUTER_API_KEY=your_key_here
  python main.py
"""

import os
import sys
from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openrouter import ChatOpenRouter


def main() -> None:
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("Error: set OPENROUTER_API_KEY in your environment.", file=sys.stderr)
        sys.exit(1)

    model_name = os.environ.get("OPENROUTER_MODEL", "google/:frgemma-2-9b-itee")

    llm = ChatOpenRouter(
        model=model_name,
        temperature=0.7,
        api_key=api_key,
    )

    messages: list = [
        SystemMessage(
            content=(
                "You are a helpful question-answering assistant. "
                "Answer clearly and concisely. If you are unsure, say so."
            )
        )
    ]

    print("QA Chatbot (LangChain + OpenRouter)")
    print(f"Model: {model_name}")
    print("Type your question, or 'quit' / 'exit' to leave.\n")

    while True:
        try:
            question = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):   
            print("\nGoodbye.")
            break

        if not question:
            continue
        if question.lower() in {"quit", "exit", "q"}:
            print("Goodbye.")
            break

        messages.append(HumanMessage(content=question))

        try:
            response = llm.invoke(messages)
        except Exception as exc:
            print(f"Error: {exc}\n", file=sys.stderr)
            messages.pop()
            continue

        answer = response.content if isinstance(response, AIMessage) else str(response.content)
        print(f"Bot: {answer}\n")
        messages.append(AIMessage(content=answer))


if __name__ == "__main__":
    main()
