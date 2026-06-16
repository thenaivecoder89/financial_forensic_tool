# report_structure_pack.md

## Pack purpose

This pack defines the output structure, drafting rules, rating logic, evidence standards, and client-facing report templates for a forensic diligence / red-flag assessment engagement. It is designed to be used with a RAG-enabled LLM so that the model generates structured, evidence-backed consulting-style outputs rather than generic narrative responses.

This pack should be used together with:

1. `forensic_methodology_pack.md`
2. `internal_controls_pack.md`
3. `bahrain_contextualization_pack.md`
4. `aml_sanctions_pack.md`
5. Client evidence corpus, once available

Until client evidence is available, outputs generated using this pack must be framed as methodology, readiness, workplan, risk taxonomy, request list, or report shell outputs. They must not be framed as factual findings on the Target.

---

## 1. Core output principles

### 1.1 Evidence-first rule

The model must not create factual findings without evidence. Every factual observation must be linked to one or more source references.

A valid finding requires:

- Finding ID
- Workstream
- Risk rating
- Observation
- Evidence summary
- Source reference
- Impact / exposure, where quantifiable
- Risk implication
- Recommended next step
- Confidence level
- Limitation / open item

If evidence is unavailable, the output should state:

> No factual finding can be made at this stage. The item should be treated as an area for review once supporting documentation is received.

### 1.2 No definitive fraud conclusion rule

The model must not state that fraud, misconduct, breach, illegality, or regulatory violation has occurred unless the engagement team has verified the matter and approved such wording.

Preferred wording:

- “Potential indicator of irregularity”
- “Matter requiring further review”
- “Inconsistency noted”
- “Unresolved red flag”
- “Potential control weakness”
- “Potential undisclosed exposure”
- “Requires corroboration”

Avoid unsupported wording:

- “Fraud occurred”
- “The Target committed misconduct”
- “The transaction is illegal”
- “Management intentionally misrepresented”
- “Confirmed money laundering”

### 1.3 Distinguish evidence from representation

The model must classify information into one of the following source types:

| Source type | Description | Evidential weight |
|---|---|---|
| Audited / externally verified evidence | Audited financial statements, bank confirmations, official registry extracts, court filings | High |
| Primary internal evidence | GL, bank statements, contracts, invoices, board minutes, asset registers | Medium to high |
| Management representation | Interview notes, Q&A responses, management explanations | Medium, requires corroboration |
| Communication evidence | Emails, messages, correspondence | Medium, context-dependent |
| Public source | Registry, regulator, sanctions list, adverse media | Medium to high depending on source |
| Unverified assertion | Informal claim, unsupported statement, incomplete screenshot | Low |

### 1.4 Limitation-first drafting

Where documentation is missing, incomplete, unclear, corrupted, scanned poorly, or not independently verified, the report must clearly state the limitation.

Example limitation language:

> This observation is based on the documents made available as of [date/time]. Further review may be required upon receipt of outstanding documents, including [list].

### 1.5 Separate factual finding from advisory commentary

Each finding should separate:

1. **Factual observation** — what the evidence says.
2. **Risk implication** — why it matters.
3. **Advisory commentary** — interpretation / professional view.
4. **Recommended next step** — what the client should do.

---

## 2. Standard workstreams

Use the following workstream taxonomy unless the engagement partner modifies it.

| Workstream code | Workstream | Examples |
|---|---|---|
| FIN | Financial review | Financial statements, management accounts, GL, TB, AP/AR, bank, debt |
| CASH | Cash and banking | Bank statements, reconciliations, transfers, unexplained payments |
| AP | Procurement and payables | Vendor master, invoices, POs, payments, duplicate vendors |
| AR | Revenue and receivables | Customer master, revenue contracts, invoices, credit notes, aged AR |
| FA | Fixed assets | Asset register, ownership, valuation, impairment, disposals |
| LEG | Legal and disputes | Claims, litigation, regulatory letters, contingent liabilities |
| REG | Regulatory and licensing | Licenses, permits, compliance, sector approvals |
| OWN | Ownership and control | Shareholding, UBO, directors, related parties, group structure |
| GOV | Governance and controls | Board approvals, DoA, segregation of duties, management override |
| COMM | Communications and representations | Emails, interviews, Q&A, inconsistent statements |
| COM | Commercial diligence | Customers, suppliers, contracts, market dependency, termination rights |
| AML | AML / sanctions / financial crime | CDD, source of funds, sanctions, PEPs, unusual transactions |
| GAP | Data gaps and limitations | Missing, incomplete, unreadable, inconsistent evidence |

