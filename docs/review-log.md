# Content Review and Learner-Testing Log (Stage 2)

The Stage 2 brief requires that **each core section is checked by someone other than its original author**, and that **a teammate who did not write an explanation or activity follows it as a learner**. This file records both. Keep every record directly below its heading so that the evidence sits next to the entry it supports.

---

## 1. Review assignments

"Author of record" is the member who revises the V2.0 draft and commits it under their own account. The reviewer must be a **different** member.

| File | Author of record (proposed) | Peer reviewer (proposed) | Learner tester (did not write it) | Due |
|---|---|---|---|---|
| `01-software-and-logic.md` | Sarvarbek | Aliya | Madi | 5 Nov |
| `02-rules-and-inference.md` | Aliya | Arsalan | Mukhammadshakhruz | 5 Nov |
| `03-symbolic-ai-vs-machine-learning.md` | Hayat | Sarvarbek | Anel | 5 Nov |
| `04-history-and-ai-winters.md` | Anel | Hayat | Arsalan | 5 Nov |
| `05-symbolic-ai-in-modern-software.md` | Madi | Mukhammadshakhruz | Aliya | 5 Nov |
| `06-test-bank.md` + `glossary.md` | Arsalan | Aliya | Hayat | 6 Nov |

*Confirm or swap names at the next meeting. Each person reviews one file and tests one file, and nobody reviews or tests their own file.*

---

## 2. Reviewer checklist

For each file, the reviewer checks and ticks:

1. **Accuracy:** definitions, claims, examples and answers are correct.
2. **Calculations and code:** every trace, count and code output is correct (run `examples/*.py` where relevant).
3. **Usability:** each activity can be completed using only the information in the file.
4. **Terminology:** terms match `content/glossary.md`.
5. **Sources:** each reference exists and supports the sentence it is attached to.
6. **Assets:** images and local links work in the **downloaded ZIP / rendered PDF**, not only on GitHub.

---

## 3. Points flagged for reviewers

| File | What to check |
|---|---|
| 02 | Run `examples/topic02_mini_rule_engine.py` with the starting facts of Parts A, E and F; confirm the answer tables. |
| 02 | XCON rule count ("about 2,500 by one account") is Wikipedia-only. Find a second source or keep the hedged wording. |
| 03 | Run `examples/topic03_learn_a_rule.py`; confirm the mistakes table in §3.3, then add email N and confirm Activity A. |
| 04 | DARPA (1974), LISP machines (1987) and Strategic Computing (1988) are Wikipedia-only. Try the history chapter of Russell & Norvig, *Artificial Intelligence: A Modern Approach* (library). |
| 05 | Check that the Liverpool lecture's guard example matches rules G1–G4. Confirm the Salesforce page still describes decision tables and eligibility. |
| 06 | Every answer must match the topic files. Re-run the trace questions (Q7–Q10, Q13). |

---

## 4. AI-assisted pre-check (3 November 2026), *not a peer review*

Before peer review, the V2.0 drafts were checked with AI assistance (see `docs/ai-use-log.md`, entry A-03). It is recorded here so reviewers know what has already been checked and what has not. **It does not replace the peer reviews in Section 5.**

| # | Location | What was checked | What was found | Action taken |
|---|---|---|---|---|
| 1 | Topic 3 §7, Activity A | Ran the demo with email N added | Draft answer said k = 3 and 4 tie; the program showed **k = 2 also ties** | Answer table and explanation corrected |
| 2 | Topic 4 §2 | Fifth Generation dates and cost against IPSJ museum page and *Nature* (1992) | V1.1 said **1981–1991, $850M** (one secondary source). Primary sources say **1982–1992**; cost ¥54 billion (IPSJ) / "over $400 million" (*Nature*) | Dates corrected; disagreement turned into Activity D |
| 3 | Topic 4 §2 | Lighthill report quote and year | Confirmed: 1973, Science Research Council; quote matches the hosted copy | Quote added with source |
| 4 | Topic 2 §8 | XCON deployment date and savings | Jan 1980 confirmed (McDermott 1981); $25M/year by 1986 confirmed (Middlesex notes); rule count not confirmed | Sources added; rule count hedged |
| 5 | Topic 2 §6 Parts E–F; Test bank Q7–Q10, Q13 | Ran both demo programs with each activity's starting facts | All answers match program output | None needed |
| 6 | All topics | Terminology | "rules engine" used once for an expert system; "Symbolic AI" capitalised inconsistently | Fixed; rules added to glossary |
| 7 | All files | Local links and images | All resolve (checked by script before rendering the PDF) | None needed |

**Not checked by the AI pre-check (reviewers must do these):** whether explanations are clear to a real beginner; whether activity instructions are unambiguous in practice; the single-source claims listed in Section 3.

---

## 5. Peer review records

*One record per file. Fill in during review; commit under the reviewer's own account.*

### Review R-01: `02-rules-and-inference.md`

| Field | Entry |
|---|---|
| Reviewer (name, GitHub) | |
| Author of record | |
| Date | |
| Commit reviewed (short hash) | |
| Checklist items covered | 1 ☐ 2 ☐ 3 ☐ 4 ☐ 5 ☐ 6 ☐ |

| # | Section heading | What was checked | What was found | What was changed (commit) |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

**Outcome:** ☐ Checked, no changes needed ☐ Checked after corrections ☐ Needs revision

### Review R-02: `01-software-and-logic.md`
*(copy the tables above)*

### Review R-03: `03-symbolic-ai-vs-machine-learning.md`
*(copy the tables above)*

### Review R-04: `04-history-and-ai-winters.md`
*(copy the tables above)*

### Review R-05: `05-symbolic-ai-in-modern-software.md`
*(copy the tables above)*

### Review R-06: `06-test-bank.md` and `glossary.md`
*(copy the tables above)*

---

## 6. Learner tests

**How to run a learner test (20–30 minutes):**
1. The tester has **not** read the file before. They get only the rendered PDF pages for the chosen section, with the answer section removed.
2. They read the explanation and worked example, then do the activity **without help**, thinking aloud.
3. The author watches and writes down, without helping: where the tester hesitated, what they asked, and any wrong answers.
4. Afterwards, compare with the answer section, and ask: "Which sentence would you change?"
5. The author revises the section and records the before/after below.

**Recommended sections to test:** Topic 1 Task D · Topic 2 §4.3 + Part A · Topic 3 §3 + Activity A · Topic 4 §3 + Activity B · Topic 5 §2 + Activity A.

### Learner test T-01: Topic 2, §4.3 (forward chaining) and Activity Part A

| Field | Entry |
|---|---|
| Tester (did not write Topic 2) | |
| Observer / author | |
| Date | |
| Time taken | |
| **What the tester understood** (their own words) | |
| **Where they became confused** (quote the sentence) | |
| Their answer to Part A (correct?) | |
| **What we changed** (before → after, with commit) | |

### Learner test T-02: Topic 3, §3 and Activity A
*(copy the table above)*

### Learner test T-03 to T-05
*(one per remaining topic)*

---

## 7. Production corrections

Errors found while making the Study Guide, Test Bank, slides or videos. Fix the Markdown first, then every resource on that row of `docs/resource-mapping.md`.

| Date | Found in (resource) | Error | Markdown fix (file, section) | Other resources updated |
|---|---|---|---|---|
| | | | | |

---

## 8. Unresolved problems (for the submission report)

*Update before submission. Starting list from Section 3:* single-source history facts in Topic 4; XCON rule count; any learner-test issues not yet fixed.
