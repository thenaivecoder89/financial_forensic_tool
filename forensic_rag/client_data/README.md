# Synthetic Client Data Pack — Financial Forensic / Commercial Diligence Testing

This pack is fully synthetic and uses fictional entities, people, transactions, banks, contracts and amounts.

**Synthetic target:** Apex Facilities Bahrain W.L.L.  
**Currency:** BHD  
**Period:** FY2024 plus Q1/Q2 2025

## Usage
- Index all files except `validation_ground_truth_findings.csv`.
- Use `validation_ground_truth_findings.csv` only as the answer key to test whether your RAG + analytics workflow detects the intended red flags.
- The folder structure mirrors your `client_data` folders: `ap_ar`, `bank`, `contracts`, `financials`, `legal_regulatory`, and `ownership`.

## Embedded testing themes
Duplicate payment, split approvals, related-party vendor indicator, unclear source of funds, unrecorded bank movement,
unaccrued legal claim, concentration risk, undisclosed side letter, sanctions/manual review escalation, liquidity/covenant stress.
