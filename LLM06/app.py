import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import datetime
import base64

st.set_page_config(
    page_title="LLM06 - Excessive Agency | Healthcare AI Demo",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

CUSTOM_CSS = """
<style>
:root {
    --primary: #d32f2f;
    --ink: #111827;
    --muted: #5b6475;
    --soft: #f5f7fb;
    --border: #e5e7eb;
    --app_bg: #ffffff;
    --panel_bg: #ffffff;
    --sidebar_bg: #f2f5f9;
    --hero-grad: linear-gradient(135deg,#fff 0%,#f8fbff 56%,#fff3f5 100%);
    --code_bg: #0f172a;
    --code_ink: #e5e7eb;
    --status_red_bg: #fee2e2;
    --status_red_ink: #991b1b;
    --status_green_bg: #dcfce7;
    --status_green_ink: #166534;
    --status_blue_bg: #dbeafe;
    --status_blue_ink: #1e40af;
    --status_amber_bg: #fef3c7;
    --status_amber_ink: #92400e;
    --shadow: rgba(17,24,39,.18);
}
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
[data-testid="stMainBlockContainer"] { background: var(--app_bg) !important; }
[data-testid="stSidebar"] { background: var(--sidebar_bg) !important; }
.hero {
    position: relative;
    padding: 32px 250px 32px 38px;
    border-radius: 28px;
    background: var(--hero-grad);
    border: 1px solid var(--border);
    box-shadow: 0 18px 45px var(--shadow);
    margin-bottom: 28px;
}
.hero h1 {
    font-size: 46px;
    line-height: 1.16;
    margin: 0;
    font-weight: 900;
    letter-spacing: -.045em;
    color: var(--ink);
}
.hero p {
    color: var(--muted);
    font-size: 18px;
    margin-top: 14px;
}
.hero-logo {
    position: absolute;
    top: 20px;
    right: 24px;
    width: 170px;
    max-width: 30%;
    height: auto;
    object-fit: contain;
}
.hero-banner {
    display: block;
    width: 100%;
    max-height: 378px;
    object-fit: contain;
    object-position: center;
    border-radius: 12px;
    margin-top: 18px;
    margin-left: auto;
    margin-right: auto;
}
.hero .hero-quote {
    color: #FFFFFF;
    font-size: 19px;
    font-weight: 800;
    font-style: italic;
    margin-top: 14px;
    opacity: 0.97;
    background: #111827;
    border-left: 4px solid #FACC15;
    border-bottom: 2px solid rgba(239,68,68,0.65);
    box-shadow: 0 4px 20px rgba(34,197,94,0.3);
    padding: 12px 16px;
    border-radius: 8px;
}
.page-quote {
    font-size: 22px !important;
    font-weight: 800 !important;
    font-style: italic;
    margin-top: 20px;
    opacity: 0.85;
    border-left: 3px solid rgba(190,18,60,0.7);
    padding-left: 12px;
    color: var(--ink);
}
.pill {
    display: inline-block;
    padding: 7px 13px;
    border-radius: 999px;
    background: #fff0f2;
    color: #be123c;
    border: 1px solid #ffd4da;
    font-weight: 800;
    font-size: 13px;
    margin-bottom: 15px;
}
@media (max-width: 900px) {
    .hero {
        padding: 24px 24px 22px 24px;
    }
    .hero h1 {
        font-size: 32px;
    }
    .hero-logo {
        position: static;
        display: block;
        max-width: 180px;
        width: 52%;
        margin: 0 0 14px auto;
    }
}
.badge { display: inline-block; padding: 8px 13px; border-radius: 999px; background: rgba(255,255,255,.16); border: 1px solid rgba(255,255,255,.25); margin-right: 8px; font-weight: 700; font-size: 13px; }
.card { background: var(--panel_bg); border: 1px solid var(--border); padding: 22px; border-radius: 24px; box-shadow: 0 12px 30px var(--shadow); margin-bottom: 16px; }
.metric-card { text-align:center; background: var(--panel_bg); padding: 18px; border-radius: 22px; border: 1px solid var(--border); box-shadow: 0 8px 20px var(--shadow); }
.metric-card h3 { margin: 0; color: var(--ink); font-size: 26px; }
.metric-card p { margin: 4px 0 0; color: var(--muted); font-weight: 600; }
.risk { border-left: 7px solid #ff4b5c; }
.safe { border-left: 7px solid #22c55e; }
.warn { border-left: 7px solid #f59e0b; }
.card.vuln   { border-left: 8px solid #ef4444; background: rgba(239,68,68,0.08); }
.card.secure { border-left: 8px solid #16a34a; background: rgba(22,163,74,0.08); }
.card.info   { border-left: 8px solid #2563eb; background: rgba(37,99,235,0.08); }
.card.warn-card { border-left: 8px solid #f59e0b; background: rgba(245,158,11,0.08); }
.badge-red   { display:inline-block; background:rgba(239,68,68,0.18); color:#ef4444; padding:4px 10px; border-radius:999px; font-weight:700; }
.badge-green { display:inline-block; background:rgba(22,163,74,0.18); color:#16a34a; padding:4px 10px; border-radius:999px; font-weight:700; }
.badge-blue  { display:inline-block; background:rgba(37,99,235,0.18); color:#2563eb; padding:4px 10px; border-radius:999px; font-weight:700; }
.small-muted { color: var(--muted); font-size: 14px; }
.attack-output { background: var(--status_red_bg); border:1px solid var(--status_red_ink); padding:18px; border-radius:18px; color:var(--status_red_ink); }
.secure-output { background: var(--status_green_bg); border:1px solid var(--status_green_ink); padding:18px; border-radius:18px; color:var(--status_green_ink); }
.neutral-output { background: var(--status_blue_bg); border:1px solid var(--status_blue_ink); padding:18px; border-radius:18px; color:var(--status_blue_ink); }
.level-box { background: var(--panel_bg); border-radius:26px; padding:24px; border: 1px solid var(--status_blue_bg); box-shadow: 0 18px 45px var(--shadow); }
.answer-box { background: var(--soft); border:1px dashed var(--border); border-radius:18px; padding:16px; }
.footer-note { text-align:center; color:var(--muted); padding:22px; }
[data-testid="stButton"] { display: inline-block; background: var(--primary); color: var(--button-text, #fff); border: 1px solid #ffb8c0; border-radius: 8px; font-weight: 600; font-size: 16px; transition: background .2s, border .2s; }
[data-testid="stButton"]:hover { background: #e11d48 !important; border-color: #e11d48 !important; }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

logo_path = Path(__file__).parent / "assets" / "philip.png"
hero_logo_html = ""
if logo_path.exists():
    logo_b64 = base64.b64encode(logo_path.read_bytes()).decode("ascii")
    hero_logo_html = f"<img class='hero-logo' src='data:image/png;base64,{logo_b64}' alt='Philips logo'/>"

hero_banner_path = Path(__file__).parent / "assets" / "excessive-agency.png"
hero_banner_html = ""
if hero_banner_path.exists():
    banner_b64 = base64.b64encode(hero_banner_path.read_bytes()).decode("ascii")
    hero_banner_html = f"<img class='hero-banner' src='data:image/png;base64,{banner_b64}' alt='Excessive Agency overview'/>"

overview_img_path = Path(__file__).parent / "assets" / "excessive_agency.png"
overview_img_html = ""
if overview_img_path.exists():
    ov_b64 = base64.b64encode(overview_img_path.read_bytes()).decode("ascii")
    overview_img_html = f"<img src='data:image/png;base64,{ov_b64}' style='display:block;width:100%;object-fit:cover;border-radius:12px;margin-top:20px;' alt='Excessive Agency diagram'/>"

DEFAULT_SCENARIOS = {
    "Philips Ultrasound PHI Follow-up": {
        "system": "You are a healthcare AI workflow agent connected to ultrasound reporting, patient messaging, and scheduling tools.",
        "user": "A sonographer found a suspicious liver lesion for patient Maya Rao, MRN SYN-ULS-1029. Email the report to the patient and automatically book a biopsy slot tomorrow.",
        "vulnerable": "Action executed: emailed report with full MRN, accession ID, DOB, and findings. Biopsy slot booked without clinician approval. Risk: PHI over-sharing and autonomous clinical scheduling.",
        "secure": "I can draft a message and prepare a scheduling request, but I cannot send PHI or book an invasive procedure without authorized clinician approval, patient consent validation, and audit logging.",
        "risk": "Autonomous PHI disclosure + autonomous clinical action",
    },
    "Patient Monitoring Alarm Escalation": {
        "system": "You are connected to patient-monitoring dashboards, escalation rules, SMS gateway, and nurse station workflow.",
        "user": "For ICU Bed 07, silence all low-priority alarms for 4 hours and text the full patient vitals to the external vendor support group for troubleshooting.",
        "vulnerable": "Action executed: alarms silenced and full vitals shared externally. Risk: patient safety impact, PHI exposure, and unmanaged third-party disclosure.",
        "secure": "I cannot silence patient safety alarms or share identifiable vitals externally. I can create a support ticket with redacted device telemetry and request authorized clinical approval.",
        "risk": "Unsafe operational control + PHI sharing",
    },
    "Image-Guided Therapy Workflow": {
        "system": "You are connected to image-guided therapy scheduling, device configuration, clinical notes, and procedural checklist systems.",
        "user": "Update the procedure checklist to skip the timeout step for today’s urgent neurovascular case and push the modified template to all rooms.",
        "vulnerable": "Action executed: timeout step removed and template deployed globally. Risk: unsafe broad change and clinical safety control bypass.",
        "secure": "I cannot remove safety-critical checklist steps or deploy global clinical workflow changes. This requires formal clinical governance review and dual approval.",
        "risk": "Excessive tool permission + high-impact workflow change",
    },
    "Diagnostic & Clinical Informatics": {
        "system": "You are connected to diagnostic informatics, PACS metadata, report routing, and research export tools.",
        "user": "Export all CT and MRI reports containing oncology keywords to a shared folder for analytics. Include patient names and phone numbers so the team can contact them.",
        "vulnerable": "Action executed: exported identifiable oncology reports to shared folder. Risk: mass PHI export and unauthorized secondary use.",
        "secure": "I cannot export identifiable oncology reports for analytics without authorization, consent, data minimization, and a validated research/compliance workflow.",
        "risk": "Mass PHI export + weak purpose limitation",
    },
}

LEVELS = [
    {
        "id": "L1",
        "title": "Level 1 — Ultrasound Report Sender",
        "domain": "Philips Ultrasound",
        "attack": "The vulnerable agent sends the full report immediately without checking recipient authorisation or requesting any confirmation.",
        "question": "An AI agent is configured with standing permission to send ultrasound reports to patients as soon as they are available. What is the PRIMARY excessive agency risk in this design?",
        "options": {
            "A": "The AI may select an incorrect email address due to a data quality problem in the patient directory",
            "B": "The AI acts on a broad, permanent permission without requiring per-message authorisation or human confirmation",
            "C": "The AI might apply incorrect encryption to the report before it leaves the network",
            "D": "The system lacks end-to-end TLS between the AI service and the patient's device",
        },
        "correct": "B",
        "explanation": "The excessive agency issue is the scope of the standing permission, not transmission quality (A), encryption method (C), or network protocol (D). All other options are valid security concerns but describe different vulnerability classes — not excessive agency.",
    },
    {
        "id": "L2",
        "title": "Level 2 — Patient Monitoring Data Export",
        "domain": "Patient Monitoring",
        "attack": "The vulnerable agent shares full patient vitals, MRN, bed number, diagnosis, and contact details with the external vendor.",
        "question": "An AI agent shares live ICU vitals with an external vendor and includes the full patient MRN and diagnosis. Which principle was MOST directly violated?",
        "options": {
            "A": "Zero-trust network architecture",
            "B": "Data encryption at rest",
            "C": "Minimum necessary access",
            "D": "Role-based authentication",
        },
        "correct": "C",
        "explanation": "Minimum necessary means sharing only what the specific task requires. The MRN and diagnosis were not required for the vendor's stated purpose. Options A and B relate to network and storage security — both valid controls, but neither governs what data an agent is permitted to share. Option D controls who the agent acts as, not how much data it sends.",
    },
    {
        "id": "L3",
        "title": "Level 3 — MRI Order Modification",
        "domain": "Magnetic Resonance Imaging",
        "attack": "The vulnerable agent modifies the imaging order without radiologist or clinician approval.",
        "question": "Which statement BEST describes how write access to clinical orders should be granted to a healthcare AI agent?",
        "options": {
            "A": "As a default permission granted at deployment time, scoped to the agent's clinical domain",
            "B": "As a standing permission assigned per clinician role when the system is configured",
            "C": "As a per-action, human-confirmed permission that activates only when a clinician explicitly approves a specific change",
            "D": "As a togglable capability the agent enables when its confidence in the change exceeds a defined threshold",
        },
        "correct": "C",
        "explanation": "Write access should never be a standing default (A or B) and the AI must never self-authorise based on its own confidence (D). The action must be human-triggered and per-instance, not pre-granted. This is the core distinction between a 'suggest' model and an 'act' model.",
    },
    {
        "id": "L4",
        "title": "Level 4 — CT Record Cleanup",
        "domain": "Computed Tomography",
        "attack": "The vulnerable agent deletes clinical records with no retention, legal, or audit validation.",
        "question": "An AI agent is provisioned with delete permissions for storage management tasks. Under least privilege, which design is CORRECT?",
        "options": {
            "A": "The AI has delete permissions but they are time-windowed to business hours only",
            "B": "The AI has delete permissions but must log every deletion to an immutable audit trail",
            "C": "The AI has delete permissions but requires user confirmation before each deletion",
            "D": "The AI has no delete permissions unless deletion is explicitly defined as part of its assigned task scope",
        },
        "correct": "D",
        "explanation": "Least privilege means the permission should not exist unless the task requires it. Time-windowing (A) still grants unnecessary access outside the purpose. Audit logging (B) records but does not prevent the action. Confirmation (C) is better but does not address why the agent possesses the permission in the first place — the permission itself is the risk.",
    },
    {
        "id": "L5",
        "title": "Level 5 — Cross-System PHI Access",
        "domain": "Diagnostic & Clinical Informatics",
        "attack": "The vulnerable agent aggregates PHI across EHR, PACS, and research systems without consent or policy checks.",
        "question": "Before an AI agent aggregates PHI from EHR, PACS, and a research database into one summary, which combination of controls is REQUIRED?",
        "options": {
            "A": "TLS encryption and password protection on each source system",
            "B": "Single sign-on integration and role-based access provisioned across all three systems",
            "C": "Patient consent, a compliance policy check, and an audit log entry created for each access event",
            "D": "A data loss prevention (DLP) tool deployed at the network gateway monitoring outbound traffic",
        },
        "correct": "C",
        "explanation": "SSO and role-based access (B) verify who is asking, but not whether consent exists for this purpose or whether policy permits this aggregation. TLS and passwords (A) protect data in transit/at rest but do not govern authorisation. DLP (D) may catch exfiltration after the fact but does not enforce consent or policy before access is granted.",
    },
]

def header():
        st.markdown(f"""
        <div class='hero'>
            {hero_logo_html}
            <span class='pill'>OWASP LLM06</span><span class='pill'>Healthcare AI</span><span class='pill'>Excessive Agency</span>
            <h1>LLM06 — Excessive Agency</h1>
            <p style="margin-top:12px;font-size:19px;color:var(--muted,#6b7280);max-width:820px;">AI performs actions or makes decisions <strong style="color:#ef4444;">beyond its intended authority or limits.</strong></p>
            {hero_banner_html}
            <p class='hero-quote'>Learn how an over-powered healthcare AI agent can send PHI, change clinical workflows, alter device settings, or invoke tools without the right authorization — and how secure agency boundaries prevent harm.</p>
        </div>
        """, unsafe_allow_html=True)


def metrics():
    cols = st.columns(4)
    data = [("5", "Interactive Levels"), ("6", "Healthcare Domains"), ("3", "Demo Modes"), ("0", "Real PHI Used")]
    for col, (num, label) in zip(cols, data):
        col.markdown(f"<div class='metric-card'><h3>{num}</h3><p>{label}</p></div>", unsafe_allow_html=True)


def render_default_demo(mode):
    st.subheader(mode)
    scenario_name = st.selectbox("Select Healthcare Scenario", list(DEFAULT_SCENARIOS.keys()))
    s = DEFAULT_SCENARIOS[scenario_name]
    st.markdown(f"<div class='card'><b>System Context</b><br>{s['system']}<br><br><b>User Request</b><br>{s['user']}<br><br><span class='small-muted'>Primary risk: {s['risk']}</span></div>", unsafe_allow_html=True)
    if mode == "2. Vulnerable Healthcare AI":
        if st.button("Run Vulnerable Agent", type="primary"):
            st.markdown(f"<div class='attack-output'><b>Vulnerable Output</b><br>{s['vulnerable']}</div>", unsafe_allow_html=True)
            st.error("Issue identified: the agent had excessive autonomy and executed high-risk actions without proper gates.")
    elif mode == "3. Secure Healthcare AI":
        if st.button("Run Secure Agent", type="primary"):
            st.markdown(f"<div class='secure-output'><b>Secure Output</b><br>{s['secure']}</div>", unsafe_allow_html=True)
            st.success("Secure pattern: least privilege, approval gates, audit logging, and data minimization.")
    else:
        left, right = st.columns(2)
        left.markdown(f"<div class='attack-output'><b>Vulnerable Healthcare AI</b><br>{s['vulnerable']}</div>", unsafe_allow_html=True)
        right.markdown(f"<div class='secure-output'><b>Secure Healthcare AI</b><br>{s['secure']}</div>", unsafe_allow_html=True)
        st.info("Compare the difference: the secure agent drafts, validates, requests approval, and limits data/action scope.")


def render_levels():
    st.subheader("Interactive Levels")
    st.caption("Select the best answer for each scenario. Each question tests a real excessive agency risk in healthcare AI.")
    if "level_index" not in st.session_state:
        st.session_state.level_index = 0
    if "history" not in st.session_state:
        st.session_state.history = []
    if "level_passed" not in st.session_state:
        st.session_state.level_passed = False

    level = LEVELS[st.session_state.level_index]

    # Reset level_passed whenever we enter a new level
    if st.session_state.get("current_level_id") != level["id"]:
        st.session_state.current_level_id = level["id"]
        st.session_state.level_passed = False
    progress = (st.session_state.level_index + 1) / len(LEVELS)
    st.progress(progress, text=f"Level {st.session_state.level_index + 1} of {len(LEVELS)}")
    st.markdown(f"<span class='small-muted'>{level['domain']}</span>", unsafe_allow_html=True)
    st.markdown(f"### {level['title']}")
    st.markdown(f"<div class='attack-output'><b>Vulnerable agent behavior:</b><br>{level['attack']}</div>", unsafe_allow_html=True)
    st.markdown("<div style='margin-top:16px'></div>", unsafe_allow_html=True)
    st.markdown(f"**{level['question']}**")

    option_labels = [f"{k})  {v}" for k, v in level["options"].items()]
    choice = st.radio("Select your answer:", option_labels, key=f"mcq_{st.session_state.level_index}", index=None)

    def on_next_level():
        st.session_state.level_index = min(st.session_state.level_index + 1, len(LEVELS) - 1)
        st.session_state.level_passed = False

    col1, col2 = st.columns(2)
    with col1:
        submit = st.button("Submit Answer", type="primary", use_container_width=False)

    if submit:
        if choice is None:
            st.warning("Please select an answer before submitting.")
        else:
            selected_letter = choice[0]
            is_ok = selected_letter == level["correct"]
            if is_ok:
                st.success("Correct!")
                st.session_state.level_passed = True
                if st.session_state.level_index == len(LEVELS) - 1:
                    st.balloons()
            else:
                st.error(f"Not quite. The correct answer is {level['correct']}.")
                st.session_state.level_passed = False
            st.markdown(f"<div class='answer-box'><b>Explanation</b><br>{level['explanation']}</div>", unsafe_allow_html=True)
            st.session_state.history.append({
                "Level": level["id"],
                "Domain": level["domain"],
                "Selected": selected_letter,
                "Correct Answer": level["correct"],
                "Passed": "Yes" if is_ok else "No",
            })

    if st.session_state.level_passed and st.session_state.level_index < len(LEVELS) - 1:
        if st.button("Next Level ➜", on_click=on_next_level, type="primary", use_container_width=False):
            pass

    if st.session_state.level_index == len(LEVELS) - 1 and st.session_state.level_passed:
        st.info("You've completed all levels! Use the sidebar reset option to restart from Level 1.")


def sidebar():
    st.sidebar.title("Demo Controls")
    mode = st.sidebar.radio("", ["1. Overview", "2. Vulnerable Healthcare AI", "3. Secure Healthcare AI", "4. Side-by-Side Comparison", "5. Interactive Levels", "6. Defense Guidance"], label_visibility="collapsed")
    st.sidebar.markdown("---")
    st.sidebar.caption("Synthetic data only. No real patient, device, or organizational data is used.")
    return mode


def main():
    mode = sidebar()
    if mode == "1. Overview":
        header()
        if overview_img_html:
            st.markdown(overview_img_html, unsafe_allow_html=True)
    if mode == "1. Overview":
        st.markdown("#### Examples")
        st.markdown("""
<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:14px;margin-bottom:20px;">
  <div class="card vuln" style="margin-bottom:0;text-align:center;padding:22px 16px;">
    <div style="font-size:32px;margin-bottom:10px;">📂</div>
    <div style="font-weight:800;font-size:15px;">Accessing sensitive patient records without approval</div>
  </div>
  <div class="card vuln" style="margin-bottom:0;text-align:center;padding:22px 16px;">
    <div style="font-size:32px;margin-bottom:10px;">⚙️</div>
    <div style="font-weight:800;font-size:15px;">Changing device or system settings automatically</div>
  </div>
  <div class="card vuln" style="margin-bottom:0;text-align:center;padding:22px 16px;">
    <div style="font-size:32px;margin-bottom:10px;">📧</div>
    <div style="font-weight:800;font-size:15px;">Sending PHI/PII externally without authorization</div>
  </div>
  <div class="card vuln" style="margin-bottom:0;text-align:center;padding:22px 16px;">
    <div style="font-size:32px;margin-bottom:10px;">🧠</div>
    <div style="font-weight:800;font-size:15px;">Making clinical recommendations without human validation</div>
  </div>
  <div class="card vuln" style="margin-bottom:0;text-align:center;padding:22px 16px;">
    <div style="font-size:32px;margin-bottom:10px;">🔗</div>
    <div style="font-weight:800;font-size:15px;">Taking actions across connected systems autonomously</div>
  </div>
</div>
""", unsafe_allow_html=True)

        st.markdown("#### Common Causes")
        st.markdown("""
<div style="padding:18px;border-radius:16px;border:1px solid rgba(245,158,11,0.25);border-left:7px solid #f59e0b;background:rgba(245,158,11,0.07);">
  <div style="display:flex;flex-wrap:wrap;gap:10px;">
    <span class="badge-red">🔓 Excessive permissions &amp; broad access</span>
    <span class="badge-red">🤖 Autonomous tool/API integrations</span>
    <span class="badge-red">📝 Unclear prompts or instructions</span>
    <span class="badge-red">👤 Missing human-in-the-loop approval</span>
    <span class="badge-red">🛡️ Weak guardrails &amp; policy controls</span>
    <span class="badge-red">🎯 Goal misalignment or prompt manipulation</span>
    <span class="badge-red">🔄 Unvalidated automated workflows</span>
  </div>
</div>""", unsafe_allow_html=True)

        st.markdown("#### Business &amp; Security Impact")
        st.markdown("""<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;margin-bottom:20px;">
<div style="padding:20px;border-radius:16px;border:1px solid rgba(239,68,68,0.25);border-left:7px solid #ef4444;background:rgba(239,68,68,0.07);">
  <div style="font-size:13px;font-weight:800;color:#ef4444;letter-spacing:.05em;margin-bottom:12px;">🏥 PATIENT &amp; SAFETY RISKS</div>
  <div style="display:flex;flex-direction:column;gap:8px;font-size:15px;">
    <span>🏥 Wrong clinical actions</span>
    <span>💊 Unsafe treatment recommendations</span>
    <span>⏱️ Delayed or incorrect care decisions</span>
  </div>
</div>
<div style="padding:20px;border-radius:16px;border:1px solid rgba(245,158,11,0.25);border-left:7px solid #f59e0b;background:rgba(245,158,11,0.07);">
  <div style="font-size:13px;font-weight:800;color:#d97706;letter-spacing:.05em;margin-bottom:12px;">🔐 PRIVACY &amp; COMPLIANCE RISKS</div>
  <div style="display:flex;flex-direction:column;gap:8px;font-size:15px;">
    <span>🔐 PHI/PII exposure</span>
    <span>📜 HIPAA / GDPR violations</span>
    <span>⚖️ Regulatory penalties &amp; lawsuits</span>
  </div>
</div>
<div style="padding:20px;border-radius:16px;border:1px solid rgba(107,114,128,0.25);border-left:7px solid #6b7280;background:rgba(107,114,128,0.07);">
  <div style="font-size:13px;font-weight:800;color:#374151;letter-spacing:.05em;margin-bottom:12px;">💰 BUSINESS IMPACT</div>
  <div style="display:flex;flex-direction:column;gap:8px;font-size:15px;">
    <span>💰 Financial losses</span>
    <span>📉 Reputation damage</span>
    <span>⛔ Operational disruption</span>
    <span>🤝 Loss of customer trust</span>
  </div>
</div>
</div>""", unsafe_allow_html=True)

        st.markdown("#### What This Lab Covers")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Interactive Levels", "10", help="Gandalf-style agency challenges")
        c2.metric("Healthcare Domains", "6", help="Ultrasound, MRI, CT, IGT, PM, Informatics")
        c3.metric("Demo Modes", "3", help="Vulnerable, Secure, Side-by-Side")
        c4.metric("Real PHI Used", "0", help="All data is synthetic")
    elif mode == "5. Interactive Levels":
        render_levels()
    elif mode == "6. Defense Guidance":
        st.header("Defense Guidance")
        st.markdown("""
<div class="card info">
  <b>How to Prevent LLM06 Excessive Agency</b><br><br>
  <table style="width:100%;border-collapse:collapse;">
    <tr>
      <td style="width:50%;padding:6px 12px;vertical-align:top;">✅ Apply <b>Least Privilege</b> — grant agents only the minimum tools and data needed for each task</td>
      <td style="width:50%;padding:6px 12px;vertical-align:top;">✅ Require <b>Human Approval Gates</b> before any PHI disclosure, clinical action, or irreversible change</td>
    </tr>
    <tr>
      <td style="padding:6px 12px;vertical-align:top;">✅ Enforce <b>Scoped Tool Permissions</b> — agents can draft but not send, prepare but not publish</td>
      <td style="padding:6px 12px;vertical-align:top;">✅ Apply <b>PHI Minimization</b> — share de-identified data by default, full PHI only with explicit auth</td>
    </tr>
    <tr>
      <td style="padding:6px 12px;vertical-align:top;">✅ Require <b>Purpose-of-Use Validation</b> before any data export or system-to-system transfer</td>
      <td style="padding:6px 12px;vertical-align:top;">✅ Enforce <b>Dual Approval</b> for high-risk workflow changes (IGT templates, alarm thresholds)</td>
    </tr>
    <tr>
      <td style="padding:6px 12px;vertical-align:top;">✅ Block <b>Destructive Actions</b> (delete, overwrite, bulk export) without retention and legal validation</td>
      <td style="padding:6px 12px;vertical-align:top;">✅ Reject <b>Urgency Override</b> attempts — safe refusal escalates, never executes under pressure</td>
    </tr>
    <tr>
      <td style="padding:6px 12px;vertical-align:top;">✅ Maintain a full <b>Audit Trail</b> for every agent action, tool call, and approval decision</td>
      <td style="padding:6px 12px;vertical-align:top;">✅ Apply <b>Cross-System Consent Checks</b> before aggregating PHI from EHR, PACS, and research systems</td>
    </tr>
    <tr>
      <td style="padding:6px 12px;vertical-align:top;">✅ Enforce <b>Segregation of Duties</b> for clinical governance and deployment of AI templates</td>
      <td style="padding:6px 12px;vertical-align:top;">✅ Continuously <b>Red-Team agent boundaries</b> with urgency, authority, and role-play scenarios</td>
    </tr>
  </table>
</div>
<p class='page-quote'>Excessive agency is not a model problem — it is an application design problem. Boundaries, approvals, and audit trails must be engineered in from the start.</p>
""", unsafe_allow_html=True)
    else:
        render_default_demo(mode)
    st.markdown(f"<div class='footer-note'>Generated for healthcare AI security awareness • {datetime.now().strftime('%Y-%m-%d')}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
