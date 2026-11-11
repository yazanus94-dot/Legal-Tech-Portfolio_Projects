"""Contract Clause Analyzer: rule-based clause detection and risk flagging for plain-text contracts.

Educational tool. Not legal advice.
"""
import re
import sys
from dataclasses import dataclass

# clause name -> (detection regex, whether it is expected in a commercial services contract)
CLAUSES = {
    "Termination": r"\bterminat(e|ion)\b",
    "Confidentiality": r"\bconfidential(ity)?\b",
    "Indemnification": r"\bindemnif(y|ication)\b",
    "Limitation of Liability": r"\blimitation of liability\b|\bliability (shall|will) not exceed\b",
    "Governing Law": r"\bgoverned by (the )?laws?\b|\bgoverning law\b",
    "Dispute Resolution": r"\barbitration\b|\bjurisdiction of the courts\b|\bmediation\b",
    "Intellectual Property": r"\bintellectual property\b",
    "Data Protection": r"\bpersonal data\b|\bdata protection\b",
    "Force Majeure": r"\bforce majeure\b",
}

RISK_PATTERNS = [
    (r"\bunlimited liability\b|\bwithout limit\b", "HIGH", "Uncapped liability exposure."),
    (r"\bsole discretion\b", "MEDIUM", "One-sided discretion; check for mutuality."),
    (r"\bautomatically renew", "MEDIUM", "Auto-renewal; confirm notice window for opting out."),
    (r"\bperpetual\b|\birrevocable\b", "MEDIUM", "Perpetual/irrevocable grant; confirm scope is intended."),
    (r"\bat any time without (cause|notice)\b", "HIGH", "Termination without cause or notice."),
    (r"\bindemnif(y|ies)\b.*\ball\b.*\b(losses|claims)\b", "MEDIUM", "Broad indemnity; check for carve-outs and caps."),
]


@dataclass
class Finding:
    severity: str
    message: str
    excerpt: str = ""


def split_sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.;])\s+|\n+", text) if s.strip()]


def analyze(text):
    found = {name for name, pat in CLAUSES.items() if re.search(pat, text, re.I)}
    findings = [Finding("INFO", f"Missing clause: {n}") for n in CLAUSES if n not in found]
    for sentence in split_sentences(text):
        for pat, sev, msg in RISK_PATTERNS:
            if re.search(pat, sentence, re.I):
                findings.append(Finding(sev, msg, sentence[:140]))
    return sorted(found), findings


def main(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    found, findings = analyze(text)
    print(f"Clauses detected ({len(found)}/{len(CLAUSES)}): {', '.join(found)}\n")
    order = {"HIGH": 0, "MEDIUM": 1, "INFO": 2}
    for fd in sorted(findings, key=lambda x: order[x.severity]):
        line = f"[{fd.severity}] {fd.message}"
        print(line + (f'\n        > "{fd.excerpt}"' if fd.excerpt else ""))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "samples/sample_services_agreement.txt")
