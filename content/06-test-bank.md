# Module Test Bank

**Status:** Drafted V2.0 (answers checked against the topic files; awaiting peer review)  |  **Used by:** Study Guide end-of-chapter questions, slide quick-checks, video "pause and try" moments

Each question is tagged with the **learning outcome** (LO, see [module outline](00-module-outline.md#2-intended-learning-outcomes)), the **topic and section** it tests, and its **type**:

- **Recall:** remember a definition or fact
- **Apply:** use an idea on a new case (trace, calculate, write a rule)
- **Analyse:** find an error, predict an outcome, compare or justify

Answers are in the second half of this file so learners can try first. Every answer refers back to the section that teaches it. **If an answer changes, update the topic file too** (and vice versa).

---

## Part 1: Questions

### Topic 1: Software and basic logic

**Q1** *(LO1 · Recall · Topic 1 §2.1)* Which of these is **software**?
a) a keyboard b) a temperature sensor c) an operating system d) a memory chip

**Q2** *(LO1 · Recall · Topic 1 §2.2)* Which property must every algorithm have?
a) It must be written in Python b) It must finish after a finite number of clear steps c) It must use AND d) It must run on a phone

**Q3** *(LO2 · Apply · Topic 1 §2.3)* `raining = False`, `snowing = True`. What is `raining OR snowing`? What is `NOT snowing`?

**Q4** *(LO2 · Apply · Topic 1 §5 Task B)* A fridge alarm rule is `IF T > 5 THEN alarm ON ELSE alarm OFF`. Complete the result for T = 4, 5 and 6.

**Q5** *(LO2 · Analyse · Topic 1 §5 Task D)* A library app uses `can_borrow = (has_card) OR (no_overdue_books)`. Give one situation where this rule gives the wrong result, and correct the rule.

### Topic 2: Rules and inference

Questions Q6–Q11 use the knowledge base from Topic 2, §4.1:

| Rule | IF … | THEN … |
|---|---|---|
| R1 | has feathers | is a bird |
| R2 | gives milk | is a mammal |
| R3 | is a bird AND cannot fly AND swims | is a penguin |
| R4 | is a bird AND can fly AND hunts at night | is an owl |
| R5 | is a mammal AND eats meat AND has black stripes | is a tiger |
| R6 | is a mammal AND has hooves AND has black stripes | is a zebra |

**Q6** *(LO3 · Recall · Topic 2 §3)* Which part of a rule-based system changes for every new case?
a) the knowledge base b) working memory c) the inference engine d) the rules

**Q7** *(LO4 · Apply · Topic 2 §4.3)* Trace forward chaining for the starting facts `has feathers`, `can fly`, `hunts at night`. Give the rule fired and new fact in each cycle, and the cycle in which the engine stops.

**Q8** *(LO4 · Analyse · Topic 2 §6 Part E)* A student's trace for `gives milk`, `has hooves`, `has black stripes` says: "Cycle 1: R6 fires → is a zebra." What is wrong?

**Q9** *(LO4 · Apply · Topic 2 §4.5)* Using backward chaining with the goal *is an owl?*, the system knows only `has feathers`. List the questions it must ask the user.

**Q10** *(LO3 · Analyse · Topic 2 §6 Part D)* The starting facts are `gives milk` and `swims`. What does the system conclude? Is this a fault in the inference engine? Explain.

**Q11** *(LO3 · Recall · Topic 2 §4.4)* Why is the ability to answer "why?" useful in an expert system such as MYCIN?

### Topic 3: Symbolic AI vs machine learning

Questions Q13–Q14 use the training data from Topic 3, §3.1:

| Email | A | B | C | D | E | F | G | H | I | J |
|---|---|---|---|---|---|---|---|---|---|---|
| Links | 0 | 1 | 1 | 2 | 3 | 2 | 4 | 5 | 6 | 8 |
| Label | not | not | not | not | not | spam | spam | spam | spam | spam |

**Q12** *(LO5 · Recall · Topic 3 §1)* In machine learning, what is **labelled data**?

**Q13** *(LO5 · Apply · Topic 3 §3.3)* How many training mistakes does the rule `IF links >= 5 THEN spam` make? Which emails are wrong?

