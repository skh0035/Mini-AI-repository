<img src="assets/silkmind-logo.png" alt="SilkMind team logo" width="140">

# SilkMind: Software & Symbolic AI

A beginner's learning module on **how software makes decisions and how rule-based (symbolic) AI reasons**. This repository holds the shared Markdown content that our Study Guide, PPT Slides and Video Tutorials are built from.

**Current version:** Markdown Content V1.1 (31 October 2026). See [Current progress](#current-progress-and-remaining-work).

---

## Team

| Member | GitHub | Role |
|---|---|---|
| Afandiyeva Hayat | [@afandiyevahayat](https://github.com/afandiyevahayat) | Team lead (CEO) |
| Khaydarov Sarvarbek | [@skh0035](https://github.com/skh0035) | Repository & information lead (CIO) |
| Nabizadehshahrbabak Arsalan | [@ArsalanVayu](https://github.com/ArsalanVayu) | Quality lead (reviews and merges pull requests) |
| Egemberdiyeva Aliya | [@All886](https://github.com/All886) | Content lead |
| Kenzhebolat Anel | [@anlinavie](https://github.com/anlinavie) | Visual design|
| Mukhtarov Mukhammadshakhruz | [@llex-27](https://github.com/llex-27) | Visual design & Video lead |
| Bakatov Madi | [@madi67-rgb](https://github.com/madi67-rgb) | Video lead |

*Student ID numbers are kept in the private submission report, not in this public repository.*

---

## Purpose and intended learners

**Purpose.** To give complete beginners a clear, connected path from "how does a program decide anything?" to "how does a rule-based AI reason, where did it succeed and fail, and where is it used today?"

**Intended learners.** First-year university students from any subject, with no prior programming, computer-science or AI background. Everyday computer use and basic comparisons (`<`, `>`) are the only prerequisites. See the [module outline](content/00-module-outline.md#1-who-this-module-is-for).

---

## Where to find things

```text
Mini-AI-repository/
├── README.md                                   ← you are here
├── content/                                    ← THE LEARNING CONTENT (read in this order)
│   ├── 00-module-outline.md                    outcomes, sequence, status of every section, known gaps
│   ├── 01-software-and-logic.md                Topic 1
│   ├── 02-rules-and-inference.md               Topic 2 (fully developed topic)
│   ├── 03-symbolic-ai-vs-machine-learning.md   Topic 3
│   ├── 04-history-and-ai-winters.md            Topic 4
│   └── 05-symbolic-ai-in-modern-software.md    Topic 5
├── assets/                                     ← images used by the content
│   ├── topic01-login-flowchart.png
│   ├── topic02-expert-system-architecture.png
│   ├── topic02-forward-chaining.png
│   ├── topic03-rules-vs-learning.png
│   ├── silkmind-logo.png
│   └── diagram-sources/                        editable Graphviz (.dot) sources for the diagrams
├── pdf/
│   └── SilkMind_Learning_Content_V1.1.pdf          rendered, readable copy of all content (outline + Topics 1–5)
├── examples/
│   └── topic02_mini_rule_engine.py             optional runnable demo for Topic 2 (Python 3, no packages)
└── docs/                                       ← project management (no personal logs)
    ├── project-plan.md                         plan, task list, owners, deadlines
    ├── project-plan-designed.pdf               designed version of the Stage 1 plan
    ├── review-log.md                           peer-review records
    ├── ai-use-log.md                           project-level record of AI assistance
    └── changelog.md                            what changed between versions and why
```

All images use **relative paths** (e.g. `../assets/topic02-forward-chaining.png`), so the content renders correctly from a downloaded copy as well as on GitHub.

---

## Content status at a glance

| Topic | File | Status |
|---|---|---|
| Module outline | [`00-module-outline.md`](content/00-module-outline.md) | Drafted |
| 1. Software and basic logic | [`01-software-and-logic.md`](content/01-software-and-logic.md) | Drafted (revised from V1.0) |
| 2. Rules and inference ★ | [`02-rules-and-inference.md`](content/02-rules-and-inference.md) | Drafted: fully developed, awaiting review |
| 3. Symbolic AI vs machine learning | [`03-symbolic-ai-vs-machine-learning.md`](content/03-symbolic-ai-vs-machine-learning.md) | Drafted |
| 4. History and AI winters | [`04-history-and-ai-winters.md`](content/04-history-and-ai-winters.md) | Drafted (dates need second source) |
| 5. Symbolic AI in modern software | [`05-symbolic-ai-in-modern-software.md`](content/05-symbolic-ai-in-modern-software.md) | Drafted (module quiz: outline only) |

Status labels: **Outline only → Drafted → Checked** (or **Needs revision**). A section becomes *Checked* only after a second member records a review in [`docs/review-log.md`](docs/review-log.md).

---

## Project plan and task list

The full task list, with owners and deadlines, is in [`docs/project-plan.md`](docs/project-plan.md). A designed overview is in [`docs/project-plan-designed.pdf`](docs/project-plan-designed.pdf).

**How we work on GitHub**
- Each member works on a branch and opens a **pull request**; the Quality lead (or another member) reviews it before merging.
- Commit messages say *what changed and why*, e.g. `Topic 2: fix activity answer for Part A (R5 should not fire)`.
- Day-to-day coordination happens in our WeChat group; decisions that affect the content are recorded in pull-request comments or in `docs/review-log.md`.

---

## Current progress and remaining work

**Done (as of 31 Oct 2026)**
- Module outline covering all five topics, with learning outcomes, prerequisites, sequence rationale, status per subtopic and a list of known gaps.
- Topic 2 fully developed: explanations, terminology, worked example with trace table, two diagrams, 4-part activity with answers, real-world examples, references, and a tested code demo.
- Topic 1 revised (activity/answer mismatch fixed, terms defined at first use, self-check added).
- Topics 3–5 drafted with explanations, examples, activities, answers and references.

**Remaining**
1. Peer review of every topic, recorded in `docs/review-log.md`. Nothing is marked *Checked* yet.
2. Confirm Topic 4 dates and Topic 2 XCON figures in a second source.
3. Find sources for, or relabel, the general examples in Topic 5 §1.2.
4. Module self-assessment quiz (Topic 5) and a designed timeline graphic (Topic 4).
5. Convert Topic 2 into the first Study Guide chapter, slide set and video (Stage 2).
