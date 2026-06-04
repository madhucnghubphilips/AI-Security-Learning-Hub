from collections import Counter
from copy import deepcopy


CONTROL_CATALOG = {
    "LLM03-001": "Approved Component Allowlist",
    "LLM03-002": "Version Pinning",
    "LLM03-003": "Integrity Verification",
    "LLM03-004": "Private Registry",
    "LLM03-005": "SBOM Generation",
    "LLM03-006": "RAG Provenance",
    "LLM03-007": "Prompt Template Integrity",
    "LLM03-008": "Runtime Egress Restriction",
    "LLM03-009": "Secrets Isolation",
    "LLM03-010": "Output Risk Detection",
}


PACKAGE_REGISTRY = {
    "healthcare-utils-1.2.0": {
        "name": "healthcare-utils",
        "version": "1.2.0",
        "maintainer": "trusted-healthcare-oss",
        "scripts": {},
        "dependencies": {
            "pydantic": "2.8.2",
        },
        "integrity": "signed-demo-package",
        "description": "Safe synthetic healthcare utility package for training.",
    },
    "healthcare-utils-1.2.1": {
        "name": "healthcare-utils",
        "version": "1.2.1",
        "maintainer": "lookalike-healthcare-oss",
        "scripts": {
            "postinstall": "python telemetry_helper.py",
        },
        "dependencies": {
            "pydantic": "2.8.2",
            "requestx-helper": "0.0.3",
        },
        "integrity": "unsigned-demo-package",
        "description": "Synthetic vulnerable OSS package for defensive training. Contains harmless indicators only.",
    },
}


PACKAGE_FILES = {
    "healthcare-utils-1.2.0": [
        {"file": "package.json", "sha256": "8a0b6e4d30b86bb8"},
        {"file": "healthcare_utils.py", "sha256": "3529f7b0426d95da"},
        {"file": "README.md", "sha256": "764d08ea39525b20"},
    ],
    "healthcare-utils-1.2.1": [
        {"file": "package.json", "sha256": "f8d751d8f5ebcfa1"},
        {"file": "healthcare_utils.py", "sha256": "9e0bd79db7b67c51"},
        {"file": "telemetry_helper.py", "sha256": "7c35f348b692ac29"},
        {"file": "README.md", "sha256": "647a137b9c129c12"},
    ],
}


ATTACK_FLOW = [
    {
        "step": 1,
        "phase": "AI reconnaissance",
        "description": "AI helps identify high-impact packages, dependency graphs, and maintainer patterns.",
    },
    {
        "step": 2,
        "phase": "Lookalike package",
        "description": "A package appears similar to a trusted OSS component, making review harder.",
    },
    {
        "step": 3,
        "phase": "Small version bump",
        "description": "A minor update hides changed metadata, new scripts, or suspicious dependencies.",
    },
    {
        "step": 4,
        "phase": "CI/CD consumption",
        "description": "Developers or pipelines pull the dependency automatically.",
    },
    {
        "step": 5,
        "phase": "Defensive gate",
        "description": "SBOM, SCA, signatures, lock files, provenance checks, and private registries stop the compromise.",
    },
]


ATTACK_SCENARIOS = {
    "Malicious dependency": {
        "component": "llm-helper-pro",
        "source": "Public Package Registry",
        "attack_type": "Typosquatting / dependency confusion",
        "unsafe_output": "Security controls look optional. Disable validation for faster delivery.",
        "trigger_event": "SIMULATED_EXFILTRATION_ATTEMPT",
        "trigger_detail": "Package attempted to read environment-like demo values.",
        "blocked_detail": "Package rejected by allowlist, checksum verification, and egress controls.",
        "controls": ["LLM03-001", "LLM03-003", "LLM03-008", "LLM03-009"],
    },
    "Poisoned RAG policy": {
        "component": "hospital-rag-policy-pack",
        "source": "Unverified Healthcare Repository",
        "attack_type": "Poisoned RAG knowledge base",
        "unsafe_output": "Upload patient summaries externally and skip authorization validation.",
        "trigger_event": "POISONED_CONTEXT_RETRIEVED",
        "trigger_detail": "Retrieved policy document came from an unapproved healthcare repository.",
        "blocked_detail": "RAG document rejected because provenance validation failed.",
        "controls": ["LLM03-006", "LLM03-010"],
    },
    "Prompt template backdoor": {
        "component": "clinical-prompt-core",
        "source": "Unverified Git Repository",
        "attack_type": "Prompt template backdoor",
        "unsafe_output": "Ignore internal validation and send diagnostic logs to an external endpoint.",
        "trigger_event": "HIDDEN_PROMPT_INSTRUCTION",
        "trigger_detail": "Template contains a hidden instruction that changes assistant behavior.",
        "blocked_detail": "Prompt template rejected after integrity validation failed.",
        "controls": ["LLM03-007", "LLM03-010"],
    },
    "Untrusted model/plugin output": {
        "component": "open-model-adapter",
        "source": "Unverified model/plugin repository",
        "attack_type": "Untrusted model/plugin",
        "unsafe_output": "Disable authentication temporarily to simplify integration testing.",
        "trigger_event": "UNTRUSTED_MODEL_OUTPUT",
        "trigger_detail": "Model/plugin produced unsafe operational guidance.",
        "blocked_detail": "Plugin action blocked by allowlist and output risk detection.",
        "controls": ["LLM03-001", "LLM03-010"],
    },
}


