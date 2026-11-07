# Glossary

Every technical term in the module, with the **one definition we use everywhere** (Markdown, Study Guide, slides and videos). If a definition changes, change it here first, then in the topic file and every resource that uses it.

The **Topic** column shows where the term is first introduced.

| Term | Definition used in this module | Topic |
|---|---|---|
| **AI winter** | A period in which funding for and interest in AI research fall sharply, usually after expectations were set too high. | 4 |
| **Algorithm** | A step-by-step procedure that solves a problem in a finite number of clear steps. | 1 |
| **AND** | Boolean operator; true only when **both** parts are true. | 1 |
| **Backward chaining** | Inference that starts from a **goal** and works back to the facts needed to prove it (goal-driven). | 2 |
| **Boolean condition** (or **condition**) | A question or statement that can only be true or false, e.g. `T < 18`. | 1 |
| **Boolean logic** | Logic in which every statement is true or false, combined with AND, OR and NOT. | 1 |
| **Brittle** | Describes a system that fails badly on cases its rules do not cover. | 2 |
| **Business rules engine** | Software that stores an organisation's decision rules separately from the rest of the program, so they can be changed without rewriting the program. | 5 |
| **Combinatorial explosion** | The very rapid growth in the number of possible combinations as a problem gets larger. | 4 |
| **Decision table** | A table in which each row is one rule: conditions on the left, the result on the right. | 5 |
| **Expert system** | A program that uses AI methods, usually a knowledge base of rules and an inference engine, to solve problems in one specialised area. | 2 |
| **Fact** | A statement taken as true for the current case, e.g. `has feathers`. | 2 |
| **Feature** | A measurable property of an example that an ML program may use, e.g. number of links. | 3 |
| **Fire (a rule)** | What happens when the inference engine finds a rule's IF part true and adds its THEN part to working memory. | 2 |
| **Forward chaining** | Inference that starts from known facts and keeps firing rules until nothing new can be added (data-driven). | 2 |
| **Hardware** | The physical parts of a computer. | 1 |
| **Inference** | Working out a new fact from facts already known. | 2 |
| **Inference engine** | The program that repeatedly finds rules whose IF part is true and fires them. | 2 |
| **Knowledge base** | The stored collection of rules for one subject area; the same for every case. | 2 |
| **Knowledge graph** | A large collection of facts stored as things connected by named relationships. | 5 |
| **Label** / **labelled data** | The correct answer attached to an example / examples that each have their correct answer. | 3 |
| **Machine learning (ML)** | AI in which software learns patterns from data instead of following rules written in advance. | 3 |
| **Model** | The result of training: the learned "rule" used to answer new cases. | 3 |
| **Neuro-symbolic AI** | A system combining a neural network (learning) with symbolic reasoning (rules). | 5 |
| **NOT** | Boolean operator; flips true to false and false to true. | 1 |
| **OR** | Boolean operator; true when **at least one** part is true (including both). | 1 |
| **Prediction** | A model's answer for a new, unlabelled example. | 3 |
| **Pseudocode** | Program-like steps in plain language; used to plan an algorithm, cannot be run. | 1 |
| **Rule** | An IF–THEN statement: if all conditions (the IF part) are true, the conclusion (the THEN part) is added or carried out. | 1, 2 |
| **Rule conflict** | When two rules can both fire and give contradictory conclusions. | 2 |
| **Software** | The instructions (programs) that tell a computer what to do. | 1 |
| **State** / **transition** | What a rule-based character is currently doing / a rule that moves it to another state. | 5 |
| **Symbol** | A name or label that stands for something, e.g. `is a bird`. The computer does not know its meaning. | 2 |
| **Symbolic AI** | AI that represents knowledge as human-readable symbols and reasons by applying rules to them. | 1, 2 |
| **Threshold rule** | A rule that classifies by comparing one value with a cut-off, e.g. `links >= 4`. | 3 |
| **Training** | The process in which an ML program searches for the pattern that best fits labelled data. | 3 |
| **Truth table** | A table listing every combination of true/false inputs with the result for each. | 1 |
| **Working memory** | The facts about the current case: starting facts plus facts the engine adds. | 2 |

**Consistency decisions made in V2.0:**
- We say **"inference engine"**, never "rules engine", when talking about expert systems; "business rules engine" is used only for the commercial software in Topic 5.
- We say **"working memory"**, not "fact base" or "database", for the facts about the current case.
- Each topic writes **"IF part"** and **"THEN part"**; *condition*/*antecedent* and *conclusion*/*consequent* appear once in Topic 2 as alternative names only.
- **symbolic AI** is lower case in running text and capitalised only at the start of a sentence, in headings and in titles (the same as "machine learning").
