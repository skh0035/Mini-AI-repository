# Topic 4: History: The Rise, the AI Winters and the Lessons

**Level:** Beginner  |  **Estimated time:** 25 minutes  |  **Status:** Drafted (awaiting team review)
**Builds on:** [Topic 2](02-rules-and-inference.md) and [Topic 3](03-symbolic-ai-vs-machine-learning.md)  |  **Comes before:** [Topic 5: Symbolic AI in Modern Software](05-symbolic-ai-in-modern-software.md)

**Learning objectives.** After this topic you will be able to:

1. Place the main events in the history of symbolic AI on a timeline.
2. Explain what an "AI winter" is and give two causes of each of the two main winters.
3. Connect the second AI winter to the limits of rule-based systems you saw in Topic 2.

---

## 1. Key term

> **AI winter:** a period in which funding and interest in AI research fall sharply, usually after expectations were set too high and results did not match them ([Wikipedia: AI winter](https://en.wikipedia.org/wiki/AI_winter)).

The history of symbolic AI is a cycle that repeats twice: **big promises → funding → disappointment → winter**.

---

## 2. Timeline

| Year(s) | Event | Phase |
|---|---|---|
| 1956 | Dartmouth summer workshop. John McCarthy, Marvin Minsky, Nathaniel Rochester and Claude Shannon organise an eight-week meeting; the term "artificial intelligence" comes from this project ([Dartmouth Alumni Magazine](https://dartmouthalumnimagazine.com/articles/birth-artificial-intelligence)). | Optimism |
| 1965 | Work begins on DENDRAL, often called the first expert system ([Britannica](https://www.britannica.com/technology/artificial-intelligence/Expert-systems)). | Optimism |
| 1973 | The **Lighthill report**, a review for the UK government, criticises AI for failing to meet its grand goals; UK AI research funding is largely dismantled. | First winter begins |
| 1974 | In the USA, DARPA cancels a major speech-recognition grant (about $3 million a year) as it moves towards mission-focused research. | First winter |
| ≈1974–1980 | **First AI winter.** | Winter |
| 1980 | XCON enters use at Digital Equipment Corporation (Topic 2, §7). Companies start building expert systems. | Boom |
| 1981–1991 | Japan's **Fifth Generation Computer** project (about $850 million) aims at computers that converse, translate and reason like people. By 1991 these goals are not met. | Boom → disappointment |
| 1987 | The market for specialised **LISP machines** (computers built to run AI software) collapses within about a year, because cheaper general-purpose computers become as powerful. | Second winter begins |
| ≈1987–1993 | **Second AI winter.** Expert systems prove expensive to maintain and brittle; US Strategic Computing funding for new AI is cut (1988). | Winter |

*Sources for 1973–1993 entries: [Wikipedia: AI winter](https://en.wikipedia.org/wiki/AI_winter). Historians give slightly different start and end years; the ranges here are the commonly cited ones.*

---

## 3. What went wrong?

### First winter (≈1974–1980): promises ahead of computers

Early researchers believed general human-like intelligence was close. But the computers of the time were slow and had little memory, and problems such as understanding language turned out to be far harder than expected. When reviews like the Lighthill report compared the promises with the results, governments cut funding.

### Second winter (≈1987–1993): the limits of rules

This is the part that connects directly to Topic 2. The expert-system boom of the 1980s ran into exactly the limits you met in the animal identifier:

| Limit seen in Topic 2 | What happened in industry |
|---|---|
| The system knows only what its rules cover (Activity Part D) | Systems failed on unusual cases; they were described as **brittle** |
| New rules can conflict with old ones (Activity Part B) | Large rule bases became very costly to update and maintain |
| No learning | Every change needed human experts and programmers |

At the same time, the special hardware that AI companies sold (LISP machines) was overtaken by cheaper ordinary computers, and a whole industry disappeared within about a year ([Wikipedia: AI winter](https://en.wikipedia.org/wiki/AI_winter)).

### The lesson

Rule-based AI did **not** disappear; it stopped being sold as a path to human-like intelligence and became an ordinary software technique (Topic 5). Meanwhile, research moved towards approaches that **learn from data** (Topic 3), which later benefited from much faster computers and much more data.

---

## 4. Learner activity

**Part A.** Put these events in order: Fifth Generation project starts · Dartmouth workshop · LISP machine market collapses · Lighthill report · XCON enters use.

**Part B.** For each winter, give **one** cause related to *expectations* and **one** cause related to *technology*.

**Part C.** In two sentences, explain how Activity Part D in Topic 2 (the "has feathers, can fly" case) helps explain the second AI winter.

---

## 5. Expected outcomes and answers

**Part A.** Dartmouth workshop (1956) → Lighthill report (1973) → XCON enters use (1980) → Fifth Generation project starts (1981/82) → LISP machine market collapses (1987).

**Part B.**

| | Expectations | Technology |
|---|---|---|
| First winter | Researchers promised human-like intelligence soon; reviews (Lighthill, 1973) found results far short of this | Computers were too slow, with too little memory, for hard problems like language |
| Second winter | Expert systems and the Fifth Generation project promised more than they delivered | Rule bases were brittle and expensive to maintain; LISP machines were overtaken by cheaper computers |

**Part C (model answer).** The system could only say "is a bird", because no rule covered flying birds that do not hunt at night; it failed on a case its builders had not foreseen. Real expert systems failed in the same way on a much larger scale, and the cost of writing ever more rules to fill such gaps helped end the expert-system boom.

---

## 6. References

Links accessed 31 October 2026.

1. Hertog, J. *The Birth of Artificial Intelligence.* Dartmouth Alumni Magazine. https://dartmouthalumnimagazine.com/articles/birth-artificial-intelligence
2. Encyclopaedia Britannica. *Artificial intelligence: Expert systems.* https://www.britannica.com/technology/artificial-intelligence/Expert-systems
3. Wikipedia. *AI winter.* https://en.wikipedia.org/wiki/AI_winter
4. Wikipedia. *Xcon.* https://en.wikipedia.org/wiki/Xcon

**Gaps for review:** several dates and amounts above come from Wikipedia only (Lighthill, DARPA grant, Fifth Generation budget, LISP machine collapse). Before this topic is marked **Checked**, a reviewer should confirm them in a second source, for example the Lighthill report itself or a textbook history chapter, and record this in `docs/review-log.md`.
