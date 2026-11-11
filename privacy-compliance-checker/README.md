# Privacy Compliance Checker

Screens JSON data-processing records (a simplified record of processing activities) against a GDPR-style checklist: lawful basis, consent withdrawal, special-category conditions, purpose, retention, processor agreements, cross-border transfers, breach procedure, and DPIA triggers.

**Topic area:** Privacy and data protection.

```bash
python checker.py samples/processing_records.json
pytest tests/
```

## Limits
- A checklist screen, not a compliance determination. Many obligations (transparency notices, data-subject rights, security measures) need human assessment.
- GDPR references are included for orientation; the UAE PDPL and other regimes differ in detail. Check current legal text for your jurisdiction.
- Sample records are fictional. Not legal advice.


## About
Built by Yazan Aljabari (B.Sc. Biomedical Engineering; IT/QA support; M.Sc. IT candidate, Arizona State University) as a legal-tech exercise. It demonstrates technical skills applied to a legal workflow, not legal qualification, and is not legal advice.
