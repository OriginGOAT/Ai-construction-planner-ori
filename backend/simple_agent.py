from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_agent(
    user_input,
    location=None,
    project_type=None,
    soil=None,
    workers=0,
    cement=0,
    excavator=0,
    steel=0,
    budget=0
):

    context = f"""
You are an AI Construction Planning Agent.

Project Details:
Location: {location}
Structure Type: {project_type}
Soil Type: {soil}

Resources:
Workers: {workers}
Cement: {cement}
Excavator: {excavator}
Steel: {steel}
Budget: {budget}

You MUST:

1. Break construction into optimized workflow tasks
2. Check resource shortages
3. Suggest execution schedule
4. Identify realistic risks
5. Suggest next actionable step
6. Adapt plan based on soil and location
7. Output clean formatted response

Respond like an industry planning assistant.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role":"system","content":context},
            {"role":"user","content":user_input}
        ]
    )

    return response.choices[0].message.content
