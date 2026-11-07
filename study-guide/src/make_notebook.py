"""Creates SilkMind_Labs.ipynb (plain JSON, no extra packages) and test-runs every code cell."""
import json, pathlib

cells = []
md = lambda s: cells.append({"cell_type": "markdown", "metadata": {}, "source": s.strip("\n").splitlines(True)})
code = lambda s: cells.append({"cell_type": "code", "metadata": {}, "execution_count": None, "outputs": [], "source": s.strip("\n").splitlines(True)})

md("""
# 🐪 The SilkMind Caravan: Lab Notebook
**Team SilkMind · Study Guide V1.0 companion · Python 3, no extra packages**

This notebook lets you *run* the ideas from the guide and change them. It is also the **offline fallback** for Labs 2A and 3.

**How to open it:** in Google Colab choose *File → Upload notebook* and pick this file (Colab makes your own copy), or open it in Jupyter.
Run each grey code cell with **Shift + Enter**, from top to bottom. Each part says what you should see and what to change.

| Part | Guide stop | What you do |
|---|---|---|
| 1 | Stop 2 (Mission 2.1, Lab 2A) | Run BEK's forward-chaining engine, change facts, add a rule |
| 2 | Stop 3 (Mission 3.1) | Watch To'ti learn a threshold rule from data, then retrain |
| 3 | Stop 3 (Lab 3 fallback) | Train a tiny word-counting scam detector and find out what it *really* learned |
""")

md("""
## Part 1 · BEK's inference engine (forward chaining)
The rules are the same R1–R6 as in the guide. Each rule is `(name, [conditions joined by AND], conclusion)`.
""")
code('''
RULES = [
    ("R1", ["has feathers"], "is a bird"),
    ("R2", ["gives milk"], "is a mammal"),
    ("R3", ["is a bird", "cannot fly", "swims"], "is a penguin"),
    ("R4", ["is a bird", "can fly", "hunts at night"], "is an owl"),
    ("R5", ["is a mammal", "eats meat", "has black stripes"], "is a tiger"),
    ("R6", ["is a mammal", "has hooves", "has black stripes"], "is a zebra"),
]

def forward_chain(starting_facts, rules=RULES):
    facts = set(starting_facts)                      # working memory
    cycle = 0
    while True:                                      # the inference engine
        cycle += 1
        fired = None
        for name, conditions, conclusion in rules:   # check rules in order
            if all(c in facts for c in conditions) and conclusion not in facts:
                fired = (name, conditions, conclusion)
                break
        if fired is None:
            print(f"Cycle {cycle}: no rule adds a new fact -> STOP")
            return facts
        name, conditions, conclusion = fired
        facts.add(conclusion)
        print(f"Cycle {cycle}: {name} fires because {' AND '.join(conditions)} -> add '{conclusion}'")

forward_chain(["has feathers", "cannot fly", "swims"])
''')
md("""
**You should see:** cycle 1 R1 → *is a bird*; cycle 2 R3 → *is a penguin*; cycle 3 STOP (same as Mission 2.1, round 1).

**Your turn**
1. Change the starting facts to `["gives milk", "has hooves", "has black stripes"]` and predict the trace before you run it.
2. Try the *mystery animal*: `["gives milk", "eats meat", "has hooves", "has black stripes"]`. What goes wrong, and is it the engine's fault?
3. Add a rule R7 for a giraffe to `RULES` (use `"has long neck"`), then test it. Did your new rule create any conflicts?
""")
code('''
# 1-3: edit and run
forward_chain(["gives milk", "eats meat", "has hooves", "has black stripes"])
''')

md("""
## Part 2 · To'ti learns a rule from labelled data
The model may only be: **IF links ≥ k THEN scam**. Training = try every k and keep the one with the fewest mistakes.
""")
code('''
TRAINING = [("A", 0, "not"), ("B", 1, "not"), ("C", 1, "not"), ("D", 2, "not"), ("E", 3, "not"),
            ("F", 2, "scam"), ("G", 4, "scam"), ("H", 5, "scam"), ("I", 6, "scam"), ("J", 8, "scam")]

def predict(links, k):
    return "scam" if links >= k else "not"

def mistakes(k, data):
    return [name for name, links, label in data if predict(links, k) != label]

def train(data):
    for k in range(10):
        wrong = mistakes(k, data)
        print(f"k = {k}: {len(wrong)} mistake(s) {wrong}")
    best = min(range(10), key=lambda k: (len(mistakes(k, data)), k))   # fewest mistakes, smallest k on a tie
    print(f"\\nLearned model: IF links >= {best} THEN scam")
    return best

k = train(TRAINING)
for name, links in [("K", 7), ("L", 0), ("M", 3)]:
    print(name, links, "links ->", predict(links, k))
''')
md("""
**You should see:** mistakes 5, 4, 2, 2, **1**, 2, 3, 4, 4, 5 → learned model `links >= 4` (only F is wrong). K → scam, L → not, M → not.

**Your turn**
1. Add the new labelled message `("N", 3, "scam")` to `TRAINING` and run again. Which values of k tie now? What did the program choose, and why?
2. Add three messages of your own that make k = 6 the best rule. What kind of data did you need?
3. Reflect: the model makes 1 mistake on its training data. Why is that *not* a good estimate of how it will do on tomorrow's messages?
""")
code('''
# 1-2: edit TRAINING and run
TRAINING_2 = TRAINING + [("N", 3, "scam")]
train(TRAINING_2)
''')

