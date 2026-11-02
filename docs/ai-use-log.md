# Project AI-Use Log

This is the **project-level** record of significant AI assistance, kept as required by Section 6 of the Shared Assignment Rules. Each member's **personal log** (kept privately, not in this public repository) records their own prompts, decisions and verification.

For each entry, we record what the AI was asked to do, what it produced, what we kept or changed, and how we verified it.

---

## Entry A-01: V1.0 module outline (October 2026)

| Field | Entry |
|---|---|
| Tool | *(team to fill in: which chatbot was used)* |
| Used by | *(name)* |
| What it was used for | Drafting parts of the V1.0 `Module outline.md` |
| Evidence | The V1.0 file contained leftover `[cite: 1]` markers from the chatbot's citation format. These were removed in V1.1, and the outline was rewritten. |
| Verification | *(team to fill in)* |

> This entry was missing from the V1.0 submission. It is added here so the record is complete.

---

## Entry A-02: V1.1 revision (31 October 2026)

| Field | Entry |
|---|---|
| Tool | Claude (Anthropic), model Claude Opus 5.5, used through claude.ai |
| Used by | Khaydarov Sarvarbek (@skh0035) |
| Prompt (summary) | Analyse our repository against the Stage 1 brief and explain why it scored 22/30; then revise the structure and the sample chapter. |
| What the AI produced | Rewritten `README.md`; new `content/00-module-outline.md`; revised Topic 1; new Topic 2 (fully developed), Topics 3–5 (drafts); three Graphviz diagrams; `examples/topic02_mini_rule_engine.py`; `docs/project-plan.md`; `docs/review-log.md` template; this log. It also renamed files and removed the test file. |
| Sources the AI consulted | Britannica (expert systems, machine learning), Wikipedia (forward chaining, XCON, AI winter), Dartmouth Alumni Magazine, Google DeepMind blog (AlphaGeometry), Google blog (Knowledge Graph), Salesforce Trailhead, IBM Developer. All are listed in each topic's References section. |
| What the AI checked itself | Ran the example program and confirmed its output matches the Topic 2 trace and activity answers. Viewed each diagram after rendering. |
| **What the team must still verify** | Every factual claim against its cited source (see "Points flagged for checking" in `review-log.md`). Every explanation and answer must be understood well enough to explain without notes. Proposed task owners in `project-plan.md`. |
| Kept / changed | *(team to fill in after review, e.g. "Aliya rewrote Topic 2 §2 in her own words; Arsalan corrected …")* |

---

## Entry A-03: Stage 2 / V2.0 drafting (3 November 2026)

| Field | Entry |
|---|---|
| Tool | Claude (Anthropic), configured model `claude-opus-5-5`, used through claude.ai |
| Used by | Khaydarov Sarvarbek (@skh0035) |
| Prompt (summary) | "Finish our GitHub as it needs to be in Stage 2", together with the Stage 2 brief. |
| What the AI produced | Expanded Topics 1–5 (misconceptions, find-the-error and predict activities, new worked examples for Topics 3 and 5); `examples/topic03_learn_a_rule.py`; Topic 4 timeline graphic; `content/06-test-bank.md`; `content/glossary.md`; `docs/resource-mapping.md`, `docs/revision-summary.md`, Stage 2 `docs/review-log.md`; updated outline, README and plan; README auto-structure workflow (adapted from Sarvarbek's script on the `skh0035_edit` branch). |
| Sources the AI consulted | Lighthill report (AIAI Edinburgh copy); IPSJ Computer Museum; *Nature* 356 (1992); McDermott (1981, 1982); Middlesex University XCON notes; MDN Web Docs; University of Liverpool game-design lecture; plus the V1.1 sources. All are listed in the topic References sections. |
| What the AI verified itself | Ran both example programs for every tracing answer (Topic 2 Parts A/E/F, Topic 3 §3 and Activity A, test bank Q7–Q10/Q13); this caught one wrong answer (Topic 3 Activity A). Compared history claims against a second source; this corrected the Fifth Generation dates. Checked all local links and viewed every figure. Full list: `docs/review-log.md` §4. |
| Decisions and limits | The AI did **not** record any peer review or learner test, because these must be done by team members. Review assignments and owners are *proposals*. |
| **What the team must still do** | Each author of record reads, edits and commits their topic under their own account; reviewers complete `review-log.md` §5–6; each member records their own verification and learning in their personal log. |
| Kept / changed | *(team to fill in after review)* |

---

## Entry template

| Field | Entry |
|---|---|
| Date | |
| Tool and model | |
| Used by | |
| Prompt (summary or excerpt) | |
| What the AI produced | |
| What we kept, changed or rejected, and why | |
| How we verified it | |
| Files / commits affected | |