---

## 3. Red / Amber / Green rating rubric

### 3.1 Rating definitions

| Rating | Definition | Required treatment |
|---|---|---|
| Red | Material issue, transaction-critical risk, possible legal/regulatory exposure, ownership/control concern, suspected misstatement, material unexplained financial exposure, or issue requiring immediate escalation | Escalate, prioritize review, define immediate action |
| Amber | Potential issue requiring further investigation, incomplete support, unresolved inconsistency, medium control weakness, or matter that may become material depending on further evidence | Track, request documents, interview relevant parties |
| Green | No material issue identified based on documents reviewed | State limitation clearly; Green does not mean no risk exists |
| Grey / Pending | Evidence not yet received or insufficient to assess | Include in data gap register, not as a clean finding |

### 3.2 Red rating triggers

Assign Red where one or more of the following are supported by evidence:

- Undisclosed shareholder, UBO, nominee, or control arrangement
- Sanctions hit or high-confidence match to restricted party
- Known legal claim, regulatory matter, or dispute not disclosed
- Material unexplained cash movement or bank-book mismatch
- Duplicate or potentially improper payment with financial impact
- Material related-party transaction not disclosed or not approved
- Material asset ownership issue, pledge, encumbrance, or missing title
- Evidence of management representation contradicted by documents
- Major control override or segregation-of-duties failure affecting financial records
- Contractual restriction that could affect transaction execution
- Material undisclosed debt, guarantee, liability, or covenant issue
- Evidence suggesting falsified, altered, backdated, or unsupported documents

### 3.3 Amber rating triggers

Assign Amber where one or more of the following are present:

- Incomplete documentation for a material item
- Management explanation not yet corroborated
- Inconsistency exists but materiality is not yet determined
- Unusual transaction pattern requiring follow-up
- Concentration risk in customer, supplier, lender, or related party
- Missing approval or incomplete audit trail
- Low or medium confidence sanctions / adverse media name similarity
- Contract clause requiring legal review but not yet transaction-blocking
- Control weakness that may not be material on its own but indicates governance risk

### 3.4 Green rating conditions

Assign Green only where:

- Relevant documents were reviewed;
- No exception was identified from the documents reviewed;
- No contradictory evidence was identified; and
- Limitations are clearly stated.

Template wording:

> Based on the documents reviewed to date, no material red flag has been identified in this area. This assessment remains subject to receipt and review of outstanding documents and management responses.

### 3.5 Grey / Pending conditions

Use Grey / Pending where:

- Documents are not received;
- Documents are unreadable or incomplete;
- Data fields are insufficient;
- Client approval is required before review;
- Legal privilege, privacy, or access constraints apply.

Template wording:

> Assessment pending. The relevant documents / data required to conclude on this matter have not yet been made available.

---

## 4. Confidence rating rubric

Each finding must include a confidence level separate from RAG rating.

| Confidence | Definition |
|---|---|
| High | Supported by multiple reliable sources or a primary source with clear evidence and traceability |
| Medium | Supported by one reliable source or partial corroboration; requires additional validation |
| Low | Based on incomplete, unclear, unverified, or circumstantial evidence |

RAG rating and confidence are different. A matter can be Red with Medium confidence if the potential impact is high but evidence is still incomplete.

---

## 5. Finding register schema

Every issue should be captured in the following register format before it is included in the client-facing report.

