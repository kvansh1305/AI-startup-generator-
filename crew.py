import os
from crewai import Crew, Process
from agents import get_agents
from tasks import get_tasks
from dotenv import load_dotenv

load_dotenv()

# ── Conversation memory (persists across Gradio interactions) ──────────────
conversation_history = []

def run_crew(user_input: str) -> str:
    """Run the full agent pipeline and return formatted output."""
    global conversation_history

    # Build context string from history
    context = "\n".join(
        [f"User: {h['user']}\nAssistant summary: {h['response'][:300]}..."
         for h in conversation_history[-3:]]  # last 3 turns
    )

    agents = get_agents()
    tasks = get_tasks(agents, user_input, context=context)

    crew = Crew(
        agents=list(agents),
        tasks=tasks,
        process=Process.sequential,   # agents run in order
        verbose=True,
        memory=True,                  # CrewAI built-in memory
        embedder={
            "provider": "openai",
            "config": {"model": "text-embedding-3-small"},
        },
    )

    result = crew.kickoff()
    output = str(result)

    # Save to conversation history
    conversation_history.append({"user": user_input, "response": output})

    return output


def clear_memory():
    global conversation_history
    conversation_history = []
    return "Memory cleared."