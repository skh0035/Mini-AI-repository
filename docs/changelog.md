# Changelog

## V2.0 (3 November 2026): Stage 2 content

Full details with locations: [`revision-summary.md`](revision-summary.md).

- Every topic now has a "Common misunderstandings" section and at least one find-the-error or predict activity.
- New worked examples: learning a threshold rule from labelled data (Topic 3, with `examples/topic03_learn_a_rule.py`); tracing a game guard; following a knowledge graph (Topic 5).
- New: `content/06-test-bank.md` (25 questions, LO-mapped), `content/glossary.md`, Topic 4 timeline graphic.
- Corrected: Fifth Generation project dates (now 1982–1992); Topic 3 Activity A answer (three-way tie).
- Sources strengthened: Lighthill report, IPSJ, *Nature* (1992), McDermott (1981, 1982), MDN, game-design lecture.
- New docs: `resource-mapping.md`, `revision-summary.md`; Stage 2 `review-log.md` with review assignments and learner-test protocol.
- README structure now updates automatically (GitHub Actions workflow).

## V1.1 (31 October 2026): revision after Stage 1 feedback (22/30)

| Area | V1.0 problem | V1.1 change |
|---|---|---|
| Coverage | Only Topic 1 had content; Topics 2–4 were three lines each | Topic 2 fully developed; Topics 3–5 drafted with explanations, examples, activities, answers and references |
| Module focus | The only developed topic was general software basics; no symbolic-AI content | Topic 2 now teaches the core of symbolic AI (facts, rules, knowledge base, inference engine, forward/backward chaining, explanations) |
| Sequence | Topic 1 said it led to "Symbolic AI", but the outline's Topic 2 was "AI Winter", so learners met the collapse of symbolic AI before symbolic AI | New order: Logic → Rules & inference → Symbolic vs ML → History → Modern use; reasons given in the outline |
| Outline | No gaps listed; "Fully Developed" label; broken file link; one learning outcome (contrast with other methods) had no topic | Status per subtopic using Outline only / Drafted / Checked / Needs revision; "Known gaps and uncertainties" section; every outcome mapped to a topic; links fixed |
| AI traces | `[cite: 1]` chatbot markers left in the outline; no AI-use log | Markers removed, outline rewritten; `docs/ai-use-log.md` added |
| Topic 1 | Activity asked for "3 rules" but answer gave 3 steps; *truth table* and *pseudocode* used before being defined; unused and weak references | Activity reworded; terms defined at first use; truth-table task and self-check added; references trimmed to the ones cited |
| Review | No documented review | `docs/review-log.md` with checklist, flagged points and record template |
| README | Student IDs in a public repo; stale "Week 1/2/3" plan; no task list; broken heading levels | IDs removed; status table; task list in `docs/project-plan.md`; current progress and remaining work updated |
| Files | `content.md` test file; file names with spaces and `&`; unreferenced 10 MB video of team members; 2 MB logo | Test file removed; files renamed `NN-topic-name.md`; video removed from public repo (keep it in the private report as meeting evidence); logo resized |