| Field | Required? | Description |
|---|---:|---|
| Finding ID | Yes | Unique identifier, e.g., F-001 |
| Workstream | Yes | FIN, CASH, AP, AR, FA, LEG, REG, OWN, GOV, COMM, COM, AML, GAP |
| RAG rating | Yes | Red / Amber / Green / Grey-Pending |
| Confidence | Yes | High / Medium / Low |
| Finding title | Yes | Short, factual heading |
| Observation | Yes | What was observed from evidence |
| Evidence summary | Yes | Concise evidence relied upon |
| Source reference | Yes | File name, page, sheet, row, date, or record ID |
| Amount / exposure | Where applicable | Financial value or qualitative exposure |
| Period | Where applicable | Date or period covered |
| Parties involved | Where applicable | Entity, person, counterparty, regulator, bank, customer, vendor |
| Risk implication | Yes | Why the matter matters to the transaction/client |
| Recommended next step | Yes | Follow-up action |
| Owner | Optional | Engagement team member / client owner |
| Status | Yes | Open / Pending info / Escalated / Resolved / Closed |
| Limitation | Yes | Data gap, assumption, uncertainty, or dependency |

---

## 6. Evidence register schema

Each source item should be captured in an evidence register to support traceability.

| Field | Required? | Description |
|---|---:|---|
| Evidence ID | Yes | Unique identifier, e.g., E-001 |
| Related Finding ID | Yes / if applicable | Link to finding |
| Source document | Yes | File name or source name |
| Source type | Yes | Audited evidence, internal evidence, management representation, communication, public source, unverified assertion |
| Page / sheet / row | Yes where available | Trace reference |
| Date of document | Where available | Document date |
| Period covered | Where available | Period covered by source |
| Extract / summary | Yes | Short summary of relevant evidence |
| Reliability | Yes | High / Medium / Low |
| Confidentiality / privilege flag | Yes | Confidential / privileged / personal data / public |
| Reviewer note | Optional | Analyst comments |

---

## 7. Source citation style

Use the following citation styles in reports and registers.

### 7.1 PDF source

`[Document name], p. [page number]`

Example:

`Bank Statement - ABC Bank - Jan 2025.pdf, p. 4`

### 7.2 Excel source

`[Workbook name], [sheet name], row [row number]`

Example:

`General Ledger FY2025.xlsx, GL_Detail, row 1842`

### 7.3 Email / communication source

`[Communication source], from [sender] to [recipient], dated [date], subject [subject]`

Example:

`Email export, CFO to CEO, dated 12 March 2025, subject “Settlement with Vendor X”`

### 7.4 Interview source

`Interview with [role / person], dated [date], question [question number]`

Example:

`Leadership interview with CFO, dated 18 June 2026, Q12`

### 7.5 Public source

`[Source / authority], [record / page title], accessed [date]`

Example:

`Sijilat public CR search, Target CR extract, accessed 18 June 2026`

---

## 8. Red Flag Report template

### 8.1 Report title

`Red Flag Report – Initial Issue`

### 8.2 Suggested section structure

1. Executive summary
2. Scope and status of review
3. Documents and information reviewed
4. Summary RAG dashboard
5. Key red / amber matters
6. Findings by workstream
7. Legal matters requiring immediate escalation
8. Communications inconsistent with disclosed record
9. Data gaps and limitations
10. Recommended next steps
11. Appendices

### 8.3 Executive summary structure

The executive summary should include:

- Engagement context
- Review status as of reporting date
- Overall risk profile
- Number of Red, Amber, Green, and Pending items
- Immediate escalation matters
- Top 3–5 priority issues
- Critical data gaps
- Recommended next steps

Template:

> As of [date], the review has focused on [documents / workstreams reviewed]. Based on the information made available to date, [number] Red matters, [number] Amber matters, [number] Green areas, and [number] Pending areas have been identified. The most significant matters relate to [summarize]. These observations remain subject to receipt and review of outstanding documents, management responses, and further validation procedures.

### 8.4 RAG dashboard format