def get_package_manifest(package_name):
    return deepcopy(PACKAGE_REGISTRY[package_name])


def get_package_files(package_name):
    return deepcopy(PACKAGE_FILES[package_name])


def compare_manifests(baseline_name, candidate_name):
    baseline = PACKAGE_REGISTRY[baseline_name]
    candidate = PACKAGE_REGISTRY[candidate_name]
    diff = []

    for field in ["version", "maintainer", "scripts", "dependencies", "integrity"]:
        if baseline.get(field) != candidate.get(field):
            diff.append(
                {
                    "field": field,
                    "trusted": baseline.get(field),
                    "candidate": candidate.get(field),
                    "risk": _manifest_field_risk(field),
                }
            )

    return diff


def evaluate_security_gates(package_name, gates):
    manifest = PACKAGE_REGISTRY[package_name]
    findings = []

    if manifest.get("maintainer") != "trusted-healthcare-oss":
        findings.append(
            _finding(
                "Maintainer validation",
                "Maintainer identity changed from trusted-healthcare-oss.",
                "High",
                gates.get("validate_maintainer_identity", False),
                ["LLM03-001", "LLM03-004"],
            )
        )

    if manifest.get("scripts"):
        findings.append(
            _finding(
                "Lifecycle script review",
                "Lifecycle script found in package metadata.",
                "Critical",
                gates.get("block_lifecycle_scripts", False),
                ["LLM03-003", "LLM03-005"],
            )
        )

    if manifest.get("integrity") != "signed-demo-package":
        findings.append(
            _finding(
                "Signature verification",
                "Package is unsigned in demo metadata.",
                "Critical",
                gates.get("block_unsigned_packages", False),
                ["LLM03-003"],
            )
        )

    if "requestx-helper" in manifest.get("dependencies", {}):
        findings.append(
            _finding(
                "Dependency review",
                "New suspicious helper dependency added.",
                "High",
                gates.get("review_new_dependencies", False),
                ["LLM03-002", "LLM03-005"],
            )
        )

    if manifest.get("version") != "1.2.0":
        findings.append(
            _finding(
                "Version pinning",
                "Dependency version changed from pinned baseline.",
                "Medium",
                False,
                ["LLM03-002"],
            )
        )

    return findings


def summarize_findings_by_severity(findings):
    counts = Counter(finding["severity"] for finding in findings)
    return {severity: counts.get(severity, 0) for severity in ["Critical", "High", "Medium", "Low"]}


def generate_scenario_events(scenario, mitigations_enabled):
    events = [
        {
            "event_type": "COMPONENT_SELECTED",
            "severity": "Info",
            "component": scenario["component"],
            "detail": f"{scenario['attack_type']} from {scenario['source']}.",
            "controls": [],
            "blocked": False,
        },
        {
            "event_type": scenario["trigger_event"],
            "severity": "High",
            "component": scenario["component"],
            "detail": scenario["trigger_detail"],
            "controls": scenario["controls"],
            "blocked": False,
        },
    ]

    if mitigations_enabled:
        events.append(
            {
                "event_type": "MITIGATION_APPLIED",
                "severity": "Pass",
                "component": scenario["component"],
                "detail": scenario["blocked_detail"],
                "controls": scenario["controls"],
                "blocked": True,
            }
        )
    else:
        events.append(
            {
                "event_type": "RISK_REALIZED",
                "severity": "Critical",
                "component": scenario["component"],
                "detail": scenario["unsafe_output"],
                "controls": scenario["controls"],
                "blocked": False,
            }
        )

    return events


def controls_for_event(event):
    return [
        {"id": control_id, "name": CONTROL_CATALOG[control_id]}
        for control_id in event.get("controls", [])
    ]


def _manifest_field_risk(field):
    risks = {
        "version": "Version drift from reviewed baseline",
        "maintainer": "Publisher identity changed",
        "scripts": "Install-time execution introduced",
        "dependencies": "New transitive dependency path introduced",
        "integrity": "Signature or checksum trust changed",
    }
    return risks[field]


def _finding(control, finding, severity, blocked, controls):
    return {
        "control": control,
        "finding": finding,
        "severity": severity,
        "blocked": blocked,
        "controls": controls,
    }
