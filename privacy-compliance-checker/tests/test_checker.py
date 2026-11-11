import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from checker import check

def test_consent_without_withdrawal():
    msgs = [m for _, m in check({"lawful_basis": "consent", "purpose": "x", "retention_period": "1y", "breach_procedure": True})]
    assert any("withdrawal" in m for m in msgs)

def test_clean_record():
    rec = {"lawful_basis": "contract", "purpose": "x", "retention_period": "1y", "breach_procedure": True}
    assert check(rec) == []