| Workstream | RAG rating | Key issue | Status | Next step |
|---|---|---|---|---|
| Financial review | Pending | Client financial data not yet received | Open | Request FS, GL, TB, bank statements |
| Ownership and control | Pending | CR / UBO documents not yet received | Open | Obtain CR extract and UBO register |
| Legal and regulatory | Pending | Claims / regulatory correspondence not yet received | Open | Request legal claims register |

### 8.5 Finding write-up format

#### F-[ID]: [Finding title]

| Field | Content |
|---|---|
| Workstream | [Workstream] |
| RAG rating | [Red / Amber / Green / Pending] |
| Confidence | [High / Medium / Low] |
| Observation | [Factual observation] |
| Evidence | [Source references] |
| Potential impact | [Financial / legal / operational / transaction impact] |
| Advisory commentary | [Interpretation] |
| Recommended next step | [Action] |
| Limitation | [Data limitations] |

### 8.6 Report wording rules

Use:

- Clear factual wording
- Short paragraphs
- Tables for registers
- Neutral tone
- Evidence references
- Explicit limitations
- Prioritized action language

Avoid:

- Unsupported conclusions
- Legal opinions unless approved by counsel
- Overly definitive fraud language
- Long theoretical explanations
- Generic textbook descriptions

---

## 9. Legal matters escalation template

### 9.1 When to escalate immediately

Escalate to General Counsel / client legal contact immediately where there is evidence or credible indication of:

- Existing litigation or threatened claim not disclosed
- Regulatory investigation, notice, penalty, or enforcement action
- Sanctions hit or high-confidence restricted-party exposure
- Potential breach of law, licence, permit, or regulatory obligation
- Contractual restriction affecting transaction execution
- Undisclosed guarantee, indemnity, security, or contingent liability
- Data privacy, privilege, or device-forensics issue requiring legal direction
- Evidence suggesting document alteration, destruction, or concealment

### 9.2 Legal escalation note format

**Subject:** Immediate Legal Escalation – [Matter title]

**Date:** [Date]

**Matter ID:** LEG-[ID]

**Summary:**
[Brief factual summary]

**Evidence identified:**
[Source documents and references]

**Potential implication:**
[Legal / regulatory / transaction implication]

**Urgency:**
[Immediate / High / Medium]

**Recommended action:**
[Action required from GC / counsel]

**Limitations:**
[Known gaps or uncertainties]

**Prepared by:**
[Name / role]

---

## 10. Initial Business Review template

### 10.1 Purpose

The Initial Business Review provides a preliminary commercial and operating view of the Target based on information reviewed to date. It should not duplicate the Red Flag Report; it should translate diligence observations into transaction and business implications.

### 10.2 Structure

1. Business overview
2. Ownership and operating structure
3. Principal activities and revenue model
4. Key customers and commercial relationships
5. Key suppliers and dependencies
6. Financial profile and trading performance
7. Assets and operating footprint
8. Regulatory and licensing context
9. Material disputes / claims / contingencies
10. Preliminary transaction implications
11. Open information requests
12. Areas for Phase 1B / Phase 2 review

### 10.3 Drafting rule

When client evidence is not yet available, use this wording:

> This section is pending receipt and review of Target documentation. The current report identifies the proposed review lens and the information required to complete the assessment.

---

## 11. Weekly update template

### 11.1 Purpose

Weekly updates should show movement in issues, risk ratings, escalations, and information gaps.

### 11.2 Structure

1. Review period
2. Work completed this week
3. Newly identified Red / Amber matters
4. Changes to prior RAG ratings
5. Legal escalations made
6. Outstanding document requests
7. Interviews completed / planned
8. Priority actions for next week

### 11.3 Movement table

| Finding ID | Previous rating | Current rating | Reason for movement | Action |
|---|---|---|---|---|
| F-001 | Amber | Red | New evidence received indicating material exposure | Escalate to GC |

---

## 12. Phase 1B scope confirmation memo template

### 12.1 Purpose

The Phase 1B memo should define the deeper workstreams required after initial red-flag review.

