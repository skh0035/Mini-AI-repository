# Topic 5: Symbolic AI in Modern Software

**Level:** Beginner  |  **Estimated time:** 40 minutes  |  **Status:** Drafted V2.0 (awaiting peer review)
**Builds on:** Topics 1–4  |  **Followed by:** [Module test bank](06-test-bank.md)

**Learning objectives.** After this topic you will be able to:

1. Identify rule-based reasoning inside everyday software, and write it as rules or as a decision table.
2. Trace a rule-based game character through a sequence of events.
3. Explain what a knowledge graph is and follow links in it to answer a question.
4. Describe how a neuro-symbolic system combines learning with rules, using one real example.

---

## 1. Rules did not disappear

Topic 4 ended with the AI winters. But the idea of **IF–THEN rules plus a program that applies them** never went away. It became such an ordinary part of software that it is rarely called "AI" any more. This topic shows four places you meet it.

### 1.1 Online forms

When you leave a required box empty on a website form and press *Submit*, the browser blocks the form and shows a message such as "Please fill out this field". This is a rule built into web browsers: a field marked `required` must not be empty, and the browser checks it before the form is sent ([MDN Web Docs: Client-side form validation](https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms/Form_validation)).

```text
IF field is required AND field is empty THEN block submission AND show message
```

This is a Boolean condition from Topic 1, applied automatically by software.

### 1.2 Business rules and decision tables

> **Business rules engine:** software that stores an organisation's decision rules separately from the rest of the program, so that staff can change the rules without rewriting the program.

