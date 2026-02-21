import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

def run_agent(
    user_input,
    location=None,
    project_type=None,
    soil=None,
    resources=None
):

    resources = resources or {}

    prompt = f"""
You are a Senior Construction Planning AI Agent.

Project Context:
Location: {location}
Structure Type: {project_type}
Soil Type: {soil}
Resources: {resources}

User Request:
{user_input}

Generate:

Project Overview
Optimized Workflow
Execution Schedule
Resource Constraints
Identified Risks
Mitigation Plan
"""

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "You are an expert construction planner."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        return f"Groq API Error: {response.text}"

    return response.json()["choices"][0]["message"]["content"]
