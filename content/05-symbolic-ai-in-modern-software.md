# Topic 5: Symbolic AI in Modern Software

**Level:** Beginner  |  **Estimated time:** 25 minutes  |  **Status:** Drafted (awaiting team review; module quiz is outline only)
**Builds on:** Topics 1–4

**Learning objectives.** After this topic you will be able to:

1. Identify rule-based reasoning inside everyday software.
2. Explain what a knowledge graph is, using a simple example.
3. Describe how a "neuro-symbolic" system combines learning with rules, using one real example.

---

## 1. Rules did not disappear

Topic 4 ended with the AI winters. But the idea of IF–THEN rules plus an engine that applies them never went away. It became an ordinary part of software engineering, and is so ordinary that it is rarely called "AI" any more.

### 1.1 Business rules engines

> **Business rules engine:** software that stores an organisation's decision rules separately from the rest of the program, so that staff can update the rules without rewriting the program.

Salesforce, for example, sells a Business Rules Engine. Its own training material says that it automates complex decisions, organises rules in tools such as **decision tables**, and lists uses such as checking **eligibility** for discounts, fee refunds and public benefits, and calculating insurance quotes ([Salesforce Trailhead: Get to Know Business Rules Engine](https://trailhead.salesforce.com/content/learn/modules/business-rules-engine/get-to-know-business-rules-engine)).

> **Decision table:** a table in which each row is one rule: the columns on the left are conditions, the column on the right is the result. It is a compact way to write many IF–THEN rules.

**Example: a student bus-pass discount as a decision table** *(our own illustration)*

| Rule | Is a student? | Age ≥ 65? | Result |
|---|---|---|---|
| D1 | Yes | – | 50% discount |
| D2 | No | Yes | 50% discount |
| D3 | No | No | Full price |

Compare this with Topic 1: each row is an IF–THEN rule, and the table as a whole is the OR condition `student OR age ≥ 65`. Compare it with Topic 2: the table is a small **knowledge base**, and the rules engine is the **inference engine**.

### 1.2 Where else you meet rules *(examples for discussion; see review note)*

- **Online forms** that refuse to submit until required fields are filled in.
- **Tax and benefit calculators** that apply bands set by law (Topic 3, Activity Q3).
- **Characters in video games** that follow rules such as "IF the player is visible AND health is low THEN run away".

---

## 2. Knowledge graphs: facts as a network

> **Knowledge graph:** a large collection of facts stored as **things** (people, places, objects) connected by **relationships**, for example `Taj Mahal --located in--> Agra`.

In 2012 Google introduced its Knowledge Graph to help search understand "things, not strings". At launch it held over 500 million objects and more than 3.5 billion facts about them and their relationships. This lets a search tell, for example, the Taj Mahal monument apart from a musician of the same name ([Google: Introducing the Knowledge Graph](https://blog.google/products/search/introducing-knowledge-graph-things-not/)).

This is symbolic AI at a very large scale: facts are stored as readable symbols, and the system can follow the links between them, just as the inference engine in Topic 2 followed rules from fact to fact.

```text
Taj Mahal --is a--> monument
Taj Mahal --located in--> Agra
Agra --located in--> India
=> Taj Mahal is located in India   (a new fact found by following two links)
```

---

## 3. Neuro-symbolic AI: learning and rules together

> **Neuro-symbolic AI:** a system that combines a **neural network** (a type of machine-learning model, Topic 3) with **symbolic reasoning** (rules and logic, Topic 2), so that each covers the other's weaknesses.

**Case study: AlphaGeometry (Google DeepMind, January 2024)** ([DeepMind blog](https://deepmind.google/blog/alphageometry-an-olympiad-level-ai-system-for-geometry/))

- **Symbolic part:** a deduction engine that applies geometry rules step by step to prove new statements, exactly like forward chaining.
- **Learning part:** a language model that, when the engine gets stuck, suggests one useful new construction (a point, line or circle) to add to the diagram. Then the engine continues.
- **Result:** on 30 olympiad geometry problems, it solved 25 within the time limit, compared with 10 for the previous best method. The average human gold medallist solves 25.9.
- **Why combine them:** DeepMind describes the language model as giving fast "intuition" and the symbolic engine as giving rigorous reasoning that can be checked.

This is a neat summary of the whole module: the rules provide reasoning that can be **explained and checked** (Topic 2), and learning provides **flexibility** that hand-written rules lack (Topic 3).

---

## 4. Learner activity: spot the rules

Choose an app or website you use often (for example a food-delivery app, a course-registration system, or a game).

1. Find **two** decisions it makes that are probably rule-based. Write each as an IF–THEN rule.
2. Find **one** feature that is probably based on machine learning. Explain why it would be hard to write as rules.
3. Is there a feature that seems to use **both**? Describe it in one sentence.

## 5. Expected outcome

There is no single correct answer; check that each response meets these criteria:

| Part | A good answer… | Example (food-delivery app) |
|---|---|---|
| 1 | States clear true/false conditions and a result | `IF order total < minimum THEN disable "Checkout"`; `IF restaurant is closed THEN hide "Order now"` |
| 2 | Names a feature that depends on patterns in lots of data | "Recommended for you": depends on millions of past orders; too many patterns to write as rules |
| 3 | Shows a learned part plus a rule part | Delivery-time estimate is learned from past trips, **but** a rule adds 10 minutes IF it is raining (*hypothetical example*) |

---

## 6. Module summary

| Topic | Big idea |
|---|---|
| 1 | Computers decide by testing true/false conditions with IF–THEN rules |
| 2 | Symbolic AI = a knowledge base of rules + an inference engine that chains them, and it can explain itself |
| 3 | Machine learning learns patterns from data instead; each approach suits different problems |
| 4 | Over-promising and the limits of rules caused two AI winters |
| 5 | Rules live on in everyday software, knowledge graphs, and neuro-symbolic systems |

*Module self-assessment quiz (8 questions covering LO1–LO7): **outline only**, planned for V2.0.*

---

## 7. References

Links accessed 31 October 2026.

1. Salesforce Trailhead. *Get to Know Business Rules Engine.* https://trailhead.salesforce.com/content/learn/modules/business-rules-engine/get-to-know-business-rules-engine
2. Singhal, A. (16 May 2012). *Introducing the Knowledge Graph: things, not strings.* Google. https://blog.google/products/search/introducing-knowledge-graph-things-not/
3. Google DeepMind (17 January 2024). *AlphaGeometry: An Olympiad-level AI system for geometry.* https://deepmind.google/blog/alphageometry-an-olympiad-level-ai-system-for-geometry/

**Review note:** the examples in Section 1.2 and the activity's example answers are general illustrations, not claims about specific products. A reviewer should either find a source for each or keep them clearly labelled as illustrations.