### 12.2 Structure

1. Background
2. Summary of Phase 1A matters
3. Matters requiring deeper investigation
4. Proposed Phase 1B procedures
5. Required documents and data
6. Required interviews
7. Legal / forensic specialist requirements
8. Timeline and resourcing
9. Client approvals required
10. Limitations and dependencies

### 12.3 Procedure mapping table

| Phase 1A matter | Proposed Phase 1B procedure | Evidence required | Interview required | Priority |
|---|---|---|---|---|
| [Issue] | [Procedure] | [Documents] | [Persons] | High / Medium / Low |

---

## 13. Communications inconsistency log

### 13.1 Purpose

This log captures inconsistencies between communications, management representations, disclosed records, contracts, financial records, and public sources.

### 13.2 Schema

| Field | Description |
|---|---|
| Inconsistency ID | COMM-001 |
| Source A | First source / statement |
| Source B | Contradictory or inconsistent source / statement |
| Nature of inconsistency | Contradiction / omission / timing issue / undisclosed party / unsupported assertion |
| Workstream | Legal / financial / ownership / commercial / regulatory |
| Materiality | High / Medium / Low / Unknown |
| RAG rating | Red / Amber / Green / Pending |
| Evidence references | File/page/sheet/row/email/interview references |
| Follow-up question | Question to be raised |
| Status | Open / resolved / escalated |

### 13.3 Classification logic

| Type | Description |
|---|---|
| Direct contradiction | Two sources make incompatible statements |
| Omission | Communication mentions a matter absent from disclosed records |
| Timing inconsistency | Dates or sequence of events do not align |
| Party inconsistency | Different parties, beneficiaries, signatories, or counterparties appear |
| Amount inconsistency | Financial amounts do not reconcile |
| Document support inconsistency | A statement is made but support is missing |
| Legal/regulatory inconsistency | Communication refers to claim, notice, dispute, licence issue, or regulator interaction not disclosed elsewhere |

---

## 14. Interview planning template

### 14.1 Leadership interview objectives

Leadership interviews should cover:

- Ownership and control
- Principal activities
- Business model
- Key commercial relationships
- Known disputes and claims
- Regulatory matters
- Financial performance and liquidity
- Related-party relationships
- Historic changes in organizational structure
- Areas where further interviews are required

### 14.2 Interview output schema

| Field | Description |
|---|---|
| Interview ID | INT-001 |
| Interviewee | Name / role |
| Date | Date |
| Topics covered | List |
| Key representations | Summary |
| Evidence requested | Follow-up documents |
| Contradictions identified | Link to COMM log |
| Second-tier interviewees suggested | Names / roles |
| Confidence | High / Medium / Low |
| Open questions | List |

### 14.3 Second-tier interview approval memo

**Purpose:** Obtain client approval before conducting second-tier interviews.

| Proposed interviewee | Role | Reason for interview | Linked finding / gap | Priority |
|---|---|---|---|---|
| [Name] | [Role] | [Reason] | [Finding ID / gap ID] | High / Medium / Low |

---

## 15. Document request and gap register

### 15.1 Document request tracker

| Request ID | Document / data requested | Workstream | Requested from | Date requested | Due date | Status | Reason needed |
|---|---|---|---|---|---|---|---|

### 15.2 Data gap register

| Gap ID | Missing item | Workstream | Impact on review | RAG effect | Follow-up action | Status |
|---|---|---|---|---|---|---|

### 15.3 Gap severity

| Severity | Definition |
|---|---|
| High | Prevents conclusion on material risk area |
| Medium | Limits confidence but does not prevent preliminary review |
| Low | Administrative or supporting item |

---

## 16. Report limitations language

Use the following standard limitations language, adjusted for each report.

### 16.1 Pre-client-data limitation

> This report has been prepared prior to receipt and review of Target-specific documentation. It sets out the proposed review framework, risk taxonomy, evidence requirements, and reporting structure. It does not constitute a factual findings report on the Target.

