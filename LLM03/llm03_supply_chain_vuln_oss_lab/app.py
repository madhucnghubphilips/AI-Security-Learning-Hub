
import json
import os
import shutil
import hashlib
from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px

APP_DIR = Path(__file__).parent
DOWNLOAD_DIR = APP_DIR / "downloads"
DOWNLOAD_DIR.mkdir(exist_ok=True)

def load_json(path):
    with open(APP_DIR / path, "r", encoding="utf-8") as f:
        return json.load(f)

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def package_hash(pkg_dir):
    hashes = []
    for p in sorted(Path(pkg_dir).rglob("*")):
        if p.is_file():
            hashes.append(str(p.relative_to(pkg_dir)) + ":" + sha256_file(p))
    return hashlib.sha256("\\n".join(hashes).encode()).hexdigest()

def copy_package(pkg_name):
    src = APP_DIR / "safe_registry" / pkg_name
    dst = DOWNLOAD_DIR / pkg_name
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    return dst

def read_manifest(pkg_dir):
    with open(pkg_dir / "package.json", "r", encoding="utf-8") as f:
        return json.load(f)

attack_flow = load_json("data/attack_flow.json")

st.set_page_config(page_title="LLM03 Supply Chain Vulnerabilities Lab", page_icon="🧬", layout="wide")

st.title("🧬 LLM03 Supply Chain Vulnerabilities — Vulnerable OSS Download Lab")
st.caption("Safe defensive training application using a local simulated OSS registry.")

st.warning("Safety scope: This lab uses harmless local files only. It does not download or execute real malicious packages.")

with st.sidebar:
    st.header("Training Controls")
    mode = st.radio("Select OSS package to download", ["Safe OSS package: healthcare-utils 1.2.0", "Vulnerable OSS package: healthcare-utils 1.2.1"])
    secure_controls = st.toggle("Enable secure controls", value=False)
    st.markdown("---")
    st.subheader("Security Gates")
    gate_signature = st.checkbox("Block unsigned packages", value=secure_controls)
    gate_scripts = st.checkbox("Block lifecycle scripts", value=secure_controls)
    gate_maintainer = st.checkbox("Validate maintainer identity", value=secure_controls)
    gate_deps = st.checkbox("Review new dependencies", value=secure_controls)

pkg_folder = "healthcare-utils-1.2.0" if "1.2.0" in mode else "healthcare-utils-1.2.1"

top1, top2, top3, top4 = st.columns(4)
top1.metric("OWASP Risk", "LLM03")
top2.metric("Lab Type", "OSS Supply Chain")
top3.metric("Mode", "Defensive")
top4.metric("Execution", "Harmless Simulation")

st.markdown("## 1. Live Simulated OSS Download")

if st.button("⬇️ Download selected OSS package from local training registry", type="primary"):
    dst = copy_package(pkg_folder)
    st.session_state["downloaded_pkg"] = str(dst)
    st.success("Downloaded simulated package: " + pkg_folder)

if "downloaded_pkg" in st.session_state:
    pkg_dir = Path(st.session_state["downloaded_pkg"])
    manifest = read_manifest(pkg_dir)
    pkg_hash_value = package_hash(pkg_dir)

    c1, c2 = st.columns([1, 1])
    with c1:
        st.subheader("Downloaded Package Manifest")
        st.json(manifest)
        st.code("Package folder: " + str(pkg_dir) + "\\nSHA256 package fingerprint: " + pkg_hash_value, language="text")

    with c2:
        st.subheader("Package Files")
        files = []
        for p in sorted(pkg_dir.rglob("*")):
            if p.is_file():
                files.append({"file": str(p.relative_to(pkg_dir)), "sha256": sha256_file(p)[:16] + "..."})
        st.dataframe(pd.DataFrame(files), use_container_width=True)

    st.markdown("## 2. Detection Results")

    findings = []
    if manifest.get("maintainer") != "trusted-healthcare-oss":
        findings.append({"control": "Maintainer validation", "finding": "Maintainer identity changed", "severity": "High", "blocked": gate_maintainer})
    if manifest.get("scripts"):
        findings.append({"control": "Lifecycle script review", "finding": "Lifecycle script found in package.json", "severity": "Critical", "blocked": gate_scripts})
    if manifest.get("integrity") != "signed-demo-package":
        findings.append({"control": "Signature verification", "finding": "Package is unsigned in demo metadata", "severity": "Critical", "blocked": gate_signature})
    if "requestx-helper" in manifest.get("dependencies", {}):
        findings.append({"control": "Dependency review", "finding": "New suspicious helper dependency added", "severity": "High", "blocked": gate_deps})
    if manifest.get("version") != "1.2.0":
        findings.append({"control": "Version pinning", "finding": "Dependency version changed from pinned baseline", "severity": "Medium", "blocked": False})

    if not findings:
        st.success("No suspicious supply-chain indicators found.")
    else:
        df = pd.DataFrame(findings)
        st.dataframe(df, use_container_width=True)
        blocked_count = sum(1 for f in findings if f["blocked"])
        if blocked_count:
            st.success(str(blocked_count) + " suspicious indicator(s) blocked by enabled security gates.")
        else:
            st.error("Suspicious indicators detected, but no security gate blocked them.")

    st.markdown("## 3. How the Supply Chain Attack Happens")

    flow_cols = st.columns(len(attack_flow))
    for col, item in zip(flow_cols, attack_flow):
        with col:
            st.markdown("### " + str(item["step"]))
            st.markdown("**" + item["phase"] + "**")
            st.write(item["description"])

    st.markdown("## 4. AI-Assisted Attacker View vs Defender View")

    a, b = st.columns(2)
    with a:
        st.error("AI-assisted attacker pattern")
        st.markdown("""
- Find high-impact OSS projects at scale
- Generate convincing README and PR text
- Create lookalike repo/package metadata
- Hide suspicious changes inside small version updates
- Target CI/CD and dependency automation
""")
    with b:
        st.success("Defender controls")
        st.markdown("""
- Pin versions and use lock files
- Validate maintainers and provenance
- Block lifecycle scripts unless approved
- Verify signatures and checksums
- Use SBOM, SCA, and private registries
- Monitor dependency changes in CI/CD
""")

    st.markdown("## 5. Risk Chart")
    if findings:
        chart_df = pd.DataFrame(findings).groupby("severity").size().reset_index(name="count")
    else:
        chart_df = pd.DataFrame([{"severity": "Low", "count": 1}])
    fig = px.bar(chart_df, x="severity", y="count", text="count", title="Detected Supply Chain Indicators by Severity")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("## 6. CTF Questions")
    q1 = st.text_input("Q1: Which manifest field introduced the most critical risk?")
    q2 = st.text_input("Q2: Which control blocks unauthorized lifecycle script execution?")
    q3 = st.text_input("Q3: Which package version is the vulnerable training example?")

    if st.button("Check CTF Answers"):
        score = 0
        if "scripts" in q1.lower() or "postinstall" in q1.lower():
            score += 1
        if "lifecycle" in q2.lower() or "script" in q2.lower():
            score += 1
        if "1.2.1" in q3:
            score += 1
        st.info("Score: " + str(score) + "/3")
        if score == 3:
            st.success("Excellent. You identified the LLM03 supply-chain compromise path.")
        else:
            st.warning("Review package.json, detection results, and security gates.")

st.markdown("---")
st.markdown("""
### Key Takeaway

LLM03 supply-chain attacks target trusted components around AI systems: dependencies, models, datasets, prompts, plugins, RAG content, and CI/CD pipelines.

**Trust nothing. Verify everything. Secure the AI supply chain.**
""")
