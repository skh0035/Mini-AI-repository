# Module Outline: Software & Symbolic AI

**Team:** SilkMind  |  **Version:** Markdown Content V1.1 (revised after Stage 1 feedback)  |  **Last updated:** 31 October 2026

This outline is the map of the whole module. It shows what learners will be able to do, the order in which topics are taught and why, what each topic contains, and how far each section has been developed.

---

## 1. Who this module is for

**Intended learners:** first-year university students from any subject who have **no prior experience** of programming, computer science or artificial intelligence.

**What we assume learners can already do (prerequisites):**

| Prerequisite | Why it is needed | Where it is covered if missing |
|---|---|---|
| Use a computer or phone: open apps, log in, browse the web | All examples are built on everyday apps (login screens, thermostats, spam filters) | Not covered; assumed |
| Read a simple table | Truth tables and trace tables are used from Topic 1 onwards | Topic 1 explains how to read a truth table |
| Basic comparisons with numbers (`<`, `>`, `=`) | Rules such as `T < 18` | Topic 1, Section 3 |
| Everyday reasoning with "if … then …" | All rules are written in IF–THEN form | Built up in Topic 1 |

**Not required:** any programming language, maths beyond basic comparisons, or knowledge of how AI models are trained. The short Python demo in Topic 2 is optional.

---

## 2. Intended learning outcomes

By the end of the module, learners should be able to:

| # | Learning outcome | Taught in |
|---|---|---|
| LO1 | Explain what software, an algorithm and a Boolean condition are, using an everyday example. | Topic 1 |
| LO2 | Write a simple decision as an IF–THEN rule and check it with a truth table. | Topic 1 |
| LO3 | Describe the parts of a rule-based (symbolic) AI system: facts, rules, knowledge base and inference engine. | Topic 2 |
| LO4 | Trace forward chaining by hand to show how a rule-based system reaches a conclusion and explains it. | Topic 2 |
| LO5 | Contrast symbolic AI with machine learning and choose a suitable approach for a given problem. | Topic 3 |
| LO6 | Explain why symbolic AI rose, fell (the "AI winters") and changed, using key events as evidence. | Topic 4 |
| LO7 | Identify where rule-based reasoning is used in modern software, including systems that combine rules with machine learning. | Topic 5 |

---

## 3. Learning sequence and why it is in this order

```text
Topic 1  Software & basic logic        "Computers follow strict true/false rules"
   │
   ▼
Topic 2  Rules & inference             "Symbolic AI = many such rules + an engine that chains them"
   │
   ▼
Topic 3  Symbolic AI vs machine learning   "Writing the rules yourself vs learning them from data"
   │
   ▼
Topic 4  History: boom, AI winters, lessons   "Why the rules-only approach hit its limits"
   │
   ▼
Topic 5  Symbolic AI in modern software        "Where rules are still used today, alone or with ML"
```

**Why this order:**

- Topic 1 gives the one idea everything else depends on: a computer decides by testing true/false conditions.
- Topic 2 scales that idea up: a symbolic AI system is a large collection of IF–THEN rules plus a program that applies them automatically.
- Topic 3 introduces the other main approach (machine learning) only **after** learners understand rules, so the comparison has something concrete to compare.
- Topic 4 (history) comes after Topics 2–3 on purpose. The AI winters are much easier to understand once learners have seen a rule-based system and know what its limits are. *(In V1.0, history was Topic 2. We moved it, because learners would have been studying the collapse of something they had not yet met.)*
- Topic 5 closes the module by connecting everything to software learners use today.

---

## 4. Topic-by-topic plan and development status

**Status labels used:**

| Label | Meaning |
|---|---|
| **Outline only** | Headings and plan, no learning text yet |
| **Drafted** | Explanations, example and activity written; not yet reviewed by a second member |
| **Checked** | Reviewed by a second member; facts checked against sources; corrections made |
| **Needs revision** | Reviewed; problems found that are not yet fixed |

> **Honest note on status (31 Oct 2026):** the V1.1 text of Topics 2–5 and the revision of Topic 1 were drafted with AI assistance (see `docs/ai-use-log.md`). No section is labelled **Checked** until a team member has completed the review in `docs/review-log.md`.

### Topic 1: Introduction to Software and Basic Logic
**File:** [`01-software-and-logic.md`](01-software-and-logic.md)  |  **Outcomes:** LO1, LO2  |  **Est. time:** 30 min

| Subtopic | Planned example / activity | Status |
|---|---|---|
| 1.1 Software vs hardware | Quick-check table: sort 6 items into hardware/software | Drafted |
| 1.2 Algorithms | Recipe comparison; login check as an algorithm | Drafted |
| 1.3 Boolean conditions and operators (AND, OR, NOT) | Operator table with everyday examples | Drafted |
| 1.4 Worked example: login decision | Step-by-step trace, truth table, pseudocode, flowchart | Drafted (V1.0 content, revised) |
| 1.5 Learner activity: thermostat rule | Write a 3-step algorithm with one IF–THEN–ELSE rule; stretch task with AND | Drafted (activity wording fixed) |
| 1.6 Check your understanding | 4 short questions with answers | Drafted |

### Topic 2: Rules and Inference: How a Symbolic AI Reasons ★ *fully developed topic*
**File:** [`02-rules-and-inference.md`](02-rules-and-inference.md)  |  **Outcomes:** LO3, LO4  |  **Est. time:** 45 min

