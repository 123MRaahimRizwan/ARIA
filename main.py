# main.py
import sys
import os
import pprint # Add this import

# ... existing code ...

# print("--- sys.path when main.py starts ---")
# pprint.pprint(sys.path)
# print("------------------------------------")
import os
import sys
import streamlit as st
from ui.resume_match_ui import show_resume_match_ui
from ui.ats_checker_ui import show_ats_checker_ui
from ui.interview_prep_ui import show_interview_prep_ui
from ui.mock_interview_ui import show_mock_interview_ui
from run_mock_interview import show_advanced_loading_screen

show_advanced_loading_screen()

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)


st.set_page_config(page_title="ARIA – Agentic Resume Intelligence Analyzer", layout="wide")

st.title("🤖 ARIA – Agentic Resume Intelligence Analyzer")

# Create tabs for each module
tabs = st.tabs(["📄 Resume Matcher", "📊 ATS Checker", "💬 Interview Prep Chatbot", "🎤 Mock Interview Analyzer"])

with tabs[0]:
    show_resume_match_ui()

with tabs[1]:
    show_ats_checker_ui()

with tabs[2]:
    show_interview_prep_ui()

with tabs[3]:
    show_mock_interview_ui()
