"""
Enhanced Launcher script for Mock Interview Analyzer
Provides a better user experience with advanced loading screen
"""

import streamlit as st
import sys
import os
import time

# Set page config for better UX
st.set_page_config(
    page_title="Mock Interview Analyzer",
    page_icon="🎤",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add the mock_interview module to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'mock_interview'))

def show_advanced_loading_screen():
    """Display an advanced loading screen with multiple phases"""
    # Create a placeholder for the loading content
    loading_placeholder = st.empty()
    
    # Show advanced loading animation
    loading_placeholder.markdown("""
    <div style="text-align: center; padding: 4rem;">
        <h1 style="color: #1f77b4; margin-bottom: 1rem; font-size: 2.5rem;">🎤 Mock Interview Analyzer</h1>
        <p style="font-size: 1.3rem; color: #666; margin-bottom: 3rem;">
            AI-Powered Interview Practice & Analysis
        </p>
        <div style="margin: 3rem 0;">
            <div style="display: inline-block; width: 60px; height: 60px; border: 6px solid #f3f3f3; border-top: 6px solid #1f77b4; border-radius: 50%; animation: spin 1s linear infinite;"></div>
        </div>
        <p style="color: #888; font-size: 1.1rem;">Initializing intelligent analysis components...</p>
        <div style="margin-top: 2rem;">
            <div style="display: inline-block; width: 20px; height: 20px; background-color: #1f77b4; border-radius: 50%; animation: pulse 1.5s ease-in-out infinite;"></div>
            <div style="display: inline-block; width: 20px; height: 20px; background-color: #1f77b4; border-radius: 50%; animation: pulse 1.5s ease-in-out infinite 0.2s; margin-left: 10px;"></div>
            <div style="display: inline-block; width: 20px; height: 20px; background-color: #1f77b4; border-radius: 50%; animation: pulse 1.5s ease-in-out infinite 0.4s; margin-left: 10px;"></div>
        </div>
    </div>
    
    <style>
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    @keyframes pulse {
        0%, 100% { opacity: 0.3; transform: scale(1); }
        50% { opacity: 1; transform: scale(1.2); }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Show progress bar with detailed steps
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Detailed loading steps
    loading_steps = [
        ("🔧 Loading core modules...", 15),
        ("🧠 Initializing AI analyzer...", 30),
        ("🎙️ Setting up audio processor...", 45),
        ("📚 Loading question database...", 60),
        ("🔍 Preparing analysis algorithms...", 75),
        ("🎯 Finalizing interface...", 90),
        ("✅ Ready to start!", 100)
    ]
    
    for step_text, progress in loading_steps:
        status_text.text(step_text)
        progress_bar.progress(progress)
        time.sleep(0.4)  # Simulate loading time
    
    # Clear loading screen
    loading_placeholder.empty()
    progress_bar.empty()
    status_text.empty()

def main():
    """Main function to run the Mock Interview Analyzer"""
    
    # Show advanced loading screen
    show_advanced_loading_screen()
    
    # Import and run the main UI
    try:
        from ui.mock_interview_ui import show_mock_interview_ui
        show_mock_interview_ui()
    except ImportError as e:
        st.error(f"❌ Error loading the application: {e}")
        st.error("Please make sure all dependencies are installed correctly.")
        st.info("💡 Try running: pip install -r requirements.txt")
    except Exception as e:
        st.error(f"❌ An unexpected error occurred: {e}")
        st.info("💡 Please check the console for more details.")

if __name__ == "__main__":
    main()