md("""
## Part 3 · A tiny word-counting scam detector (offline version of Lab 3)
This is **not** how Machine Learning for Kids works inside; it is a much simpler learner we wrote so you can see every number.
It counts how often each word appears in *genuine* and *scam* training messages. A new message scores **+1 for each scam count and −1 for each genuine count** of its words:
score > 0 → scam, score < 0 → genuine, 0 → unsure.
""")
code('''
import re

GENUINE = ["Your order of twenty silk scarves will arrive on Tuesday", "Can we meet at the bazaar at noon to agree the price",
           "The camel caravan is delayed by one day because of a sandstorm", "Thank you for your payment, here is your receipt",
           "Please bring the spice samples to my shop tomorrow", "We have new carpets from Bukhara, visit us this week",
           "Your room at the caravanserai is booked for three nights", "The market closes early on Friday for the festival"]
SCAM = ["Congratulations you have won a free camel, click this link now", "URGENT your account is locked, send your password today",
        "You are selected for a secret gold prize, pay a small fee to claim", "Cheap silk 90 percent off only today, send money first",
        "Final warning: your parcel is held, pay the release fee now", "Click here to claim free gold coins, limited time",
        "Your bank details are needed to receive your inheritance", "Win win win, act now, free prize waiting"]
TESTS = ["Free tea tasting at our shop on Friday", "Your parcel from Samarkand will arrive tomorrow",
         "Send your password to unlock your prize", "Please confirm the meeting time for the silk delivery",
         "CONGRATULATIONS", "The weather in Kashgar is sunny"]

def words(text):
    return re.findall(r"[a-z0-9]+", text.lower())

def learn(genuine, scam):
    counts = {}
    for label, messages in (("genuine", genuine), ("scam", scam)):
        for m in messages:
            for w in words(m):
                counts.setdefault(w, {"genuine": 0, "scam": 0})[label] += 1
    return counts

def classify(counts, text):
    score = sum(counts.get(w, {"genuine": 0, "scam": 0})["scam"] - counts.get(w, {"genuine": 0, "scam": 0})["genuine"]
                for w in words(text))
    return ("scam" if score > 0 else "genuine" if score < 0 else "unsure"), score

model = learn(GENUINE, SCAM)
for t in TESTS:
    print(classify(model, t), t)
''')
md("""
**You should see:** T1 genuine (−4), T2 genuine (−2), T3 scam (+8), T4 genuine (−14), T5 scam (+1), T6 genuine (−7).

**Investigate what it *really* learned**
1. Run the next cell. Why is *"The weather in Kashgar is sunny"* (T6) called genuine, even though it has nothing to do with trade?
2. Classify `"Weather sunny"` and `"Click the free link"`. Explain both scores.
3. The model has learned that the word *"the"* suggests a genuine message. Is that a sensible thing to learn? What does it tell you about **training data**?
4. Compare with BEK: could you have written rules for this? Which approach is easier to explain?
""")
code('''
for w in ["the", "is", "free", "prize", "your", "sunny"]:
    print(w, model.get(w, "never seen"))
print(classify(model, "Weather sunny"))
print(classify(model, "Click the free link"))
''')
md("""
**Feedback:** `the` appears 7 times in genuine messages and once in scams, so every "the" pushes a message towards *genuine*. T6 is "genuine" only because of *the* and *is*: the model has no idea what weather is, and it **cannot answer "neither"**.
`"Weather sunny"` scores 0 (never-seen words) → unsure. `"Click the free link"`: click +2, the −6, free +3, link +1 → 0 → unsure.
Learning "the = genuine" is an accident of our small, unbalanced data set: a model learns whatever patterns are in the data, sensible or not. More and better-balanced examples help;
an explicit rule (BEK) would be easier to explain but would need constant hand-editing as scammers change words.
""")

nb = {"cells": cells, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
                                   "language_info": {"name": "python"}}, "nbformat": 4, "nbformat_minor": 5}
out = pathlib.Path("../supporting-files/SilkMind_Labs.ipynb")
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding="utf-8")

# test-run every code cell in one namespace
ns = {}
for c in cells:
    if c["cell_type"] == "code":
        print("----- running cell")
        exec("".join(c["source"]), ns)
print("\nNotebook written:", out)