**Q14** *(LO5 · Analyse · Topic 3 §6 Activity D)* A team reports: "Our model is 90% accurate" after measuring it on the same 10 emails used to choose k. Why is this claim weak, and what should they do instead?

**Q15** *(LO5 · Analyse · Topic 3 §4)* A bank must explain to every customer exactly why a loan application was refused, using its published criteria. Symbolic AI, machine learning, or both? Justify.

**Q16** *(LO5 · Analyse · Topic 3 §4)* Give **one** advantage and **one** disadvantage of machine learning compared with symbolic AI.

### Topic 4: History and AI winters

**Q17** *(LO6 · Recall · Topic 4 §2)* Put in order: XCON enters use · Lighthill report · Dartmouth workshop · LISP-machine market collapses.

**Q18** *(LO6 · Apply · Topic 4 §3)* Using a 3-digit lock (digits 0–9) and then a 6-digit lock, explain the **combinatorial explosion** in one or two sentences with numbers.

**Q19** *(LO6 · Analyse · Topic 4 §4)* Explain how the "rule conflict" problem you saw in Topic 2 (Part F) helps explain the end of the expert-system boom.

**Q20** *(LO6 · Analyse · Topic 4 §5)* True or false, with a reason: "During the AI winters, all AI research and all expert systems stopped."

### Topic 5: Symbolic AI in modern software

Questions Q21–Q22 use the guard rules from Topic 5, §1.3:

| Rule | IF current state is… | AND… | THEN new state |
|---|---|---|---|
| G1 | Wander | player is seen | Attack |
| G2 | Attack | health is low | Flee |
| G3 | Attack | no player is present | Wander |
| G4 | Flee | no player is present | Wander |

**Q21** *(LO7 · Apply · Topic 5 §2)* The guard is in **Attack**. The player stays visible and the guard's health stays full for three moments. What state is the guard in after each moment? Why?

**Q22** *(LO7 · Analyse · Topic 5 §2)* A designer wants the guard to attack again if it is fleeing and its health has recovered. Write the missing transition rule.

**Q23** *(LO7 · Analyse · Topic 5 §6 Activity B)* A cinema uses this table: *Child: age under 12 → €5; Adult: age over 12 and under 65 → €10; Senior: age 65 or over → €7.* Which age is not covered? Correct the table.

**Q24** *(LO7 · Apply · Topic 5 §3)* Facts: `Bishkek --located in--> Kyrgyzstan`, `Kyrgyzstan --located in--> Central Asia`. Using rule L1, what new fact can be derived? Show the step.

**Q25** *(LO7 · Analyse · Topic 5 §4)* In AlphaGeometry, which part does the step-by-step proving, and which part suggests new constructions? Which of these parts comes from symbolic AI?

---

## Part 2: Answers and explanations

