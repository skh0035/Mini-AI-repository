"""
Topic 2 demo: a tiny forward-chaining rule engine.

Optional for learners: you do NOT need to understand Python to follow Topic 2.
This file shows a computer doing exactly what the trace table in
content/02-rules-and-inference.md does by hand.

Run it with:   python3 topic02_mini_rule_engine.py
Requires Python 3.8+ and no extra packages.
"""

# ---------------------------------------------------------------
# 1. KNOWLEDGE BASE: the rules (IF all conditions are known facts
#    THEN add the conclusion as a new fact)
# ---------------------------------------------------------------
RULES = [
    ("R1", ["has feathers"], "is a bird"),
    ("R2", ["gives milk"], "is a mammal"),
    ("R3", ["is a bird", "cannot fly", "swims"], "is a penguin"),
    ("R4", ["is a bird", "can fly", "hunts at night"], "is an owl"),
    ("R5", ["is a mammal", "eats meat", "has black stripes"], "is a tiger"),
    ("R6", ["is a mammal", "has hooves", "has black stripes"], "is a zebra"),
]


def forward_chain(starting_facts):
    """Fire rules until no rule can add anything new. Return facts and a log."""
    facts = set(starting_facts)          # 2. WORKING MEMORY
    how = {}                             # remembers which rule produced each fact
    cycle = 0

    while True:                          # 3. INFERENCE ENGINE (the loop)
        cycle += 1
        fired = None
        for name, conditions, conclusion in RULES:      # rules are tried in order
            all_true = all(c in facts for c in conditions)
            if all_true and conclusion not in facts:    # ignore rules that add nothing new
                fired = (name, conditions, conclusion)
                break                                   # strategy: fire the first match
        if fired is None:
            print(f"Cycle {cycle}: no rule adds a new fact -> STOP")
            break
        name, conditions, conclusion = fired
        facts.add(conclusion)
        how[conclusion] = (name, conditions)
        print(f"Cycle {cycle}: {name} fires because {' AND '.join(conditions)} "
              f"-> add '{conclusion}'")
    return facts, how


def explain(fact, how, indent=""):
    """Answer 'why?' by walking back through the rules that produced a fact."""
    if fact not in how:
        print(f"{indent}- '{fact}' was given as a starting fact")
        return
    name, conditions = how[fact]
    print(f"{indent}- '{fact}' because of {name} (IF {' AND '.join(conditions)})")
    for c in conditions:
        explain(c, how, indent + "    ")


if __name__ == "__main__":
    start = ["has feathers", "cannot fly", "swims"]
    print("Starting facts:", ", ".join(start), "\n")
    final_facts, how = forward_chain(start)
    print("\nFinal facts:", ", ".join(sorted(final_facts)))
    print("\nWhy is it a penguin?")
    explain("is a penguin", how)
