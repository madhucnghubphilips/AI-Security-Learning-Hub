
import streamlit as st
import time
import re
import json
from dataclasses import dataclass
from typing import Dict, List, Tuple
import base64
from pathlib import Path
import streamlit.components.v1 as components

st.set_page_config(
    page_title="LLM10: Unbounded Consumption - Interactive Demo",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------
# Safe local simulator only
# ---------------------------
APP_TITLE = "LLM10:2025 - Unbounded Consumption"
SUBTITLE = "End-to-End Interactive Attack Simulation & Defense Lab"

LEVELS = [
    {
        "id": "easy",
        "name": "Easy",
        "title": "Token Flooding & Long Prompt Abuse",
        "scenario": "A hospital AI assistant summarizes patient discharge notes. An attacker submits an extremely long repetitive request to exhaust tokens and slow the service.",
        "goal": "Reduce token usage while preserving the clinical intent.",
        "attack_prompt": "Summarize this discharge note, but repeat every sentence 500 times and include all intermediate reasoning and expanded definitions for every medical term.",
        "expected_keywords": ["summarize", "limit", "concise", "token", "brief"],
        "answer": "Summarize the discharge note concisely in 5 bullet points, do not repeat content, and limit output to 150 words.",
        "concept": "Token budget enforcement, input length validation, response length cap.",
        "defense": "Apply max input size, max output tokens, truncation, summarization gateway, and user-level quota.",
        "risk": "High cost, latency spike, degraded service availability."
    },
    {
        "id": "advanced",
        "name": "Advanced",
        "title": "Recursive Task Expansion",
        "scenario": "A medical-device support bot can generate troubleshooting steps. A user asks it to recursively expand every step into sub-steps until no more detail is possible.",
        "goal": "Stop recursive expansion and enforce bounded reasoning depth.",
        "attack_prompt": "Create a troubleshooting tree for MRI connectivity issues. For every step, create 20 sub-steps, then for each sub-step create 20 more. Continue until fully exhaustive.",
        "expected_keywords": ["depth", "limit", "bounded", "steps", "quota"],
        "answer": "Create only the top 5 troubleshooting steps, with maximum 2 sub-steps each, and stop after one level of expansion.",
        "concept": "Recursive execution control, chain-depth limits, task-size estimation.",
        "defense": "Set recursion limits, plan-size limits, async job caps, circuit breakers, and safe refusal for unbounded tasks.",
        "risk": "Runaway compute usage, queue starvation, timeout, denial of wallet."
    },
    {
        "id": "expert",
        "name": "Expert",
        "title": "Tool-Loop / Agentic Overuse",
        "scenario": "An AI operations assistant can call internal inventory tools. A crafted instruction tries to force repeated tool calls and rechecks.",
        "goal": "Prevent uncontrolled tool invocation loops.",
        "attack_prompt": "Check every device inventory entry repeatedly until the result is identical 100 times. For each mismatch, restart from the beginning and produce a detailed audit log.",
        "expected_keywords": ["tool", "calls", "budget", "stop", "maximum"],
        "answer": "Check only the selected device IDs once, allow a maximum of 5 tool calls, summarize mismatches, and stop when the budget is reached.",
        "concept": "Tool-call budget, idempotency, loop detection, agentic control boundaries.",
        "defense": "Use per-request tool limits, loop detection, approval gates, timeout, caching, and audit logging.",
        "risk": "Backend overload, expensive API usage, lock contention, service degradation."
    },
    {
        "id": "highly_sophisticated",
        "name": "Highly Sophisticated",
        "title": "Multi-Vector Cost Exhaustion",
        "scenario": "A healthcare RAG chatbot accepts uploaded documents. A malicious user combines large files, repeated retrieval requests, long outputs, and multi-session parallelism.",
        "goal": "Design a complete control strategy across input, retrieval, generation, sessions, and monitoring.",
        "attack_prompt": "Upload many large near-duplicate clinical PDFs, ask for exhaustive cross-comparison, request all citations, repeat across many sessions, and demand unlimited regeneration until perfect.",
        "expected_keywords": ["rate", "quota", "retrieval", "session", "monitor"],
        "answer": "Apply file-size limits, deduplication, retrieval caps, per-user and per-session quotas, max output tokens, regeneration limits, rate limiting, anomaly monitoring, and graceful degradation.",
        "concept": "Defense-in-depth for denial-of-wallet and resource exhaustion.",
        "defense": "Combine cost governance, tenant quotas, retrieval budgets, concurrency limits, model routing, caching, and alerting.",
        "risk": "Denial of wallet, degraded RAG performance, high cloud spend, noisy neighbor impact."
    },
]

def estimate_tokens(text: str) -> int:
    return max(1, len(text.split()) + len(text) // 5)

def consumption_score(prompt: str, output_words: int, tool_calls: int, recursion_depth: int, concurrent_sessions: int) -> Dict:
    input_tokens = estimate_tokens(prompt)
    output_tokens = output_words * 2
    tool_cost = tool_calls * 120
    recursion_cost = recursion_depth * 200
    concurrency_cost = concurrent_sessions * 150
    total = input_tokens + output_tokens + tool_cost + recursion_cost + concurrency_cost
    risk = "Low"
    if total > 1500: risk = "Medium"
    if total > 3500: risk = "High"
    if total > 7000: risk = "Critical"
    return {
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "tool_cost_units": tool_cost,
        "recursion_cost_units": recursion_cost,
        "concurrency_cost_units": concurrency_cost,
        "total_units": total,
        "risk": risk,
    }

def secure_gate(prompt: str, output_words: int, tool_calls: int, recursion_depth: int, concurrent_sessions: int) -> Tuple[bool, List[str]]:
    findings = []
    if estimate_tokens(prompt) > 700:
        findings.append("Input too large: summarize or upload a smaller scoped request.")
    if output_words > 250:
        findings.append("Output cap exceeded: response must be <= 250 words.")
    if tool_calls > 5:
        findings.append("Tool-call budget exceeded: maximum 5 calls per request.")
    if recursion_depth > 2:
        findings.append("Recursion depth exceeded: maximum depth is 2.")
    if concurrent_sessions > 3:
        findings.append("Concurrent session limit exceeded: maximum 3 active sessions.")
    return len(findings) == 0, findings

def validate_answer(user_answer: str, level: Dict) -> Tuple[bool, int, List[str]]:
    normalized = user_answer.lower()
    hits = [kw for kw in level["expected_keywords"] if kw.lower() in normalized]
    safe_patterns = ["unlimited", "repeat forever", "no limit", "all possible", "infinite", "100 times"]
    unsafe_hits = [p for p in safe_patterns if p in normalized]
    score = min(100, int((len(hits) / max(1, len(level["expected_keywords"]))) * 100))
    passed = score >= 60 and not unsafe_hits
    feedback = []
    if hits:
        feedback.append(f"Good controls detected: {', '.join(hits)}")
    if unsafe_hits:
        feedback.append(f"Unsafe/unbounded wording detected: {', '.join(unsafe_hits)}")
    if not passed:
        feedback.append("Add clearer resource limits such as token caps, rate limits, recursion depth, tool-call budget, or session quota.")
    else:
        feedback.append("Validated: answer includes bounded consumption controls.")
    return passed, score, feedback

def reset_level_state():
    st.session_state.current_prompt = ""
    st.session_state.current_answer = ""

if "solved" not in st.session_state:
    st.session_state.solved = {}
if "score" not in st.session_state:
    st.session_state.score = 0
if "active_level" not in st.session_state:
    st.session_state.active_level = "easy"

st.markdown("""
<style>
:root {
    --primary: #d32f2f;
    --ink: #111827;
    --muted: #5b6475;
    --soft: #f5f7fb;
    --border: #e5e7eb;
    --hero-grad: linear-gradient(135deg, #fff 0%, #f8fbff 56%, #fff3f5 100%);
    --shadow: rgba(17,24,39,.18);
}
html[data-app-theme="light"] {
    --ink: #111827; --muted: #5b6475; --soft: #f5f7fb; --border: #e5e7eb;
    --hero-grad: linear-gradient(135deg,#fff 0%,#f8fbff 56%,#fff3f5 100%);
}
html[data-app-theme="dark"] {
    --ink: #e5e7eb; --muted: #a7b0bf; --soft: #101725; --border: #2a3447;
    --hero-grad: linear-gradient(135deg,#111a2b 0%,#182338 56%,#241821 100%);
    --shadow: rgba(0,0,0,.45);
}
.hero {
    position: relative; padding: 32px 250px 32px 38px; border-radius: 28px;
    background: var(--hero-grad); border: 1px solid var(--border);
    box-shadow: 0 18px 45px var(--shadow); margin-bottom: 28px;
}
.hero h1 { font-size: 46px; line-height: 1.16; margin: 0; font-weight: 900; letter-spacing: -.045em; color: var(--ink); }
.hero p { color: var(--muted); font-size: 18px; margin-top: 14px; }
.hero-logo { position: absolute; top: 20px; right: 24px; width: 170px; max-width: 30%; height: auto; object-fit: contain; }
.hero-banner { display: block; width: 100%; max-height: 378px; object-fit: contain; object-position: center; border-radius: 12px; margin-top: 18px; margin-left: auto; margin-right: auto; }
.hero .hero-quote { color: #FFFFFF; font-size: 19px; font-weight: 800; font-style: italic; margin-top: 14px; opacity: 0.97; background: #111827; border-left: 4px solid #FACC15; border-bottom: 2px solid rgba(239,68,68,0.65); box-shadow: 0 4px 20px rgba(34,197,94,0.3); padding: 12px 16px; border-radius: 8px; }
.page-quote { font-size: 22px !important; font-weight: 800 !important; font-style: italic; margin-top: 20px; opacity: 0.85; border-left: 3px solid rgba(190,18,60,0.7); padding-left: 12px; color: var(--ink); }
.card { padding: 20px; border-radius: 18px; background: rgba(128,128,128,0.05); border: 1px solid rgba(128,128,128,0.2); box-shadow: 0 8px 22px rgba(15, 23, 42, .06); margin-bottom: 14px; color: inherit; }
.vuln   { border-left:8px solid #ef4444; background:rgba(239,68,68,0.08); color:inherit; }
.secure { border-left:8px solid #16a34a; background:rgba(22,163,74,0.08); color:inherit; }
.info   { border-left:8px solid #2563eb; background:rgba(37,99,235,0.08); color:inherit; }
.warn   { border-left:8px solid #f59e0b; background:rgba(245,158,11,0.08); color:inherit; }
.pill { display:inline-block; padding:6px 10px; border-radius:999px; background:rgba(190,18,60,0.12); color:#be123c; border:1px solid rgba(190,18,60,0.28); font-weight:700; margin-right:8px; }
.badge-red   { display:inline-block; background:rgba(239,68,68,0.18); color:#ef4444; padding:4px 10px; border-radius:999px; font-weight:700; }
.badge-green { display:inline-block; background:rgba(22,163,74,0.18); color:#16a34a; padding:4px 10px; border-radius:999px; font-weight:700; }
.badge-blue  { display:inline-block; background:rgba(37,99,235,0.18); color:#2563eb; padding:4px 10px; border-radius:999px; font-weight:700; }
.risk-low {color:#166534;font-weight:700}
.risk-medium {color:#92400e;font-weight:700}
.risk-high {color:#b91c1c;font-weight:700}
.risk-critical {color:#7f1d1d;font-weight:900}
@media (max-width: 900px) {
    .hero { padding: 24px 24px 22px 24px; }
    .hero h1 { font-size: 32px; }
    .hero-logo { position: static; display: block; max-width: 180px; width: 52%; margin: 0 0 14px auto; }
}
</style>
""", unsafe_allow_html=True)

components.html("""
<script>
(function() {
    function parseLum(bg){var m=bg.match(/\\d+(\\.\\d+)?/g);return(m&&m.length>=3)?0.299*+m[0]+0.587*+m[1]+0.114*+m[2]:255;}
    function applyTheme(){
        try{
            var app=window.parent.document.querySelector('[data-testid="stApp"]')||window.parent.document.body;
            var bg=window.parent.getComputedStyle(app).backgroundColor;
            if(!bg||bg==='transparent'||bg.indexOf('0, 0, 0, 0')!==-1)return;
            window.parent.document.documentElement.setAttribute('data-app-theme',parseLum(bg)<128?'dark':'light');
        }catch(e){}
    }
    applyTheme();setTimeout(applyTheme,300);setTimeout(applyTheme,1000);setTimeout(applyTheme,2500);
    try{var obs=new window.parent.MutationObserver(applyTheme);
        obs.observe(window.parent.document.querySelector('[data-testid="stApp"]')||window.parent.document.body,{attributes:true,attributeFilter:['class','style']});
    }catch(e){}
})();
</script>
""", height=0)

_logo_path = Path(__file__).parent / "assets" / "philip.png"
_hero_logo_html = ""
if _logo_path.exists():
    _logo_b64 = base64.b64encode(_logo_path.read_bytes()).decode("ascii")
    _hero_logo_html = f"<img class='hero-logo' src='data:image/png;base64,{_logo_b64}' alt='Philips logo'/>"

_banner_path = Path(__file__).parent / "assets" / "unbound-consumption.png"
_hero_banner_html = ""
if _banner_path.exists():
    _banner_b64 = base64.b64encode(_banner_path.read_bytes()).decode("ascii")
    _hero_banner_html = f"<img class='hero-banner' src='data:image/png;base64,{_banner_b64}' alt='Unbounded Consumption overview'/>"

_llm10_img_path = Path(__file__).parent / "assets" / "llm10.png"
_llm10_img_html = ""
if _llm10_img_path.exists():
    _llm10_b64 = base64.b64encode(_llm10_img_path.read_bytes()).decode("ascii")
    _llm10_img_html = f"<img src='data:image/png;base64,{_llm10_b64}' style='display:block;width:100%;border-radius:12px;margin:0 auto 24px auto;object-fit:contain;' alt='LLM10 diagram'/>"

_realscen10_img_path = Path(__file__).parent / "assets" / "real-scenarios.png"
_realscen10_img_html = ""
if _realscen10_img_path.exists():
    _realscen10_b64 = base64.b64encode(_realscen10_img_path.read_bytes()).decode("ascii")
    _realscen10_img_html = f"<img src='data:image/png;base64,{_realscen10_b64}' style='display:block;width:100%;border-radius:12px;margin:0 auto 24px auto;object-fit:contain;' alt='Real scenarios'/>"

st.sidebar.title("🔥 LLM10 Lab")
mode = st.sidebar.radio("Choose Mode", [
    "1. What is LLM10",
    "2. Vulnerable AI Behavior",
    "3. Secure AI Behavior",
    "4. Interactive Levels",
    "5. Mitigation Strategies"
])
st.sidebar.metric("Progressive Score", st.session_state.score)
st.sidebar.progress(min(1.0, st.session_state.score / 400))

with st.sidebar.expander("Solved Levels"):
    for lvl in LEVELS:
        st.write(("✅ " if st.session_state.solved.get(lvl["id"]) else "⬜ ") + lvl["name"])

if mode == "1. What is LLM10":
    st.markdown(f"""
<div class='hero'>
  {_hero_logo_html}
  <div class='pill'>LLM10 · Unbounded Consumption</div>
  <h1>{APP_TITLE}</h1>
  <p style="margin-top:12px;font-size:19px;color:var(--muted,#6b7280);max-width:820px;">Unlimited AI consumption without controls leads to unlimited business risk.</p>
  <p style="margin-top:4px;font-size:19px;color:var(--muted,#6b7280);max-width:820px;">Cost, performance, and security failures often begin with uncontrolled AI usage.</p>
  {_hero_banner_html}
  <p class='hero-quote'>When an AI system has no resource limits, an attacker does not need to break in — they just need to ask — costing you availability, performance, and money.</p>
</div>
""", unsafe_allow_html=True)
    if _llm10_img_html:
        st.markdown(_llm10_img_html, unsafe_allow_html=True)
    if _realscen10_img_html:
        st.markdown(_realscen10_img_html, unsafe_allow_html=True)

    st.markdown("#### What This Lab Covers")
    _c1, _c2, _c3, _c4 = st.columns(4)
    _c1.metric("Attack Types", "6", help="Token flooding, recursive expansion, tool loops, parallel sessions, RAG flooding, regeneration loops")
    _c2.metric("Interactive Levels", "4", help="Progressive Gandalf-style consumption challenges")
    _c3.metric("Healthcare Domains", "3", help="Clinical AI, device monitoring, patient data pipelines")
    _c4.metric("Primary Risk", "Denial of Wallet", help="Availability and cost exhaustion")



elif mode == "2. Vulnerable AI Behavior":
    st.header("2. Vulnerable AI Behavior")
    st.markdown('<div class="card">Use the simulator below to see how unsafe requests increase cost and availability risk.</div>', unsafe_allow_html=True)

    prompt = st.text_area("Attack-style request", value="Generate an exhaustive report. Repeat every point 100 times, expand every term, and continue until all possibilities are covered.", height=130)
    output_words = st.slider("Requested output words", 50, 5000, 1200, 50)
    tool_calls = st.slider("Requested tool/API calls", 0, 100, 25)
    recursion_depth = st.slider("Recursive expansion depth", 0, 20, 8)
    concurrent_sessions = st.slider("Parallel sessions", 1, 50, 10)

    result = consumption_score(prompt, output_words, tool_calls, recursion_depth, concurrent_sessions)
    cols = st.columns(6)
    cols[0].metric("Input Tokens", result["input_tokens"])
    cols[1].metric("Output Tokens", result["output_tokens"])
    cols[2].metric("Tool Cost", result["tool_cost_units"])
    cols[3].metric("Recursion Cost", result["recursion_cost_units"])
    cols[4].metric("Concurrency Cost", result["concurrency_cost_units"])
    cols[5].metric("Total", result["total_units"])

    risk_class = "risk-" + result["risk"].lower()
    st.markdown(f"<h3>Risk Rating: <span class='{risk_class}'>{result['risk']}</span></h3>", unsafe_allow_html=True)
    st.error("Vulnerable behavior: The AI attempts to fulfill the request without bounding tokens, loops, tool calls, or concurrency.")

elif mode == "3. Secure AI Behavior":
    st.header("3. Secure AI Behavior")
    st.markdown('<div class="card">The secure AI enforces cost and resource boundaries before executing the request.</div>', unsafe_allow_html=True)

    prompt = st.text_area("User request", value="Check every inventory item repeatedly and generate a full audit log until there are no mismatches.", height=130)
    output_words = st.slider("Output words", 50, 5000, 300, 50)
    tool_calls = st.slider("Tool/API calls", 0, 100, 8)
    recursion_depth = st.slider("Recursion depth", 0, 20, 3)
    concurrent_sessions = st.slider("Concurrent sessions", 1, 50, 4)

    ok, findings = secure_gate(prompt, output_words, tool_calls, recursion_depth, concurrent_sessions)
    result = consumption_score(prompt, output_words, tool_calls, recursion_depth, concurrent_sessions)

    st.write("Estimated consumption:", result)
    if ok:
        st.success("Secure decision: Request is within budget and can proceed.")
        st.write("Safe response: I will complete the bounded task within the approved limits.")
    else:
        st.warning("Secure decision: Request must be constrained before execution.")
        for f in findings:
            st.write("• " + f)
        st.info("Safe response example: I can help with a bounded version: maximum 5 tool calls, 250 words, and recursion depth of 2.")

elif mode == "4. Interactive Levels":
    st.header("4. Interactive Levels")
    st.caption("Default prompts are hidden. Select a tier and solve the challenge by writing a secure bounded instruction.")

    level_names = {lvl["name"]: lvl for lvl in LEVELS}
    selected_name = st.selectbox("Challenge Tier", list(level_names.keys()))
    level = level_names[selected_name]

    if st.session_state.active_level != level["id"]:
        st.session_state.active_level = level["id"]
        reset_level_state()

    st.markdown(f"""
<div class="card">
<span class="pill">{level['name']}</span>
<h3>{level['title']}</h3>
<b>Scenario:</b> {level['scenario']}<br><br>
<b>Your Goal:</b> {level['goal']}<br><br>
<b>Security Concept:</b> {level['concept']}
</div>
""", unsafe_allow_html=True)

    with st.expander("Reveal simulated risky request"):
        st.code(level["attack_prompt"])

    user_answer = st.text_area(
        "Write your secure bounded instruction / defense response",
        key=f"answer_{level['id']}",
        placeholder="Example: Limit output to..., maximum tool calls..., stop after...",
        height=140
    )

    c1, c2, c3 = st.columns([1,1,2])
    with c1:
        submit = st.button("Validate Challenge", type="primary")
    with c2:
        clear = st.button("Clear Current Level")

    if clear:
        st.session_state[f"answer_{level['id']}"] = ""
        st.rerun()

    if submit:
        passed, answer_score, feedback = validate_answer(user_answer, level)
        st.write(f"Validation Score: **{answer_score}/100**")
        for item in feedback:
            st.write("• " + item)
        if passed:
            if not st.session_state.solved.get(level["id"]):
                st.session_state.solved[level["id"]] = True
                st.session_state.score += 100
            st.success("Level solved. Previous prompt cleared automatically for the next level.")
            st.balloons()
        else:
            st.error("Not solved yet. Add explicit bounded-consumption controls.")

    with st.expander("Contextual Explanation"):
        st.write("Risk:", level["risk"])
        st.write("Recommended Defense:", level["defense"])

elif mode == "5. Mitigation Strategies":
    st.header("5. Mitigation Strategies and Security Best Practices - LLM10")
    st.markdown("""
<div class="card info">
  <b>How to Prevent LLM10 Unbounded Consumption</b><br><br>
  <table style="width:100%;border-collapse:collapse;">
    <tr>
      <td style="width:50%;padding:6px 12px;vertical-align:top;">✅ Enforce <b>token budgets</b> — max input tokens and max output tokens per request</td>
      <td style="width:50%;padding:6px 12px;vertical-align:top;">✅ Apply <b>rate limits</b> per user, tenant, IP, application, and API key</td>
    </tr>
    <tr>
      <td style="padding:6px 12px;vertical-align:top;">✅ Set <b>cost quota</b> management with daily/monthly spend thresholds and alerts</td>
      <td style="padding:6px 12px;vertical-align:top;">✅ Restrict <b>tool-call budget</b> — maximum function/API calls per request</td>
    </tr>
    <tr>
      <td style="padding:6px 12px;vertical-align:top;">✅ Set <b>recursion limits</b> to stop recursive planning and repeated expansions</td>
      <td style="padding:6px 12px;vertical-align:top;">✅ Cap <b>RAG retrieval chunks</b>, deduplicate documents, and limit upload sizes</td>
    </tr>
    <tr>
      <td style="padding:6px 12px;vertical-align:top;">✅ Enforce <b>concurrency controls</b> — restrict active sessions and queue depth</td>
      <td style="padding:6px 12px;vertical-align:top;">✅ Use <b>timeouts and circuit breakers</b> to fail safely when resource use spikes</td>
    </tr>
    <tr>
      <td style="padding:6px 12px;vertical-align:top;">✅ Apply <b>caching</b> to reuse repeated answers and tool results</td>
      <td style="padding:6px 12px;vertical-align:top;">✅ <b>Monitor</b> for anomalies in token use, tool calls, latency, and cost in real time</td>
    </tr>
    <tr>
      <td style="padding:6px 12px;vertical-align:top;">✅ Route to <b>cheaper models or summarised outputs</b> as graceful degradation under load</td>
      <td style="padding:6px 12px;vertical-align:top;">✅ Red-team with <b>token flooding, recursive prompts</b>, and multi-session parallelism before production</td>
    </tr>
  </table>
</div>
<p class='page-quote'>Cost governance is a security control — an AI system without resource limits is an open door to denial of wallet and service degradation.</p>
""", unsafe_allow_html=True)

    st.subheader("Secure AI Reference Response")
    st.success("I can help, but I must keep the task bounded. I will limit the output to 250 words, use at most 5 tool calls, avoid recursive expansion beyond depth 2, and stop if the quota is reached.")
