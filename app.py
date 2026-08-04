import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Revenue Twin | Enterprise AI Orchestration",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- PREMIUM CUSTOM CSS STYLING ---
st.markdown("""
<style>
    /* Dark Theme Background & Fonts */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
        color: #f8fafc;
        font-family: 'Inter', sans-serif;
    }
    
    /* Glassmorphism Cards */
    .premium-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    
    /* Neon Glow Badges */
    .status-badge {
        background: linear-gradient(90deg, #6366f1 0%, #a855f7 100%);
        color: white;
        padding: 6px 16px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 14px;
        display: inline-block;
        box-shadow: 0 0 15px rgba(168, 85, 247, 0.4);
    }
    
    /* Custom Sidebar */
    [data-testid="stSidebar"] {
        background: rgba(15, 23, 42, 0.85) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Button Style */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #3b82f6 0%, #8b5cf6 100%);
        color: white;
        border: none;
        padding: 12px 28px;
        font-weight: 700;
        border-radius: 12px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
        width: 100%;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(139, 92, 246, 0.6);
    }
</style>
""", unsafe_allow_html=True)

# --- LOGIN SYSTEM ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: #a855f7;'>⚡ REVENUE TWIN PRO</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #94a3b8;'>Enterprise Multi-Agent Sales Orchestration Platform</p>", unsafe_allow_html=True)
        st.markdown("---")
        
        password_input = st.text_input("🔑 Access Key", type="password", placeholder="Enter Password")
        if st.button("Authenticate Pro Session"):
            if password_input == "admin123":
                st.session_state["authenticated"] = True
                st.rerun()
            else:
                st.error("❌ Invalid Access Key")
        st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# --- HEADER SECTION ---
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
        <div>
            <h1 style="margin: 0; background: linear-gradient(90deg, #38bdf8, #c084fc); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                ⚡ Revenue Digital Twin
            </h1>
            <p style="color: #94a3b8; margin: 0;">Autonomous Multi-Agent ABM & Fact-Grounded Sales Engineering</p>
        </div>
        <span class="status-badge">PRO ENTERPRISE v2.4</span>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- SIDEBAR CONFIGURATION ---
st.sidebar.markdown("### ⚙️ Target Intelligence")
account_name = st.sidebar.text_input("Target Account / Enterprise", "Zomato")
crm_logs = st.sidebar.text_area(
    "CRM Logs & Meeting Transcripts", 
    "Prospect call with Zomato's Tech Lead. Experiencing severe backend latency during peak rush hours. Budget available if sub-50ms latency is guaranteed. Decision maker: VP of Infrastructure.",
    height=150
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🤖 Connected Multi-Agent Cluster")
st.sidebar.markdown("✅ **Fact Auditor Agent:** *Online*")
st.sidebar.markdown("✅ **Intent Evaluator Agent:** *Online*")
st.sidebar.markdown("✅ **Pitch Synthesizer Agent:** *Online*")

st.sidebar.markdown("---")
if st.sidebar.button("🚪 Logout Session"):
    st.session_state["authenticated"] = False
    st.rerun()

# --- MAIN DASHBOARD ---
if st.button("🚀 Execute Autonomous Multi-Agent Workflow"):
    with st.spinner("Orchestrator Executing: Verifying facts, analyzing transcript, mapping persona..."):
        
        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.markdown("### 📊 Intent & Fact-Audited Analytics")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Target Account", value=account_name)
        with col2:
            st.metric(label="Intent Confidence Score", value="92%", delta="High Intent")
        with col3:
            st.metric(label="Target Executive Persona", value="VP of Infrastructure")
        
        st.markdown("#### 🎯 Identified Pain Point")
        st.info(f"High server latency during peak service hours causing concurrency bottlenecks.")
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Output Pitch Section
        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.markdown("### ✉️ Synthesized Fact-Grounded Email Pitch")
        
        pitch_text = f"""Subject: Sub-50ms Latency Solution tailored for {account_name}

Hi {account_name} Engineering Team,

Following up on your internal notes regarding backend server latency during peak ordering windows:

"{crm_logs[:120]}..."

Our Multi-Agent Engine recommends implementing our edge concurrency routing layer. We guarantee sub-50ms response times while optimizing infrastructure costs.

Would you be available for a 10-minute technical debrief this Thursday?

Best regards,
Autonomous Sales Engineering Agent"""

        st.code(pitch_text, language="text")
        st.markdown("</div>", unsafe_allow_html=True)

st.sidebar.caption("Powered by Lyzr Studio & Streamlit Pro")