| Subtopic | Planned example / activity | Status |
|---|---|---|
| 2.1 What "symbolic" means | Symbols as labels; why the computer doesn't "understand" them | Drafted |
| 2.2 Facts, rules, knowledge base, working memory | Animal-identifier knowledge base (6 rules) | Drafted |
| 2.3 The inference engine and forward chaining | Worked example with cycle-by-cycle trace table + diagram | Drafted |
| 2.4 Backward chaining (goal-driven) | Same knowledge base, asking "Is it a penguin?" | Drafted |
| 2.5 Explanations ("why?") | How the system shows the rules that led to its answer | Drafted |
| 2.6 Real expert systems and their limits | DENDRAL, MYCIN, XCON; the MYCIN gunshot-wound limitation | Drafted |
| 2.7 Learner activity + answers | 4-part activity: trace, extend, backward chain, find the gap | Drafted |
| 2.8 Optional code demo | `examples/topic02_mini_rule_engine.py` (prints the same trace) | Drafted; code tested |

### Topic 3: Symbolic AI vs Machine Learning
**File:** [`03-symbolic-ai-vs-machine-learning.md`](03-symbolic-ai-vs-machine-learning.md)  |  **Outcome:** LO5  |  **Est. time:** 30 min

| Subtopic | Planned example / activity | Status |
|---|---|---|
| 3.1 Two ways to give a computer knowledge: write rules vs learn from examples | Diagram: rules + data → answers vs data + answers → rules | Drafted |
| 3.2 Same problem, two approaches: a spam filter | Rule-based filter vs a filter trained on labelled emails | Drafted |
| 3.3 Comparison table: explainability, data needed, flexibility, maintenance | Table | Drafted |
| 3.4 Learner activity: choose an approach for 5 scenarios | Answers with reasons | Drafted |
| 3.5 How machine learning actually trains a model | *Deliberately brief; beyond this module's scope* | Outline only |

### Topic 4: History: The Rise, the AI Winters and the Lessons
**File:** [`04-history-and-ai-winters.md`](04-history-and-ai-winters.md)  |  **Outcome:** LO6  |  **Est. time:** 25 min

| Subtopic | Planned example / activity | Status |
|---|---|---|
| 4.1 1956: the Dartmouth workshop and early optimism | Timeline | Drafted |
| 4.2 First AI winter (≈1974–1980): Lighthill report, funding cuts | Cause → effect table | Drafted |
| 4.3 The expert-system boom of the 1980s | XCON as a case study | Drafted |
| 4.4 Second AI winter (≈1987–1993): brittleness, maintenance cost, LISP machine collapse | Link back to the limits seen in Topic 2 | Drafted |
| 4.5 Learner activity: match each event to its cause | Answers | Drafted |
| 4.6 Timeline graphic for slides | Visual design lead to produce | Outline only |

### Topic 5: Symbolic AI in Modern Software
**File:** [`05-symbolic-ai-in-modern-software.md`](05-symbolic-ai-in-modern-software.md)  |  **Outcome:** LO7  |  **Est. time:** 25 min

| Subtopic | Planned example / activity | Status |
|---|---|---|
| 5.1 Rules hidden in everyday software (eligibility checks, forms, game characters) | Annotated examples | Drafted |
| 5.2 Knowledge graphs | Small fact-network example | Drafted |
| 5.3 Neuro-symbolic AI: rules + learning together | AlphaGeometry (2024) case study | Drafted |
| 5.4 Learner activity: spot the rules in an app you use | Expected-outcome guide | Drafted |
| 5.5 Module wrap-up and self-assessment quiz | 8-question quiz covering LO1–LO7 | Outline only |

---

## 5. Known gaps and uncertainties

We list these openly so that reviewers and the teacher can see what is still weak.

1. **No section is "Checked" yet.** A second team member must review each topic using `docs/review-log.md`.
2. **Topic 5 sources are thinner than Topics 1–2.** Section 5.1 describes general software practice (business rules, game AI) with few direct sources. We need one reliable source per example or must cut the example.
3. **Topic 4 dates are approximate.** Historians give slightly different start and end years for the AI winters. We use the commonly cited ranges and say "about".
4. **Topic 3 simplifies machine learning heavily.** We do not explain how training works. We need to check that the simplification does not become misleading.
5. **Uncertainty handling is not covered.** Real expert systems such as MYCIN used confidence values. We mention this only briefly in Topic 2; a short optional box could be added.
6. **Module quiz (5.5) and Topic 4 timeline graphic are not yet started.**

---

## 6. From Markdown to the three learning resources

| Resource | How this Markdown will be used | First section to convert |
|---|---|---|
| **Study Guide** | Each topic file becomes one chapter. Learning objectives, key terms, worked example, activity and answers are kept; answers move to an appendix so learners try first. | Topic 2 |
| **PPT Slides** | One slide per subtopic. Diagrams (login flowchart, expert-system architecture, forward-chaining trace) become the main slide visuals; trace tables are revealed one row per click. | Topic 2, Section 3 (forward-chaining trace) |
| **Video Tutorial** | A 4–5 minute screen recording that walks through the forward-chaining trace by hand, then runs `examples/topic02_mini_rule_engine.py` to show the computer producing the same trace. | Topic 2, Sections 3 and 8 |
