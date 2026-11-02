# Module Outline: Software & Symbolic AI

**Team:** SilkMind  |  **Version:** Markdown Content V2.0  |  **Last updated:** 3 November 2026

This outline is the map of the whole module. It shows what learners will be able to do, the order in which topics are taught and why, what each topic contains, and how far each section has been developed. Terms are defined consistently in the [glossary](glossary.md).

---

## 1. Who this module is for

**Intended learners:** first-year university students from any subject who have **no prior experience** of programming, computer science or artificial intelligence.

**What we assume learners can already do (prerequisites):**

| Prerequisite | Why it is needed | Where it is covered if missing |
|---|---|---|
| Use a computer or phone: open apps, log in, browse the web | All examples are built on everyday apps (login screens, thermostats, spam filters, games) | Not covered; assumed |
| Read a simple table | Truth tables, trace tables and decision tables are used throughout | Topic 1 explains how to read a truth table |
| Basic comparisons with numbers (`<`, `>`, `>=`, `=`) | Rules such as `T < 18` and `links >= 4` | Topic 1, Sections 2.3 and 6 (Task B) |
| Everyday reasoning with "if … then …" | All rules are written in IF–THEN form | Built up in Topic 1 |

**Not required:** any programming language, maths beyond counting and comparing, or knowledge of how real AI models are trained. The two Python demos (`examples/`) are optional; every result they print is also shown in the text.

---

## 2. Intended learning outcomes

By the end of the module, learners should be able to:

| # | Learning outcome | Taught in | Tested in ([test bank](06-test-bank.md)) |
|---|---|---|---|
| LO1 | Explain what software, an algorithm and a Boolean condition are, using an everyday example. | Topic 1 | Q1–Q2 |
| LO2 | Write a simple decision as an IF–THEN rule and check it with a truth table. | Topic 1 | Q3–Q5 |
| LO3 | Describe the parts of a rule-based (symbolic) AI system: facts, rules, knowledge base, working memory and inference engine. | Topic 2 | Q6, Q10, Q11 |
| LO4 | Trace forward and backward chaining by hand to show how a rule-based system reaches and explains a conclusion. | Topic 2 | Q7–Q9 |
| LO5 | Contrast symbolic AI with machine learning, trace a simple example of learning a rule from data, and choose a suitable approach for a problem. | Topic 3 | Q12–Q16 |
| LO6 | Explain why symbolic AI rose, fell (the "AI winters") and changed, using key events as evidence. | Topic 4 | Q17–Q20 |
| LO7 | Identify and trace rule-based reasoning in modern software, including systems that combine rules with machine learning. | Topic 5 | Q21–Q25 |

---

## 3. Learning sequence and why it is in this order

```text
Topic 1  Software & basic logic          "Computers decide with strict true/false rules"
   │
   ▼
Topic 2  Rules & inference               "Symbolic AI = many such rules + an engine that chains them"
   │
   ▼
Topic 3  Symbolic AI vs machine learning "Writing the rules yourself vs learning them from data"
   │
   ▼
Topic 4  History: boom, AI winters, lessons  "Why the rules-only approach hit its limits"
   │
   ▼
Topic 5  Symbolic AI in modern software  "Where rules are still used today, alone or with ML"
   │
   ▼
Test bank  25 questions across LO1–LO7
```

**Why this order:**

- **Topic 1** gives the one idea everything else depends on: a computer decides by testing true/false conditions.
- **Topic 2** scales that idea up: a symbolic AI system is a large collection of IF–THEN rules plus a program that applies them automatically.
- **Topic 3** introduces machine learning only **after** learners understand rules. Its worked example shows that a learned model is *also* a rule; the difference is who writes it.
- **Topic 4** (history) comes after Topics 2–3 on purpose. The AI winters make sense once learners have seen, in Topic 2's activities, exactly how rule bases fail (gaps and conflicts). *(In V1.0, history came second; it was moved in V1.1.)*
- **Topic 5** closes the module by reusing every earlier idea (conditions, decision tables, forward chaining, learning + rules) on software learners use today.

**How the topics connect (the "thread" activities):**

