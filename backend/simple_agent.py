from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in environment variables")

client = Groq(api_key=GROQ_API_KEY)


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

    system_prompt = f"""
You are an AI Construction Planning Agent used by civil engineers and project managers.

You must generate:

1. Optimized Construction Workflow
2. Execution Schedule
3. Resource Constraint Check
4. Risk Identification
5. Mitigation Suggestions

Consider:

Project Location: {location}
Project Type: {project_type}
Soil Type: {soil}

Available Resources:
Workers: {workers}
Cement: {cement}
Excavators: {excavators}
Steel: {steel}
Budget: {budget}

Think like a real project planner.

Output strictly in this format:

PROJECT OVERVIEW
---------------
Location:
Structure:
Soil Stability:
Weather Risk:

OPTIMIZED WORKFLOW
------------------

EXECUTION SCHEDULE
------------------

RESOURCE CONSTRAINTS
------------------

IDENTIFIED RISKS
------------------

MITIGATION PLAN
------------------
"""

    user_prompt = f"""
User Request:
{user_input}

Generate the full project planning response.
"""

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.4,
            max_tokens=1200
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Groq API Error: {str(e)}"
