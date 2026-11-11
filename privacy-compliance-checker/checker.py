"""Privacy Compliance Checker: screens a data-processing record against a GDPR-style checklist.

Educational tool. Not legal advice. The UAE PDPL (Federal Decree-Law No. 45 of 2021) has similar
themes (lawful processing, transparency, security, breach notification, cross-border transfer rules);
verify exact requirements against the current text before relying on any output.
"""
import json
import sys

LAWFUL_BASES = {"consent", "contract", "legal_obligation", "vital_interests", "public_task", "legitimate_interests"}

def check(rec):
    issues = []
    def add(sev, msg): issues.append((sev, msg))

    if rec.get("lawful_basis") not in LAWFUL_BASES:
        add("HIGH", "No valid lawful basis recorded (GDPR Art. 6).")
    if rec.get("lawful_basis") == "consent" and not rec.get("consent_withdrawable"):
        add("HIGH", "Consent relied on but no withdrawal mechanism (GDPR Art. 7(3)).")
    if rec.get("special_category_data") and not rec.get("special_category_condition"):
        add("HIGH", "Special-category data without a recorded Art. 9 condition.")
    if not rec.get("purpose"):
        add("MEDIUM", "No specified purpose (purpose limitation, Art. 5(1)(b)).")
    if not rec.get("retention_period"):
        add("MEDIUM", "No retention period (storage limitation, Art. 5(1)(e)).")
    if rec.get("uses_processor") and not rec.get("processor_agreement"):
        add("HIGH", "Processor used without a written agreement (Art. 28).")
    if rec.get("cross_border_transfer") and not rec.get("transfer_mechanism"):
        add("HIGH", "Cross-border transfer without a recorded mechanism (Chapter V).")
    if not rec.get("breach_procedure"):
        add("MEDIUM", "No breach procedure; GDPR requires supervisory notice within 72 hours where applicable (Art. 33).")
    if rec.get("high_risk_processing") and not rec.get("dpia_done"):
        add("HIGH", "High-risk processing without a DPIA (Art. 35).")
    return issues

def main(path):
    with open(path, encoding="utf-8") as f:
        records = json.load(f)
    for rec in records:
        issues = check(rec)
        print(f"\n== {rec.get('name', 'unnamed')} ==")
        print("PASS: no issues found by this checklist." if not issues else "\n".join(f"[{s}] {m}" for s, m in issues))

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "samples/processing_records.json")
