import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from analyzer import analyze

def test_detects_and_flags():
    found, findings = analyze("Either party may terminate at any time without notice. Fees in sole discretion.")
    assert "Termination" in found
    sev = {f.severity for f in findings}
    assert "HIGH" in sev and "MEDIUM" in sev

def test_missing_clause_reported():
    _, findings = analyze("Nothing relevant here.")
    assert any("Governing Law" in f.message for f in findings)
