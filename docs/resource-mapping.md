# Resource Mapping: Markdown → Study Guide / Test Bank, Slides, Videos

**Last updated:** 3 November 2026  |  **Markdown version:** V2.0

This table shows how each part of the shared Markdown content is used in the three Stage 2 learning resources. **The Markdown is the single source of truth:** if an error is found while making a slide or video, fix it here first, then in every resource listed on that row.

> **To the team:** slide numbers and video titles below are the *plan*. When the slides and videos exist, replace "planned" with the real slide numbers and video file names.

| Markdown file and section heading | Study Guide / Test Bank use | PPT use | Video Tutorial use |
|---|---|---|---|
| `00-module-outline.md` §2 Intended learning outcomes; §3 Learning sequence | Study Guide introduction: outcomes and "how to use this guide" | Slide deck 0: title, outcomes, module map | Opening of Video 1 (30 s module overview) |
| `01-software-and-logic.md` §2 Concept explanation | Chapter 1 §1–2 | Deck 1: software vs hardware; algorithm; AND/OR/NOT table | Not selected for video |
| `01-software-and-logic.md` §3 Worked example: login decision; §4 flowchart | Chapter 1 worked example | Deck 1: flowchart (Figure 1.1) built up box by box; truth table revealed row by row | **Video 1: "How does a login screen decide?"** (step-by-step trace) |
| `01-software-and-logic.md` §5–6 Activities A–D and answers | Chapter 1 practice + answers in appendix; Test bank Q3–Q5 | Deck 1: "Try it" slide (thermostat); answer slide | Video 1 ends with a "pause and try" on Task D (find the error) |
| `02-rules-and-inference.md` §2–3 Symbols and the parts of a rule-based system | Chapter 2 §1–3; Test bank Q6, Q11 | Deck 2: architecture diagram (Figure 2.1), one part highlighted per click | Video 2, first part |
| `02-rules-and-inference.md` §4.3 Forward chaining, step by step | Chapter 2 worked example; Test bank Q7, Q8 | Deck 2: trace table revealed one cycle per click; Figure 2.2 | **Video 2: "Forward chaining by hand, then by computer"** (hand trace, then run `topic02_mini_rule_engine.py`) |
| `02-rules-and-inference.md` §4.4–4.5 Explanations; backward chaining | Chapter 2 §4; Test bank Q9 | Deck 2: "why?" chain; forward vs backward comparison table | Video 2, last part (explanation printout) |
| `02-rules-and-inference.md` §5–7 Activities A–F, answers, misunderstandings | Chapter 2 practice + answers; misconceptions box; Test bank Q10 | Deck 2: Part F "predict the outcome" slide | Not selected for video |
| `02-rules-and-inference.md` §8 Real expert systems and limits | Chapter 2 case-study box | Deck 2: DENDRAL / MYCIN / XCON table | Not selected for video |
| `03-symbolic-ai-vs-machine-learning.md` §1–2 Two approaches; spam filter | Chapter 3 §1–2; Test bank Q12 | Deck 3: Figure 3.1 | Video 3, first part |
| `03-symbolic-ai-vs-machine-learning.md` §3 Worked example: learning a rule | Chapter 3 worked example; Test bank Q13 | Deck 3: data table → mistakes table → learned rule (3 slides) | **Video 3: "Watch a computer learn a rule"** (hand count for k = 2 and k = 4, then run `topic03_learn_a_rule.py`) |
| `03-symbolic-ai-vs-machine-learning.md` §4–7 Comparison, misunderstandings, activities | Chapter 3 comparison table and practice; Test bank Q14–Q16 | Deck 3: comparison table; "which approach?" quiz slide | Not selected for video |
| `04-history-and-ai-winters.md` §2 Timeline | Chapter 4 timeline; Test bank Q17 | Deck 4: Figure 4.1 timeline | Not selected for video |
| `04-history-and-ai-winters.md` §3 Worked example: explaining an event | Chapter 4 worked example; Test bank Q18 | Deck 4: expectations / technology / effect slide; combinatorial-explosion numbers | Not selected for video |
| `04-history-and-ai-winters.md` §4–7 Second winter, misunderstandings, activities | Chapter 4 practice; Test bank Q19–Q20 | Deck 4: Topic 2 limits → industry table | Not selected for video |
| `05-symbolic-ai-in-modern-software.md` §1 Forms, decision tables, game characters | Chapter 5 §1 | Deck 5: decision table; guard rules G1–G4 | **Video 4 (optional): "Inside a game guard's brain"** |
| `05-symbolic-ai-in-modern-software.md` §2 Worked example: tracing a game guard | Chapter 5 worked example; Test bank Q21–Q22 | Deck 5: state trace revealed one moment per click | Video 4 (optional) |
| `05-symbolic-ai-in-modern-software.md` §3–4 Knowledge graphs; neuro-symbolic AI | Chapter 5 §3–4; Test bank Q24–Q25 | Deck 5: graph diagram; AlphaGeometry two-part table | Not selected for video |
| `05-symbolic-ai-in-modern-software.md` §6–7 Activities and answers | Chapter 5 practice; Test bank Q23 | Deck 5: "find the error" decision-table slide | Not selected for video |
| `06-test-bank.md` (all) | **Test Bank** (all 25 questions; answers section) | One quick-check question at the end of each deck | "Pause and try" questions in Videos 1–3 |
| `glossary.md` | Study Guide glossary (appendix) | Definitions on concept slides use the same wording | Narration scripts use the same wording |

## Consistency rules for production

1. **Definitions** come from `glossary.md`, word for word.
2. **Examples and data** (rules R1–R6, the ten emails, guard rules G1–G4, the timeline dates) are copied, not retyped, from the Markdown.
3. **Answers** in the Study Guide and Test Bank must match `06-test-bank.md` and the topic answer sections exactly.
4. **Error found in production?** Fix the Markdown, record it in `docs/review-log.md` (Production corrections), then update every resource on that row.
