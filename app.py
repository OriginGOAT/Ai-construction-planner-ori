import streamlit as st
from backend.simple_agent import run_agent

st.set_page_config(page_title="Construction Planner", layout="wide")

if "chat" not in st.session_state:
    st.session_state.chat = []

with st.sidebar:

    st.markdown("## 📍 Project Info")

    st.session_state.location = st.text_input(
        "Project Location",
        value=st.session_state.get("location","")
    )

    st.session_state.project_type = st.selectbox(
        "Structure Type",
        ["Residential House","Commercial Building","Bridge","Warehouse"]
    )

    st.session_state.soil = st.selectbox(
        "Soil Type",
        ["Clay","Sandy","Rocky","Loamy"]
    )

    st.markdown("## 🔧 Resources")

    st.session_state.workers = st.number_input("Workers", value=10)
    st.session_state.cement = st.number_input("Cement", value=500)
    st.session_state.excavator = st.number_input("Excavators", value=1)
    st.session_state.steel = st.number_input("Steel", value=20)
    st.session_state.budget = st.number_input("Budget", value=800000)

st.title("🏗 Construction Planning Assistant")

for msg in st.session_state.chat:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask planner...")

if user_input:

    st.session_state.chat.append({"role":"user","content":user_input})

    with st.chat_message("assistant"):

        reply = run_agent(
    user_input=user_input,
    location=st.session_state.get("location"),
    project_type=st.session_state.get("project_type"),
    soil=st.session_state.get("soil"),

    workers=st.session_state.get("workers",0),
    cement=st.session_state.get("cement",0),
    excavators=st.session_state.get("excavators",0),
    steel=st.session_state.get("steel",0),
    budget=st.session_state.get("budget",0)
)



        st.markdown(reply)

    st.session_state.chat.append({"role":"assistant","content":reply})
