import streamlit as st

class SessionMemory:

    def init_memory(self):
        if "agent_memory" not in st.session_state:
            st.session_state.agent_memory = {
                "tasks": [],
                "risks": [],
                "schedule": [],
                "project": {},
                "history": []
            }

    def get_memory(self):
        self.init_memory()
        return st.session_state.agent_memory

    def update_project(self,data):
        mem = self.get_memory()
        mem["project"] = data

    def update_history(self,prompt,response):
        mem = self.get_memory()
        mem["history"].append({
            "user":prompt,
            "agent":response
        })

    def clear(self):
        if "agent_memory" in st.session_state:
            del st.session_state.agent_memory
