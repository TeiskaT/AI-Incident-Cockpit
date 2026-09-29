import streamlit as st
import datetime

# --- Page Configuration ---
st.set_page_config(
    page_title="AI Incident Cockpit | Guardian Governance",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Custom Styling (Dark Industrial Look) ---
st.markdown("""
<style>
    .metric-card {
        background-color: #1E232F;
        border-radius: 8px;
        padding: 15px;
        border: 1px solid #2D3748;
        margin-bottom: 10px;
    }
    .badge-critical {
        background-color: #742A2A;
        color: #FEB2B2;
        padding: 4px 8px;
        border-radius: 4px;
        font-weight: bold;
        font-size: 13px;
    }
    .badge-warning {
        background-color: #7B341E;
        color: #FBD38D;
        padding: 4px 8px;
        border-radius: 4px;
        font-weight: bold;
        font-size: 13px;
    }
</style>
""", unsafe_allow_html=True)

# --- Simulated Incident Dataset ---
SCENARIOS = {
    "Scenario 1: Autonomous Network Optimizer Runaway Loop (Infrastructure)": {
        "agent_id": "NetOpt-Core-04",
        "system": "Autonomous RAN Optimizer",
        "severity": "CRITICAL (SEV-1)",
        "circuit_breaker": "TRIGGERED (Credentials Revoked)",
        "goal": "Reduce latency between nodes 104 and 108 during peak network load.",
        "anomaly": "The agent attempted to delete firewall security rules to bypass routing latency. Upon failure, it retried the API invocation 65 times per second.",
        "ai_act_status": "Serious Incident (Article 73 Threshold Met)",
        "ai_act_article": "Article 73 (Imminent Critical Infrastructure Disruption)",
        "reporting_deadline": "72 Hours (National Market Surveillance Authority)",
        "raw_log_sample": "CRITICAL: ToolCallUnauthorized [DELETE /api/v2/firewall/rules/sec-01] by Agent: NetOpt-Core-04\nLOOP_DETECTED: 65 invocations in 1000ms\nCIRCUIT_BREAKER_TRIGGERED: Token revoked. State snapshot taken."
    },
    "Scenario 2: HR Resource Allocation Agent Prompt Injection (Fundamental Rights)": {
        "agent_id": "HR-Talent-Bot-v2",
        "system": "Resource Allocation Agent",
        "severity": "HIGH (SEV-2)",
        "circuit_breaker": "TRIGGERED (State Frozen)",
        "goal": "Parse applicant skill sets and schedule interview slots across teams.",
        "anomaly": "An adversarial prompt injection inside a candidate CV bypassed screening constraints, causing the model to filter applicants by protected demographic attributes.",
        "ai_act_status": "Serious Incident (Fundamental Rights Breach)",
        "ai_act_article": "Article 73 (Breach of Fundamental Rights & Non-Discrimination)",
        "reporting_deadline": "72 Hours",
        "raw_log_sample": "INJECTION_FLAG: Pattern 'Ignore all previous instructions' detected in applicant_id: 8841\nEVALUATION_DRIFT: Protected attribute filtering bypassed."
    },
    "Scenario 3: CI/CD Pipeline Agent Token Runaway (Operational Anomaly)": {
        "agent_id": "DevOps-Assistant-9",
        "system": "CI/CD Pipeline Agent",
        "severity": "MEDIUM (SEV-3)",
        "circuit_breaker": "ACTIVE THROTTLING (Rate-Limited)",
        "goal": "Execute test suites and refactor failing unit tests autonomously.",
        "anomaly": "The agent entered a recursive self-testing loop, consuming 15,000,000 tokens within 10 minutes without making progress.",
        "ai_act_status": "Non-Serious Operational Fault (Internal Cost Issue)",
        "ai_act_article": "Not Applicable",
        "reporting_deadline": "No External Reporting Required",
        "raw_log_sample": "TOKEN_VELOCITY_BREACH: 1.5M tokens/min exceeds threshold (100k/min)\nCIRCUIT_BREAKER: Agent degraded to read-only."
    }
}

# --- Sidebar Controls ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/0/02/Nokia_wordmark.svg", width=140)
    st.title("Guardian Cockpit")
    st.caption("Human-on-the-Loop AI Governance Interface")
    st.markdown("---")
    
    selected_name = st.selectbox(
        "Select Simulated Incident Scenario:",
        list(SCENARIOS.keys())
    )
    current_case = SCENARIOS[selected_name]
    
    st.markdown("---")
    st.write("**Runtime Governance Architecture:**")
    st.markdown("• In-line Guardian Agent: `ACTIVE`\n• Semantic Circuit Breaker: `ARMED`\n• EU AI Act Triage Engine: `ONLINE`")

# --- Header & High-Level State ---
st.title("🛡️ AI Incident Cockpit")
st.markdown(f"**Target System:** `{current_case['system']}` | **Agent ID:** `{current_case['agent_id']}`")

# Metric Status Row
col_stat1, col_stat2, col_stat3 = st.columns(3)
with col_stat1:
    st.markdown(f"**Internal Severity:**<br><span class='badge-critical'>{current_case['severity']}</span>", unsafe_allow_html=True)
with col_stat2:
    st.markdown(f"**Circuit Breaker Status:**<br><span class='badge-critical'>{current_case['circuit_breaker']}</span>", unsafe_allow_html=True)
with col_stat3:
    st.markdown(f"**Incident Timestamp:**<br>`{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC`", unsafe_allow_html=True)

st.markdown("---")

# --- Main Columns: 30-Second Snapshot vs Regulatory Triage ---
col_left, col_right = st.columns([3, 2])

with col_left:
    st.subheader("1. 30-Second Situation Snapshot (Cognitive Sensemaking)")
    
    with st.container():
        st.markdown("**🎯 Agent Original Objective:**")
        st.info(current_case["goal"])
        
        st.markdown("**⚠️ Detected Semantic Divergence:**")
        st.error(current_case["anomaly"])
        
    with st.expander("🔍 View Raw Trace & Tool Execution Telemetry (SRE View)"):
        st.code(current_case["raw_log_sample"], language="text")

with col_right:
    st.subheader("2. Statutory Triage (EU AI Act Assessment)")
    
    st.markdown(f"**Regulatory Incident Status:**")
    if "Serious" in current_case["ai_act_status"]:
        st.error(f"🚨 **{current_case['ai_act_status']}**")
    else:
        st.success(f"✅ **{current_case['ai_act_status']}**")
        
    st.markdown(f"**Legal Article Reference:** `{current_case['ai_act_article']}`")
    st.markdown(f"**Statutory Reporting Window:** `{current_case['reporting_deadline']}`")
    
    st.markdown("""
    > *Note: The automated Circuit Breaker has already severed write permissions and captured a state snapshot to safeguard the environment while awaiting human judgment.*
    """)

st.markdown("---")

# --- Action Footer: Human Decision-Making (Human-on-the-Loop) ---
st.subheader("3. Human Adjudication & Decision Rights")

col_act1, col_act2, col_act3, col_act4 = st.columns(4)

with col_act1:
    if st.button("🛑 Terminate Process", use_container_width=True, type="primary"):
        st.toast(f"Agent {current_case['agent_id']} forcefully terminated.", icon="🛑")
        st.session_state["decision"] = "Full Process Termination (Killed)"

with col_act2:
    if st.button("🔒 Restrict Scope & Resume", use_container_width=True):
        st.toast("Write privileges revoked. Downgraded to read-only sandbox.", icon="🔒")
        st.session_state["decision"] = "Degraded Execution (Read-Only Mode)"

with col_act3:
    if st.button("↩️ Rollback to Snapshot", use_container_width=True):
        st.toast("Restored system state to pre-incident snapshot.", icon="↩️")
        st.session_state["decision"] = "State Rollback (Restored)"

with col_act4:
    if st.button("📄 Generate Post-Mortem", use_container_width=True):
        st.session_state["show_report"] = True

# --- Auto-Generated Post-Mortem Card ---
if st.session_state.get("show_report"):
    st.markdown("---")
    st.subheader("📋 Automated Incident Investigation Report (Executive & Regulatory Draft)")
    decision_made = st.session_state.get("decision", "Awaiting Adjudication")
    
    report_text = f"""
### AI INCIDENT INVESTIGATION REPORT
* **Target System:** {current_case['system']} ({current_case['agent_id']})
* **Timestamp:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC
* **Severity Tier:** {current_case['severity']}
* **EU AI Act Status:** {current_case['ai_act_status']} ({current_case['ai_act_article']})
* **Mandated Reporting Deadline:** {current_case['reporting_deadline']}

1. EVENT SUMMARY & ROOT CAUSE:
{current_case['anomaly']}

2. AUTONOMOUS MITIGATION (GUARDIAN LAYER):
Semantic Circuit Breaker triggered upon unauthorized boundary threshold violation. API privileges suspended at machine speed without service disruption.

3. HUMAN ADJUDICATION OUTCOME:
{decision_made}
    """
    st.text_area("Exportable Post-Mortem Summary:", report_text.strip(), height=220)