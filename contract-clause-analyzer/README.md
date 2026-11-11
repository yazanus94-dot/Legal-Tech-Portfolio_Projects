# Contract Clause Analyzer

Command-line tool that scans a plain-text commercial contract, detects nine standard clauses, lists missing ones, and flags risky language (uncapped liability, termination without notice, auto-renewal, broad indemnity, one-sided discretion).

**Topic area:** Commercial contracts.

```bash
python analyzer.py samples/sample_services_agreement.txt
pytest tests/
```

## Design notes and limits
- Rule-based (regex), deliberately transparent and auditable. It finds keywords, it does not interpret meaning or enforceability.
- Risk patterns are a starting checklist; real review depends on jurisdiction, deal context, and bargaining position.
- Sample contract is fictional. Educational use only; not legal advice.


## About
Built by Yazan Aljabari (B.Sc. Biomedical Engineering; IT/QA support; M.Sc. IT candidate, Arizona State University) as a legal-tech exercise. It demonstrates technical skills applied to a legal workflow, not legal qualification, and is not legal advice.