| Q | Answer | Explanation / where taught |
|---|---|---|
| 1 | **c** | An operating system is instructions; the others are physical hardware (Topic 1 §2.1). |
| 2 | **b** | Algorithms are finite, clear, step-by-step procedures; the language and device do not matter (Topic 1 §2.2). |
| 3 | `raining OR snowing` = **True**; `NOT snowing` = **False** | OR needs at least one true part; NOT flips the value (Topic 1 §2.3). |
| 4 | T = 4 → OFF; T = 5 → **OFF**; T = 6 → ON | `5 > 5` is false: "greater than" is strict, the same trap as 18 °C (Topic 1 §6 Task B). |
| 5 | A person with **no card** but no overdue books can borrow (OR is true). Correct rule: `can_borrow = (has_card) AND (no_overdue_books)` | Same error as the OR login rule (Topic 1 §6 Task D). Any row where exactly one part is true shows the fault. |
| 6 | **b** | Working memory holds this case's facts; the knowledge base (rules) stays the same (Topic 2 §3). |
| 7 | Cycle 1: **R1** → is a bird. Cycle 2: **R4** (is a bird AND can fly AND hunts at night) → is an owl. Cycle 3: no new fact → **stop** | Checked with `examples/topic02_mini_rule_engine.py`. |
| 8 | R6 cannot fire in cycle 1 because `is a mammal` is not yet known. Correct: cycle 1 **R2** → is a mammal; cycle 2 **R6** → is a zebra; cycle 3 stop. | New facts become available only in the next cycle (Topic 2 §6 Part E). |
| 9 | Only R4 concludes *owl*, so it needs `is a bird` (proved by R1 from `has feathers` ✔), `can fly`, `hunts at night`. It asks: **"Can it fly?"** and **"Does it hunt at night?"** | Backward chaining asks only about facts needed for the goal (Topic 2 §4.5). |
| 10 | Only **"is a mammal"** (R2). No rule uses `swims` with `is a mammal`. Not an engine fault: a **gap in the knowledge base**. | The system knows only what its rules cover (brittleness, Topic 2 §6 Part D). |
| 11 | It shows the rules that led to the conclusion, so a doctor can **check each step** and decide whether to trust it. | Topic 2 §4.4 and §8. |
| 12 | Examples that each come with their **correct answer** (label), e.g. emails marked spam / not spam. | Topic 3 §1. |
| 13 | **2 mistakes**: F (2 links, spam → predicted not) and G (4 links, spam → predicted not). | All others match. Checked with `examples/topic03_learn_a_rule.py` (k = 5 row). |
| 14 | The model was fitted to those same emails, so accuracy on them **overstates** future accuracy; 10 examples are also too few. Test on **new labelled emails not used in training**. | Topic 3 §7 Activity D. |
| 15 | **Symbolic AI** (possibly with ML used only for other tasks). The criteria are published rules and every refusal must be explained; rules can list exactly which criterion failed. | Topic 3 §4: "answers must be justified". |
| 16 | *Advantage (any one):* learns patterns too complex to write by hand; can be retrained when data changes. *Disadvantage (any one):* needs lots of good labelled data; hard to explain at real-world scale; can be confidently wrong. | Topic 3 §4. |
| 17 | Dartmouth (1956) → Lighthill (1973) → XCON (1980) → LISP-machine collapse (1987) | Topic 4 §2, Figure 4.1. |
| 18 | 3 digits: 10 × 10 × 10 = **1,000** combinations; 6 digits: **1,000,000**. Adding 3 digits multiplied the work by 1,000. This rapid growth is the combinatorial explosion. | Topic 4 §3. |
| 19 | As rule bases grew to thousands of rules, every new rule could clash with old ones (like R5 and R6 both firing). Finding and fixing conflicts made large systems expensive to maintain, one reason companies lost faith in expert systems in the late 1980s. | Topic 4 §4 links Topic 2 Part F to the second winter. |
| 20 | **False.** Funding and interest fell sharply, but research continued at a smaller scale and some systems (e.g. XCON) stayed in use. | Topic 4 §5. |
| 21 | **Attack, Attack, Attack.** G2 needs low health and G3 needs no player present; neither is true, so no rule fires and the guard stays in its current state. | Topic 5 §1.3: "If no rule matches, the character stays in its current state." |
| 22 | `G5: IF current state is Flee AND health is not low AND player is seen THEN Attack` (accept equivalent wording that names the current state, the health condition and the new state). | Topic 5 §2, moment 4 shows the missing behaviour. |
| 23 | Age **12** is not covered (not "under 12", not "over 12"). Fix: Adult = **12 or over** and under 65 (or Child = 12 or under). | Gap at a boundary, as in Topic 5 Activity B and Topic 1 Task B. |
| 24 | Bishkek → Kyrgyzstan and Kyrgyzstan → Central Asia, so by L1: **Bishkek is located in Central Asia**. | Topic 5 §3 worked example. |
| 25 | The **symbolic deduction engine** does the proving (this part is symbolic AI); the **language model** suggests constructions (this part is learned from data). | Topic 5 §4. |

---

## Coverage check

| Learning outcome | Questions | Types included |
|---|---|---|
| LO1 Software, algorithms, conditions | Q1, Q2 | Recall |
| LO2 IF–THEN rules and truth tables | Q3, Q4, Q5 | Apply, Analyse |
| LO3 Parts of a rule-based system | Q6, Q10, Q11 | Recall, Analyse |
| LO4 Tracing forward/backward chaining | Q7, Q8, Q9 | Apply, Analyse |
| LO5 Symbolic AI vs ML | Q12–Q16 | Recall, Apply, Analyse |
| LO6 History and AI winters | Q17–Q20 | Recall, Apply, Analyse |
| LO7 Modern uses | Q21–Q25 | Apply, Analyse |

**Totals:** 25 questions: 6 recall, 8 apply, 11 analyse.