| Idea | Introduced | Reused in |
|---|---|---|
| Strict boundaries (`<` vs `<=`) | Topic 1, Task B (18 °C) | Topic 5, Activity B (5 km); Test bank Q4, Q23 |
| AND vs OR mistakes | Topic 1, Task D | Test bank Q5 |
| Gaps in a rule base | Topic 2, Part D | Topic 4 §4 (brittleness); Topic 5, Activity B |
| Rule conflicts | Topic 2, Part F | Topic 4 §4 (maintenance cost); Test bank Q19 |
| Forward chaining | Topic 2 §4.3 | Topic 5 §3 (knowledge graph); Topic 5 §4 (AlphaGeometry) |
| "A model is also a rule" | Topic 3 §3 | Topic 3 §5; Topic 5 §4 |

---

## 4. Topic-by-topic plan and development status

**Status labels used:**

| Label | Meaning |
|---|---|
| **Outline only** | Headings and plan, no learning text yet |
| **Drafted** | Explanations, worked example, activities and answers written; not yet reviewed by a second member |
| **Checked** | Reviewed by a member who did not write it; facts checked against sources; corrections made and recorded in [`docs/review-log.md`](../docs/review-log.md) |
| **Needs revision** | Reviewed; problems found that are not yet fixed |

> **Status note (3 Nov 2026):** all core sections are now **Drafted** with full learning content. None is labelled **Checked** yet, because peer reviews and learner tests are scheduled for 4–6 November (see `docs/review-log.md`). The V1.1 and V2.0 drafts were prepared with AI assistance (see `docs/ai-use-log.md`), so peer review is required before any section is marked Checked.

### Topic 1: Introduction to Software and Basic Logic
**File:** [`01-software-and-logic.md`](01-software-and-logic.md)  |  **Outcomes:** LO1, LO2  |  **Est. time:** 35 min

| Subtopic | Example / activity | Status |
|---|---|---|
| 2.1–2.2 Software, hardware, algorithms | Hardware/software table; recipe comparison | Drafted |
| 2.3 Boolean conditions, AND/OR/NOT, truth tables | Operator table with everyday examples | Drafted |
| 3 Worked example: login decision | Step-by-step trace, truth table, pseudocode | Drafted |
| 4 Flowchart | Figure 1.1 | Drafted |
| 5–6 Activities A–D with answers | Thermostat algorithm, boundary truth table, AND stretch task, **find the error** (OR login rule) | Drafted |
| 7 Common misunderstandings | 4 misconceptions | Drafted |
| 8 Check your understanding | 4 questions with answers | Drafted |

### Topic 2: Rules and Inference: How a Symbolic AI Reasons ★ *core topic*
**File:** [`02-rules-and-inference.md`](02-rules-and-inference.md)  |  **Outcomes:** LO3, LO4  |  **Est. time:** 55 min

| Subtopic | Example / activity | Status |
|---|---|---|
| 1–3 Symbols, facts, rules, knowledge base, working memory, inference engine | Detective comparison; Figure 2.1 | Drafted |
| 4.1–4.4 Forward chaining and explanations | Animal identifier; cycle-by-cycle trace table; Figure 2.2; "why?" chain | Drafted |
| 4.5 Backward chaining | Same knowledge base, goal "penguin?" | Drafted |
| 4.6 Code demo (optional) | `examples/topic02_mini_rule_engine.py` | Drafted; output checked |
| 5–6 Activities A–F with answers | Trace, extend, backward chain, find the gap, **find the error in a trace**, **predict a rule conflict** | Drafted; answers checked with demo |
| 7 Common misunderstandings | 5 misconceptions | Drafted |
| 8 Real expert systems and limits | DENDRAL, MYCIN, XCON; optional uncertainty box | Drafted; XCON re-sourced |

### Topic 3: Symbolic AI vs Machine Learning
**File:** [`03-symbolic-ai-vs-machine-learning.md`](03-symbolic-ai-vs-machine-learning.md)  |  **Outcome:** LO5  |  **Est. time:** 40 min

