"""UAE End-of-Service Gratuity Estimator (private sector, unlimited-term contracts).

Assumed rule (Federal Decree-Law No. 33 of 2021 and its Executive Regulations):
  - 21 days of basic salary per year for the first 5 years
  - 30 days of basic salary per year beyond 5 years
  - Pro-rated for partial years; minimum 1 year of service
  - Total capped at 2 years of basic salary
Gratuity is based on BASIC salary only. Verify against current law and the contract; this is an
educational estimate, not legal advice. Edge cases (resignation, limited-term contracts, unpaid
leave, free-zone rules such as DIFC/ADGM) are NOT modelled.
"""
import argparse

def gratuity(basic_monthly, years_of_service):
    if basic_monthly < 0 or years_of_service < 0:
        raise ValueError("Inputs must be non-negative.")
    if years_of_service < 1:
        return 0.0
    daily = basic_monthly * 12 / 365  # simple daily-rate convention; some employers use /30
    first = min(years_of_service, 5)
    extra = max(years_of_service - 5, 0)
    total = daily * (21 * first + 30 * extra)
    return round(min(total, basic_monthly * 24), 2)

if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--basic", type=float, required=True, help="Monthly basic salary (AED)")
    p.add_argument("--years", type=float, required=True, help="Years of service (decimals allowed)")
    a = p.parse_args()
    print(f"Estimated gratuity: AED {gratuity(a.basic, a.years):,.2f}")