Salesforce, for example, sells a Business Rules Engine. Its training material describes it as automating complex decisions, organising rules in tools such as **decision tables**, and lists uses such as checking **eligibility** for discounts and public benefits and calculating insurance quotes ([Salesforce Trailhead: Get to Know Business Rules Engine](https://trailhead.salesforce.com/content/learn/modules/business-rules-engine/get-to-know-business-rules-engine)).

> **Decision table:** a table in which each row is one rule. The columns on the left are conditions, and the column on the right is the result. It is a compact way to write many IF–THEN rules, and it makes it easy to check that **every case is covered exactly once**.

**Example: a bus-pass discount** *(our own illustration)*

| Rule | Is a student? | Age ≥ 65? | Result |
|---|---|---|---|
| D1 | Yes | (any) | 50% discount |
| D2 | No | Yes | 50% discount |
| D3 | No | No | Full price |

Each row is an IF–THEN rule (Topic 1). The table as a whole is the condition `student OR age ≥ 65`. In Topic 2's terms, the table is a small **knowledge base** and the business rules engine plays the role of the **inference engine**.

### 1.3 Characters in video games

Many computer-controlled characters follow a **finite state machine**: the character is always in one **state** (such as *Wander*, *Attack* or *Flee*) and changes state when a rule's condition becomes true. Game-design teaching material describes this as the most common pattern for game AI, because it is easy to draw, program and debug ([*Principles of Computer Game Design and Implementation*, Lecture 23](https://intranet.csc.liv.ac.uk/~xiaowei/game_materials/lecture23.pdf)).

> **State:** what the character is currently doing.
> **Transition:** a rule that moves the character from one state to another: `IF (current state) AND (condition) THEN (new state)`.

The lecture's example guard uses these transition rules:

| Rule | IF current state is… | AND… | THEN new state |
|---|---|---|---|
| G1 | Wander | player is seen | Attack |
| G2 | Attack | health is low | Flee |
| G3 | Attack | no player is present | Wander |
| G4 | Flee | no player is present | Wander |

If no rule matches, the character **stays in its current state**.

---

## 2. Worked example: tracing a game guard

The guard starts in **Wander** with full health. Here is what happens over five moments of play:

| Moment | What is happening | Current state | Rule that matches | New state |
|---|---|---|---|---|
| 1 | Player not visible | Wander | none (G1 needs "player is seen") | **Wander** |
| 2 | Player comes into view | Wander | **G1** | **Attack** |
| 3 | Player still visible; guard's health falls to low | Attack | **G2** | **Flee** |
| 4 | Player still visible | Flee | none (G4 needs "no player present") | **Flee** |
| 5 | Player leaves | Flee | **G4** | **Wander** |

**What to notice:**
- In each moment the guard checks only the rules for its **current** state, just as an inference engine checks which rules have a true IF part (Topic 2).
- At moment 4 the player is visible, but the guard does *not* attack again. No rule says "Flee + player seen → Attack". The behaviour is entirely decided by the rules people wrote, including what they left out.
- Because each state change is caused by a named rule, a game designer can explain exactly *why* the guard ran away (rule G2), which is the explainability strength from Topic 2.

---

## 3. Knowledge graphs: facts as a network

> **Knowledge graph:** a large collection of facts stored as **things** (people, places, objects) connected by named **relationships**. Each fact has the form *thing → relationship → thing*.

In 2012 Google introduced its Knowledge Graph to help its search engine understand "things, not strings". At launch it held over 500 million objects and more than 3.5 billion facts about them and their relationships, which lets a search tell, for example, the Taj Mahal monument apart from a musician with the same name ([Google: Introducing the Knowledge Graph](https://blog.google/products/search/introducing-knowledge-graph-things-not/)).

### Worked example: following links with a rule

A tiny knowledge graph *(our own example)*:

```text
Registan   --located in-->  Samarkand
Samarkand  --located in-->  Uzbekistan
Uzbekistan --located in-->  Central Asia
Registan   --is a-->        public square
```

The graph does **not** store "Registan is located in Central Asia". But one rule lets the system work it out:

```text
L1: IF X is located in Y AND Y is located in Z THEN X is located in Z
```

**Question:** Is the Registan located in Central Asia?

| Step | Facts used | Rule | New fact |
|---|---|---|---|
| 1 | Registan → Samarkand; Samarkand → Uzbekistan | L1 | Registan is located in Uzbekistan |
| 2 | Registan → Uzbekistan (new); Uzbekistan → Central Asia | L1 | **Registan is located in Central Asia** |

This is **forward chaining** (Topic 2) on a network of facts. Large knowledge graphs do the same thing with billions of facts.

---

## 4. Neuro-symbolic AI: learning and rules together

> **Neuro-symbolic AI:** a system that combines a **neural network** (a type of machine-learning model, Topic 3) with **symbolic reasoning** (rules and logic, Topic 2), so that each covers the other's weaknesses.

**Case study: AlphaGeometry (Google DeepMind, January 2024)** ([DeepMind blog](https://deepmind.google/blog/alphageometry-an-olympiad-level-ai-system-for-geometry/))

| Part | What it does | Which topic it comes from |
|---|---|---|
| **Symbolic deduction engine** | Applies geometry rules step by step to derive new facts about the diagram, like forward chaining | Topic 2 |
| **Language model** (learned from data) | When the engine gets stuck, suggests one useful new construction (a point, line or circle) to add; then the engine continues | Topic 3 |

- **Result:** on 30 olympiad geometry problems, AlphaGeometry solved 25 within the time limit. The previous best automatic method solved 10, and the average human gold medallist solves 25.9.
- **Why combine them:** DeepMind describes the language model as providing fast "intuition" and the symbolic engine as providing rigorous reasoning that can be checked.

This sums up the whole module: rules give reasoning that can be **explained and checked** (Topic 2), and learning gives **flexibility** that hand-written rules lack (Topic 3).

---

## 5. Common misunderstandings

| Misunderstanding | What is actually true |
|---|---|
| "If it isn't machine learning, it isn't AI." | Rule-based reasoning is the original form of AI (Topics 2 and 4) and is still used. It is simply less often *called* AI now. |
| "A game character that seems clever must be learning." | Most follow hand-written state rules (§1.3). Their "intelligence" is the designer's rules, as the moment-4 example in §2 shows. |
| "A knowledge graph knows only the facts typed into it." | It can also derive new facts by applying rules to the links (§3), just like an inference engine. |
| "Neuro-symbolic systems replaced rules with learning." | They keep both: in AlphaGeometry the symbolic engine does the actual proof. |

---

## 6. Learner activities

**Activity A: trace the guard (predict).** Using rules G1–G4, the guard starts in **Wander**. Predict its state after each moment:
1. Player seen, health full
2. Player not present, health full
3. Player seen, health low
4. Player seen, health low
5. Player not present, health low

**Activity B: find the error in a decision table.** A delivery app uses this table:

| Rule | Distance (km) | Fee |
|---|---|---|
| F1 | less than 5 | €2 |
| F2 | more than 5 and at most 10 | €4 |
| F3 | more than 10 | €6 |

A customer exactly 5 km away gets an error. Find the problem and correct the table. (Hint: Topic 1, Task B.)

**Activity C: follow the graph.** Add these facts to the graph in §3: `Bukhara --located in--> Uzbekistan` and `Ark of Bukhara --located in--> Bukhara`. Show, step by step with rule L1, how the system concludes that the Ark of Bukhara is in Central Asia.

**Activity D: spot the rules in an app you use.** Choose an app or website you use often.
1. Find **two** decisions it probably makes using rules. Write each as an IF–THEN rule.
2. Find **one** feature that probably uses machine learning, and explain why it would be hard to write as rules.
3. Is there a feature that seems to use **both**? Describe it in one sentence.

---

## 7. Expected outcomes and answers

### Activity A

| Moment | Rule | State after |
|---|---|---|
| 1 | G1 | Attack |
| 2 | G3 | Wander |
| 3 | G1 (in Wander, only G1 can apply; health does not matter in Wander) | Attack |
| 4 | G2 | Flee |
| 5 | G4 | Wander |

The trap is moment 3: the guard is in **Wander**, so G2 (which needs state *Attack*) cannot fire yet. It attacks first, then flees at moment 4. Checking the **current state** first is the key step.

### Activity B

The table has a **gap**: 5 km is not "less than 5" (F1) and not "more than 5" (F2), so no rule matches. This is the same strict-boundary issue as 18 °C in Topic 1. One correct table:

| Rule | Distance (km) | Fee |
|---|---|---|
| F1 | less than 5 | €2 |
| F2 | **at least 5** and at most 10 | €4 |
| F3 | more than 10 | €6 |

Check: every distance now falls into **exactly one** row (no gaps, no overlaps). Making F1 "at most 5" is also correct, as long as F2 then starts at "more than 5".

### Activity C

| Step | Facts used | Rule | New fact |
|---|---|---|---|
| 1 | Ark of Bukhara → Bukhara; Bukhara → Uzbekistan | L1 | Ark of Bukhara is located in Uzbekistan |
| 2 | Ark of Bukhara → Uzbekistan; Uzbekistan → Central Asia | L1 | **Ark of Bukhara is located in Central Asia** |

### Activity D

There is no single correct answer. Check each response against these criteria:

| Part | A good answer… | Example (food-delivery app) *(our illustration)* |
|---|---|---|
| 1 | States clear true/false conditions and a result | `IF order total < minimum THEN disable "Checkout"`; `IF restaurant is closed THEN hide "Order now"` |
| 2 | Names a feature that depends on patterns in lots of data | "Recommended for you": depends on millions of past orders; too many patterns to write as rules |
| 3 | Shows a learned part plus a rule part | Delivery-time estimate learned from past trips, **plus** a rule that adds 10 minutes IF it is raining |

### Common mistakes

1. Activity A: applying a rule for the wrong state (e.g. G2 while still in Wander).
2. Activity B: fixing the gap but creating an overlap (e.g. F1 "at most 5" *and* F2 "at least 5" both match 5 km).
3. Activity D: calling any automatic feature "machine learning". A fixed IF–THEN check is a rule.

---

## 8. Module summary

| Topic | Big idea |
|---|---|
| 1 | Computers decide by testing true/false conditions with IF–THEN rules |
| 2 | Symbolic AI = a knowledge base of rules + an inference engine that chains them, and it can explain itself |
| 3 | Machine learning chooses its rule from labelled data instead; each approach suits different problems |
| 4 | Over-promising and the limits of rules caused two AI winters |
| 5 | Rules live on in forms, business rules, games, knowledge graphs and neuro-symbolic systems |

**Check yourself:** the [module test bank](06-test-bank.md) has questions on every topic, with answers.

---

## 9. References

Links accessed 31 October and 3 November 2026.

1. MDN Web Docs (Mozilla). *Client-side form validation.* https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms/Form_validation
2. Salesforce Trailhead. *Get to Know Business Rules Engine.* https://trailhead.salesforce.com/content/learn/modules/business-rules-engine/get-to-know-business-rules-engine
3. *Principles of Computer Game Design and Implementation*, Lecture 23 (finite state machines; Wander / Attack / Flee example). University of Liverpool course material. https://intranet.csc.liv.ac.uk/~xiaowei/game_materials/lecture23.pdf
4. Singhal, A. (16 May 2012). *Introducing the Knowledge Graph: things, not strings.* Google. https://blog.google/products/search/introducing-knowledge-graph-things-not/
5. Google DeepMind (17 January 2024). *AlphaGeometry: An Olympiad-level AI system for geometry.* https://deepmind.google/blog/alphageometry-an-olympiad-level-ai-system-for-geometry/

**Our own material:** the bus-pass table, the delivery-fee table, the five-moment guard trace, the Registan/Bukhara graph, rule L1 and the food-delivery examples are written by the team for teaching. The guard's four transition rules follow the lecture's example; the trace and activity are ours.
