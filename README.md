# Legal-Tech Portfolio Projects

[![Tests](https://github.com/yazanus94-dot/Legal-Tech-Portfolio_Projects/actions/workflows/ci.yml/badge.svg)](https://github.com/yazanus94-dot/Legal-Tech-Portfolio_Projects/actions/workflows/ci.yml)
![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Three command-line tools at the intersection of **law and software engineering**:
contract review screening, privacy-law compliance screening, and statutory
benefit calculation. Every tool is rule-based **by design** — transparent,
auditable logic a lawyer can inspect line by line — and every README states its
limits as clearly as its features.

| # | Project | Domain | What it does |
|---|---------|--------|--------------|
| 1 | [contract-clause-analyzer](contract-clause-analyzer/) | Commercial contracts | Detects 9 standard clauses in plain-text contracts, lists the missing ones, and flags risky language: uncapped liability, termination without notice, auto-renewal, broad indemnity, one-sided discretion |
| 2 | [privacy-compliance-checker](privacy-compliance-checker/) | Privacy / data protection | Screens JSON processing records against a GDPR-style checklist: lawful basis, consent withdrawal, special-category conditions, retention, processor agreements, cross-border transfers, breach procedure, DPIA triggers |
| 3 | [uae-end-of-service-calculator](uae-end-of-service-calculator/) | UAE employment law | Estimates end-of-service gratuity on unlimited-term contracts: 21 days' basic pay/year for the first 5 years, 30 days thereafter, capped at 2 years' basic pay — with the 21/30 pro-rata edge cases covered in tests |

## Engineering stance

- **Rule-based, not "AI-magic".** Regex/statutory rules are deliberately chosen over opaque models: for legal screening, explainability *is* the feature.
- **Statutory math is test-first.** The gratuity calculator's tests cover the statutory tiers, the two-year cap, and partial-year pro-rata — the places hand calculations usually go wrong.
- **Honest limits.** Each README documents what the tool does *not* do (no enforceability interpretation, no compliance determination, no free-zone regimes) — the single most important habit for legal software.

## Quick start

```bash
# 1. Contract screening
cd contract-clause-analyzer
python analyzer.py samples/sample_services_agreement.txt
python -m pytest tests/

# 2. Privacy screening
cd ../privacy-compliance-checker
python checker.py samples/processing_records.json
python -m pytest tests/

# 3. Gratuity estimation
cd ../uae-end-of-service-calculator
python eosb.py --basic 10000 --years 7.5
python -m pytest tests/
```

CI runs all three suites and CLI smoke runs on Python 3.11 / 3.12 / 3.13.

## Scope

Portfolio projects by Yazan Aljabari. Not legal advice; sample documents and
records are synthetic. Nothing here is affiliated with any law firm.

## License

MIT, see [LICENSE](LICENSE).
