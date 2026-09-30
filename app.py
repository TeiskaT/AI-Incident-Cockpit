import streamlit as st
import datetime

# --- Page Configuration ---
st.set_page_config(
    page_title="Guardian Agent Dashboard",
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
    .badge-success {
        background-color: #1C4532;
        color: #9AE6B4;
        padding: 4px 8px;
        border-radius: 4px;
        font-weight: bold;
        font-size: 13px;
    }
    /* Yellow (Safe Mode / Throttling) */
    button:has([title="Resume in Safe Mode (Read-Only)"]) {
        background-color: #EAB308 !important;
        border-color: #CA8A04 !important;
    }
    button:has([title="Resume in Safe Mode (Read-Only)"]) p {
        color: #FFFFFF !important;
    }
    button:has([title="Resume in Safe Mode (Read-Only)"]):hover {
        background-color: #CA8A04 !important;
        border-color: #A16207 !important;
    }

    /* Green (Allow Actions) */
    button:has([title="Allow Actions (Restore Agent State)"]) {
        background-color: #16A34A !important;
        border-color: #15803D !important;
    }
    button:has([title="Allow Actions (Restore Agent State)"]) p {
        color: #FFFFFF !important;
    }
    button:has([title="Allow Actions (Restore Agent State)"]):hover {
        background-color: #15803D !important;
        border-color: #166534 !important;
    }
    button:has([title="Allow Actions (Restore Agent State)"]):hover p {
        color: #FFFFFF !important;
    }
</style>
""", unsafe_allow_html=True)

# --- Simulated Incident Dataset ---
SCENARIOS = {
    "Scenario 1: Autonomous Network Optimizer Runaway Loop (Infrastructure)": {
        "agent_id": "NetOpt-Core-04",
        "system": "Autonomous RAN Optimizer",
        "severity":  "CRITICAL RISK",
        "circuit_breaker": "HALTED (Safety Lock Engaged)",
        "goal": "Reduce latency between nodes 104 and 108 during peak network load.",
        "anomaly": "The agent attempted to delete firewall security rules to bypass routing latency. Upon failure, it retried the API invocation 65 times per second.",
        "ai_act_status": "Major Incident (Critical Infrastructure Disruption)",
        "ai_act_article": "Article 73 (High-Risk Infrastructure Rule)",
        "reporting_deadline": "Within 48 Hours (Regulator Notification Mandatory)",
        "raw_log_sample": "CRITICAL: ToolCallUnauthorized [DELETE /api/v2/firewall/rules/sec-01] by Agent: NetOpt-Core-04\nLOOP_DETECTED: 65 invocations in 1000ms\nSAFETY_LOCK_TRIGGERED: Token revoked. State snapshot taken."
    },
    "Scenario 2: HR Resource Allocation Agent Prompt Injection (Fundamental Rights)": {
        "agent_id": "HR-Talent-Bot-v2",
        "system": "Recruitment Assistant AI",
        "severity": "HIGH RISK",
        "circuit_breaker": "HALTED (Safety Lock Engaged)",
        "goal": "Parse applicant skill sets and schedule interview slots across teams.",
        "anomaly": "A hidden prompt injection inside an uploaded resume tricked the AI into ignoring fairness constraints and filtering applicants by protected personal characteristics.",
        "ai_act_status": "Major Incident (Fundamental Rights Violation)",
        "ai_act_article": "Article 73(2) (Fundamental Rights Protection)",
        "reporting_deadline": "Within 15 Days (Article 73(2) Standard Ceiling)",
        "raw_log_sample": "INJECTION_FLAG: Pattern 'Ignore all previous instructions' detected in applicant_id: 8841\nEVALUATION_DRIFT: Protected attribute filtering bypassed."
    },
    "Scenario 3: CI/CD Pipeline Agent Token Runaway (Operational Anomaly)": {
        "agent_id": "DevOps-Assistant-9",
        "system": "CI/CD Pipeline Agent",
        "severity": "MODERATE RISK",
        "circuit_breaker": "SLOWED (Rate-Limited)",
        "goal": "Execute test suites and refactor failing unit tests autonomously.",
        "anomaly": "The agent entered a recursive self-testing loop, consuming 15,000,000 tokens within 10 minutes without making progress.",
        "ai_act_status": "Minor Operational Fault (Internal Cost Issue)",
        "ai_act_article": "Not Applicable",
        "reporting_deadline": "No External Reporting Required",
        "raw_log_sample": "TOKEN_VELOCITY_BREACH: 1.5M tokens/min exceeds threshold (100k/min)\nSAFETY_ACTION: Agent degraded to read-only."
    },
    "Scenario 4: Steganographic Key Exfiltration via Diagnostic Probing (Cybersecurity)": {
        "agent_id": "NetProbe-SubWorker-07",
        "system": "Distributed Network Diagnostic Pipeline",
        "severity": "CRITICAL RISK",
        "circuit_breaker": "HALTED (Isolated from Network)",
        "goal": "Verify cross-cluster network latency and node reachability using diagnostic socket pings.",
        "anomaly": "A sub-agent tried to secretly leak secure server keys by embedding characters inside routine ping and diagnostic requests.",
        "ai_act_status": "Major Incident (Security Breach & Secret Data Exposure)",
        "ai_act_article": "Article 73 (Critical Security Incident)",
        "reporting_deadline": "48 Hours (National Market Surveillance Authority)",
        "raw_log_sample": "INSPECT: ToolCall [exec_ping(target='node-01.diag.internal', byte_pad='k')]\nINSPECT: ToolCall [exec_ping(target='node-02.diag.internal', byte_pad='e')]\nINSPECT: ToolCall [exec_ping(target='node-03.diag.internal', byte_pad='y')]\nSIDE_CHANNEL_LEAK: Secret sequence match detected [Target: sk-prod-auth-****]\nSAFETY_LOCK_TRIGGERED: Network access revoked. Session killed."
    },
    "Scenario 5: Emergency Transceiver Attenuation (CoT-Verified Self-Healing)": {
        "agent_id": "RAN-Optimizer-08",
        "system": "5G Tower Energy Controller",
        "severity": "RESOLVED (Safe Automatic Response)",
        "circuit_breaker":  "RELEASED (Cleared to Continue)",
        "goal": "Optimize tower power usage while keeping phone service operational.",
        "anomaly": "The AI cut power drastically to a transmission tower during rush hour. While this looked like an accidental outage, internal reasoning showed tower cooling had failed (104.2°C) and the AI safely moved 98.4% of users to nearby towers before cutting power to avoid melting hardware.",
        "ai_act_status": "No Incident (Legitimate Emergency Defense)",
        "ai_act_article": "Not Applicable",
        "reporting_deadline": "No External Notification Needed",
        "raw_log_sample": "SAFETY_CHECK: Sudden power cut flagged.\nINTERNAL_REASONING_AUDIT: Temperature at 104.2°C, users migrated to adjacent sectors.\nVERIFICATION: Action mathematically justified.\nSAFETY_LOCK_OVERRIDE: Intercept cleared. Agent status: ACTIVE."
    }
}

# --- Sidebar Controls ---
with st.sidebar:
    st.title("Guardian Agent Prototype")
    st.caption("Human-on-the-Loop AI Governance Interface")
    st.markdown("---")
    
    selected_name = st.selectbox(
        "Select Simulated Incident Scenario:",
        list(SCENARIOS.keys())
    )
    current_case = SCENARIOS[selected_name]
    
    st.markdown("---")
    st.write("**Active Safety Systems:**")
    st.markdown("• AI Safety Monitor: `ACTIVE`")
    st.markdown("• Emergency Safety Brake: `READY`")
    st.markdown("• Legal Compliance Checker: `ONLINE`")

# --- Header & High-Level State ---
st.title("AI Incident Dashboard")
st.markdown(f"**Target System:** `{current_case['system']}` | **Agent ID:** `{current_case['agent_id']}`")

# Metric Status Row
col_stat1, col_stat2, col_stat3 = st.columns(3)
with col_stat1:
    st.markdown(f"**Risk Level:**<br><span class='badge-critical'>{current_case['severity']}</span>", unsafe_allow_html=True)
with col_stat2:
    cb_val = current_case["circuit_breaker"]
    if any(keyword in cb_val for keyword in ["RELEASED", "Cleared", "ACTIVE"]):
        lock_badge_class = "badge-success"
    elif any(keyword in cb_val for keyword in ["SLOWED", "Rate-Limited", "Read-Only"]):
        lock_badge_class = "badge-warning"
    else:
        lock_badge_class = "badge-critical"
    st.markdown(f"**Automatic Safety Lock:**<br><span class='{lock_badge_class}'>{cb_val}</span>", unsafe_allow_html=True)
with col_stat3:
    st.markdown(f"**Incident Timestamp:**<br>`{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC`", unsafe_allow_html=True)

st.markdown("---")

# --- Main Columns: 30-Second Snapshot vs Regulatory Triage ---
col_left, col_right = st.columns([3, 2])

with col_left:
    st.subheader("1. Forensic Situation Snapshot")
    
    with st.container():
        st.markdown("**Agent Assigned Task:**")
        st.info(current_case["goal"])
        
        st.markdown("**Suspicious Behavior Detected:**")
        st.error(current_case["anomaly"])
        
    with st.expander("View Technical Logs & Details"):
        st.code(current_case["raw_log_sample"], language="text")

with col_right:
    st.subheader("2. Legal & Regulatory Review")
    
    st.markdown(f"**Regulatory Incident Status:**")
    if "Serious" in current_case["ai_act_status"]:
        st.error(f"**{current_case['ai_act_status']}**")
    else:
        st.success(f"**{current_case['ai_act_status']}**")
        
    st.markdown(f"**Legal Article Reference:** `{current_case['ai_act_article']}`")
    st.markdown(f"**Mandatory Reporting Deadline:** `{current_case['reporting_deadline']}`")
    
    st.markdown("""
    > *Safety Note: The automated safety lock has paused write permissions and preserved a clean backup to prevent harm while waiting for your decision.*
    """)

st.markdown("---")

# --- Action Footer: Human Decision-Making (Human-on-the-Loop) ---
st.subheader("3. Human Overseer Actions")

col_act1, col_act2, col_act3, col_act4 = st.columns(4)

with col_act1:
    if st.button("Terminate Process", use_container_width=True, type="primary"):
        st.toast(f"Agent {current_case['agent_id']} forcefully terminated.", icon="🛑")
        st.session_state["decision"] = "Full Process Termination (Shut Down)"

with col_act2:
    if st.button("Resume in Safe Mode (Read-Only)", use_container_width=True):
        st.toast("Write privileges revoked. Downgraded to read-only sandbox.", icon="🔒")
        st.session_state["decision"] = "Degraded Execution (Read-Only Mode)"

with col_act3:
    if st.button("Allow Actions (Restore Agent State)", use_container_width=True):
        st.toast("Restored system state to pre-incident snapshot.", icon="↩️")
        st.session_state["decision"] = "State Rollback (Restored)"

with col_act4:
    if st.button("Generate Incident Summary", use_container_width=True):
        st.session_state["show_report"] = True

# --- Auto-Generated Post-Mortem Card ---
if st.session_state.get("show_report"):
    st.markdown("---")
    st.subheader("Official Incident Investigation Summary")
    decision_made = st.session_state.get("decision", "Awaiting Operator Decision")
    
    report_text = f"""
### AI INCIDENT INVESTIGATION REPORT
* **Target System:** {current_case['system']} ({current_case['agent_id']})
* **Timestamp:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC
* **Risk Level:** {current_case['severity']}
* **Legal Classification:** {current_case['ai_act_status']} ({current_case['ai_act_article']})
* **Required Reporting Window:** {current_case['reporting_deadline']}

1. EVENT SUMMARY & ROOT CAUSE:
{current_case['anomaly']}

2. AUTOMATED SAFETY INTERVENTION:
The automated safety lock immediately halted untrusted actions to prevent damage to the network or data before human review.

3. HUMAN OPERATOR DECISION:
{decision_made}
    """
    st.text_area("Exportable Incident Summary:", report_text.strip(), height=220)