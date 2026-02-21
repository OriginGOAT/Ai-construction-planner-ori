# 🏗 AI Construction Planning Agent

An AI-powered Construction Decision Support System that assists project managers in planning, scheduling, risk evaluation and execution of infrastructure projects using both deterministic planning logic and generative AI.
// Code for AI
---

## 📌 Overview

This system combines:

- Generative AI (LLM-based planning)
- Deterministic scheduling logic
- Resource constraint validation
- Risk analysis
- Workforce productivity modelling
- Monte Carlo delay simulation
- External weather risk API

to produce actionable execution plans for construction projects.

---

## 🚀 Features

### ✔ Task Decomposition
Breaks down high-level project goals into structured construction workflow tasks.

### ✔ Schedule Optimization
Generates optimized task timelines based on resource availability.

### ✔ Resource Validation
Detects shortages in workforce, materials or equipment.

### ✔ Weather Risk Modelling
External API integration for rainfall-based delay prediction.

### ✔ Workforce Allocation
Suggests deployment strategy based on available labour.

### ✔ Cost vs Timeline Analysis
Predicts execution duration and project cost.

### ✔ Monte Carlo Simulation
Estimates probabilistic delay scenarios across multiple runs.

### ✔ Risk Mitigation Suggestions
Provides fallback strategies for detected resource or budget issues.

### ✔ Multi-Site Planning
Supports parallel project planning for multiple locations.

### ✔ Database Persistence
Stores project configuration and planning data.

---

## 🧠 System Architecture

User Input
↓
LLM Planning Agent
↓
Task Decomposer
↓
Constraint Engine
↓
Scheduler Engine
↓
Productivity Analyzer
↓
Monte Carlo Simulation
↓
Weather API
↓
Final Planning Output

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|------------|
Frontend | Streamlit |
Backend | Python |
AI Layer | Groq LLM |
Database | SQLite |
API Layer | FastAPI |
Simulation | Monte Carlo |
Visualization | Plotly |

---

## 📊 Planning Capabilities

- Task Dependency Awareness  
- Workforce Productivity Scaling  
- Budget Burn Prediction  
- Weather Delay Risk  
- Timeline Optimization  
- Multi-Project Planning  

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/ai-construction-planner-ori.git
cd ai-construction-planner-ori
