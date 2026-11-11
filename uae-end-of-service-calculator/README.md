# UAE End-of-Service Gratuity Estimator

Estimates end-of-service gratuity for private-sector employees on unlimited-term contracts under UAE labour law (21 days' basic pay per year for the first five years, 30 days thereafter, capped at two years' basic pay).

**Topic area:** Employment law.

```bash
python eosb.py --basic 10000 --years 7.5
pytest tests/
```

## Limits
- Does not model resignation scenarios, limited-term contracts, unpaid leave, or free-zone regimes (DIFC, ADGM).
- Daily-rate convention (annual basic / 365) varies in practice; check the contract and current Ministry of Human Resources and Emiratisation guidance.
- Educational estimate, not legal advice.


## About
Built by Yazan Aljabari (B.Sc. Biomedical Engineering; IT/QA support; M.Sc. IT candidate, Arizona State University) as a legal-tech exercise. It demonstrates technical skills applied to a legal workflow, not legal qualification, and is not legal advice.
