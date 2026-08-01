import streamlit as st
import requests

# Page Config
st.set_page_config(page_title="Revenue Digital Twin", page_icon="🚀", layout="wide")

st.title("🚀 Revenue Digital Twin Manager")
st.subheader("Autonomous Multi-Agent ABM & Fact-Grounded Sales Orchestration")

st.markdown("---")

# Sidebar Input
st.sidebar.header("Account Details")
account_name = st.sidebar.text_input("Target Account / Company", "Acme Corp")
crm_logs = st.sidebar.text_area("Paste CRM Logs / Call Transcripts", "Client suffers high latency and cloud infrastructure costs. Decision maker: CTO Suresh.")

st.sidebar.markdown("---")
st.sidebar.info("Connected Lyzr Orchestrator Agent: Live")

# Main Action Button
if st.button("Run Multi-Agent Workflow"):
    st.info("Orchestrator Executing: Verifying facts, calculating intent, mapping persona, and synthesizing pitch...")
    
    # Live Lyzr Agent Embed Display
    st.markdown("### 🤖 Lyzr Agent Interactive Playground")
    lyzr_url = "https://studio.lyzr.ai/create-new-agent/6a6e235494f73521498d2ddf?tab=playground&public=true"
    st.components.v1.iframe(lyzr_url, height=700, scrolling=True)

st.sidebar.caption("Powered by Lyzr Studio & Streamlit")