### 16.2 Document availability limitation

> The observations in this report are based solely on documents and information made available as of [date/time]. Additional documents or explanations may affect the observations, ratings, and recommended next steps.

### 16.3 No audit opinion limitation

> The procedures performed do not constitute an audit, review, or assurance engagement. No audit opinion or assurance conclusion is expressed.

### 16.4 No legal opinion limitation

> Legal and regulatory matters identified in this report are presented as potential issues for further review by counsel. This report does not constitute legal advice or a legal opinion.

### 16.5 No fraud determination limitation

> The identification of red flags or indicators does not constitute a determination that fraud or misconduct has occurred. Any such determination would require further investigation and appropriate legal review.

### 16.6 Public-source limitation

> Public-record and sanctions/adverse-media checks are based on sources accessed as of [date]. Results may be incomplete due to source availability, name variations, transliteration, data latency, or access restrictions.

---

## 17. QA checklist before client delivery

Before any output is shared with the client, check:

1. Are all findings supported by source references?
2. Are management statements distinguished from evidence?
3. Are all Red items clearly escalated or marked for escalation?
4. Are legal matters flagged for counsel review?
5. Are limitations clearly stated?
6. Are unsupported fraud/legal conclusions avoided?
7. Are amounts, dates, names, and source references checked?
8. Are duplicate findings consolidated?
9. Are RAG ratings consistent with the rating rubric?
10. Are data gaps separated from findings?
11. Are confidentiality and privilege issues considered?
12. Does the executive summary match the detailed findings?
13. Are recommended next steps practical and prioritized?
14. Are open items clearly assigned?
15. Is the report framed correctly as initial, interim, or final?

---

## 18. Model prompt guardrails

Use these instructions in system or developer prompts when generating outputs from this pack.

### 18.1 General output instruction

You are assisting with a forensic diligence / red-flag assessment. Generate structured, evidence-based, client-ready consulting outputs. Do not invent facts. Do not make definitive fraud, legal, or regulatory conclusions unless explicitly supported by evidence and approved wording. Use Red / Amber / Green ratings only according to the rubric. Distinguish evidence from management representation. Include limitations wherever evidence is incomplete.

### 18.2 Finding generation instruction

For each proposed finding, provide: Finding ID, workstream, RAG rating, confidence, observation, evidence, source reference, potential impact, advisory commentary, recommended next step, and limitation. If source evidence is insufficient, classify the matter as a data gap or area for review, not as a finding.

### 18.3 Report drafting instruction

Draft in a concise consulting style. Use tables where helpful. Avoid generic textbook explanation. Focus on what was reviewed, what was observed, why it matters, and what should be done next. Include a clear executive summary, RAG dashboard, prioritized issues, limitations, and next steps.

---

## 19. Initial deliverable when client data is not yet available

If Target-specific evidence has not yet been received, generate an “Initial Forensic Diligence Framework and Readiness Pack” instead of a Red Flag Findings Report.

### 19.1 Suggested title

`Initial Forensic Diligence Framework and Bahrain Contextual Risk Assessment`

### 19.2 Suggested sections

1. Purpose and context
2. Scope interpretation from SOW
3. Proposed risk taxonomy
4. Bahrain contextual review lens
5. Proposed document request list
6. Proposed interview plan
7. Proposed forensic analytics procedures
8. Proposed RAG rating rubric
9. Draft Red Flag Report structure
10. Immediate setup actions
11. Limitations

### 19.3 Required limitation

> This document is a pre-evidence framework and readiness deliverable. It does not present factual findings on the Target because Target-specific documentation has not yet been received or reviewed.

---

## 20. End-state outputs from the full RAG system

The full system should be able to produce:

1. Document inventory
2. Data gap register
3. Evidence register
4. Findings register
5. Communications inconsistency log
6. Legal escalation tracker
7. Interview question list
8. Expanded interview list approval memo
9. Red Flag Report
10. Weekly update
11. Initial Business Review
12. Phase 1B scope confirmation memo
13. Appendix of source references

