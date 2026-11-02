# Revision Summary (Stage 1 → Stage 2)

For the Stage 2 submission report. Sources of feedback: the Stage 1 mark (22/30) and our own analysis of it against the Stage 1 brief, plus problems found by our own review and testing in V2.0.

> **To the team:** if written teacher feedback for Stage 1 is available, add each comment as its own row at the top and point to the change that answers it. Any suggestion we did *not* adopt must be listed with a reason.

| # | Feedback or problem | What changed and why | Where to find the change |
|---|---|---|---|
| 1 | Stage 1: only one topic had real content; Topics 2–4 were three-line placeholders | All five topics now have explanations, a worked example, a visual, activities with answers, misconceptions and references | `content/01`–`05`, all sections |
| 2 | Stage 1: the developed topic was general software basics; no symbolic-AI content | Topic 2 now teaches the core of symbolic AI (knowledge base, working memory, inference engine, forward/backward chaining, explanations) with six activities | `02-rules-and-inference.md`, §3–§6 |
| 3 | Stage 1: illogical sequence; history of the AI winter came before learners met symbolic AI | Re-ordered to Logic → Rules → Symbolic vs ML → History → Modern use; reasons and "thread" activities documented | `00-module-outline.md`, §3 "Learning sequence and why it is in this order" |
| 4 | Stage 1: leftover AI-chatbot markers (`[cite: 1]`) in the outline; no AI-use record | Outline rewritten; markers removed; AI use logged | `00-module-outline.md`; `docs/ai-use-log.md` |
| 5 | Stage 1: Topic 1 activity asked for "3 rules" but the answer gave 3 steps | Activity reworded to "3-step algorithm with one IF–THEN–ELSE rule" | `01-software-and-logic.md`, §5 "Learner activities" (Task A) |
| 6 | Stage 1: terms *truth table*, *pseudocode* and *condition* used before being defined | Defined at first use; all terms collected in a glossary with one definition each | `01-software-and-logic.md`, §2.3 and §3; `glossary.md` |
| 7 | Stage 2 brief: avoid relying on recall; include tracing, predicting, comparing, explaining and **finding errors** | Added find-the-error tasks to every topic (OR login rule; impossible trace; accuracy claim; date/cost claim; decision-table gap) and predict tasks (rule conflict; game guard) | Topic 1 §5 Task D; Topic 2 §5 Parts E–F; Topic 3 §6 Activity D; Topic 4 §6 Activity D; Topic 5 §6 Activities A–B |
| 8 | Stage 2 brief: address likely misunderstandings | "Common misunderstandings" table in every topic | Topic 1 §7; Topic 2 §7; Topic 3 §5; Topic 4 §5; Topic 5 §5 |
| 9 | Own review: Topic 3 never showed *how* a computer learns; ML was only described | New hand-traceable worked example: learning a threshold rule from 10 labelled emails, with a mistakes table and a runnable demo | `03-symbolic-ai-vs-machine-learning.md`, §3 "Worked example: watching a computer 'learn' a rule"; `examples/topic03_learn_a_rule.py` |
| 10 | Own testing: running the demo showed our first answer to Topic 3 Activity A was wrong (we said k = 3 and 4 tie; k = 2 also ties) | Answer table corrected to include k = 2; explanation of ties added | `03-symbolic-ai-vs-machine-learning.md`, §7 "Activity A" |
| 11 | Own source check: Topic 4 gave the Fifth Generation project as 1981–1991 costing $850M (single secondary source) | Corrected to 1982–1992 using the IPSJ Computer Museum and *Nature* (1992); cost figures shown as disagreeing; turned into a learner activity on checking claims | `04-history-and-ai-winters.md`, §2 "Timeline" and §6–7 Activity D |
| 12 | V1.1 review flag: XCON figures supported only by Wikipedia | Deployment date confirmed in McDermott (1981); $25M/year saving confirmed in Middlesex University notes; rule count softened to "by one account" | `02-rules-and-inference.md`, §8 "Real expert systems, and their limits"; §11 References |
| 13 | V1.1 review flag: Topic 5 examples (forms, games) had no sources | Forms sourced to MDN; game characters sourced to a game-design lecture; tax example replaced by an invented delivery-fee table labelled as our own | `05-symbolic-ai-in-modern-software.md`, §1.1–1.3; §9 References |
| 14 | Stage 1 outline gap: Topic 4 timeline graphic "outline only" | Timeline graphic drawn (Figure 4.1), with editable source | `04-history-and-ai-winters.md`, §2; `assets/topic04-ai-timeline.png` |
| 15 | Stage 1 outline gap: module quiz "outline only" | 25-question test bank, mapped to all 7 learning outcomes, answers checked | `06-test-bank.md` |
| 16 | Own review: terminology inconsistent ("rules engine" vs "inference engine"; "Symbolic AI" vs "symbolic AI") | Glossary fixes one term for each idea; text standardised | `glossary.md` "Consistency decisions"; Topic 5 §1.2 |
| 17 | Stage 1: weak evidence of review | Review assignments, learner-test protocol and records added; AI-assisted source check recorded separately from peer review | `docs/review-log.md` |

**Not adopted:**

| Suggestion | Reason |
|---|---|
| Teach how real neural networks are trained (Stage 1 outline gap #4) | Requires maths beyond our beginner audience; the threshold example (Topic 3 §3) teaches the core idea, and §3.5 states clearly what it leaves out. |
| Cover uncertain reasoning in full | Kept as a short, clearly labelled optional box (Topic 2 §8) so that every core trace stays checkable by hand. |
