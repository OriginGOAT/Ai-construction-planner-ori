from groq import Groq
import os
from dotenv import load_dotenv
from backend.memory import SessionMemory

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)
memory = SessionMemory()


def run_agent(
    user_input,
    location=None,
    project_type=None,
    soil=None,
    workers=0,
    cement=0,
    excavators=0,
    steel=0,
    budget=0
):

    mem = memory.get_memory()

    project_data = {
        "location":location,
        "structure":project_type,
        "soil":soil,
        "workers":workers,
        "cement":cement,
        "excavators":excavators,
        "steel":steel,
        "budget":budget
    }

    memory.update_project(project_data)

    context = f"""
Previous Project Info: {mem['project']}
Conversation History: {mem['history']}
"""

    system_prompt = f"""
You are a Professional Construction Planning AI Agent.

Use previous memory to refine planning decisions.

Memory Context:
{context}

Generate:

PROJECT OVERVIEW
OPTIMIZED WORKFLOW
EXECUTION SCHEDULE
RESOURCE CONSTRAINTS
IDENTIFIED RISKS
MITIGATION PLAN
"""

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role":"system","content":system_prompt},
                {"role":"user","content":user_input}
            ],
            temperature=0.4,
            max_tokens=1200
        )

        reply = response.choices[0].message.content

        memory.update_history(user_input,reply)

        return reply

    except Exception as e:
        return f"Groq API Error: {str(e)}"