| Subtopic | Example / activity | Status |
|---|---|---|
| 1 Top-down vs bottom-up; ML terms | Term table; Figure 3.1 | Drafted |
| 2 Spam filter, two ways | Rule-based vs learned | Drafted |
| 3 Worked example: learning a threshold rule from 10 labelled emails | Mistakes table for every k; predictions; `examples/topic03_learn_a_rule.py` | Drafted; checked with demo (**new in V2.0**) |
| 4 Comparison table | 6 criteria | Drafted |
| 5 Common misunderstandings | 4 misconceptions | Drafted |
| 6–7 Activities A–D with answers | Retrain with new data, predict and explain, choose an approach, **find the error** in an accuracy claim | Drafted; Activity A checked with demo |

### Topic 4: History: The Rise, the AI Winters and the Lessons
**File:** [`04-history-and-ai-winters.md`](04-history-and-ai-winters.md)  |  **Outcome:** LO6  |  **Est. time:** 35 min

| Subtopic | Example / activity | Status |
|---|---|---|
| 1–2 AI winter; timeline 1956–1993 | Figure 4.1 timeline graphic (**new in V2.0**); event table | Drafted; dates re-checked |
| 3 Worked example: explaining the first winter step by step | Expectations / technology / effect method; combinatorial explosion | Drafted |
| 4 Second winter linked to Topic 2's limits | Table linking Parts D and F to industry problems | Drafted |
| 5 Common misunderstandings | 4 misconceptions | Drafted |
| 6–7 Activities A–D with answers | Order events, explain, predict, **check a claim against sources** | Drafted |

### Topic 5: Symbolic AI in Modern Software
**File:** [`05-symbolic-ai-in-modern-software.md`](05-symbolic-ai-in-modern-software.md)  |  **Outcome:** LO7  |  **Est. time:** 40 min

| Subtopic | Example / activity | Status |
|---|---|---|
| 1 Forms, business rules, decision tables, game characters | Sourced examples (MDN, Salesforce, game-design lecture) | Drafted; sources added in V2.0 |
| 2 Worked example: tracing a game guard | Five-moment state trace | Drafted (**new in V2.0**) |
| 3 Knowledge graphs + worked chaining example | Registan graph; rule L1 | Drafted |
| 4 Neuro-symbolic AI | AlphaGeometry case study | Drafted |
| 5 Common misunderstandings | 4 misconceptions | Drafted |
| 6–7 Activities A–D with answers | Trace the guard, **find the error in a decision table**, follow the graph, spot rules in an app | Drafted |

### Test bank and glossary
| File | Content | Status |
|---|---|---|
| [`06-test-bank.md`](06-test-bank.md) | 25 questions mapped to LO1–LO7 (6 recall, 8 apply, 11 analyse), with answers and explanations | Drafted; tracing answers checked with demos |
| [`glossary.md`](glossary.md) | 38 terms with the single definition used across all resources | Drafted |

### Optional extensions (clearly not core)
| Extension | Where | Status |
|---|---|---|
| Uncertain rules (confidence values) | Topic 2, box in §8 | Drafted (short box; not tested) |
| How real ML models are trained (beyond the threshold example) | Topic 3 | Not planned for this module |

---

## 5. Known gaps and how we will resolve them

| # | Gap | Plan | Owner / date |
|---|---|---|---|
| 1 | No section is **Checked** yet | Peer review of every file by a non-author + one learner test per topic, recorded in `docs/review-log.md` | See review assignments; 4–6 Nov |
| 2 | Some Topic 4 facts (DARPA 1974, LISP machines 1987, Strategic Computing 1988) and XCON's rule count have only one source (Wikipedia) | Reviewer to find a second source (e.g. Russell & Norvig textbook history chapter in the library); otherwise soften wording to "about" / "by one account" | Topic 4 reviewer; 6 Nov |
| 3 | The learner tests may show explanations that are too fast for beginners | Revise the affected sections and record before/after in `review-log.md` | Topic authors; 6 Nov |
| 4 | Study Guide, slides and videos are being built in parallel | Any error found in production is fixed here first, then in every resource (see `docs/resource-mapping.md`) | All; ongoing |

---

## 6. From Markdown to the three learning resources

The full section-by-section mapping is in [`docs/resource-mapping.md`](../docs/resource-mapping.md).
