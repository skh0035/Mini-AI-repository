"""
Topic 3 demo: the smallest possible example of "learning a rule from data".

Optional for learners: you do NOT need to read Python for Topic 3.
This program does exactly what the table in
content/03-symbolic-ai-vs-machine-learning.md, Section 3, does by hand.

The "model" is one rule of the form:
    IF number_of_links >= k THEN spam ELSE not spam
Training = trying every k and keeping the one with the fewest mistakes
on the labelled examples.

Run it with:   python3 topic03_learn_a_rule.py
Requires Python 3.8+ and no extra packages.
"""

# Labelled training data: (email, number of links, correct label)
TRAINING = [
    ("A", 0, "not spam"),
    ("B", 1, "not spam"),
    ("C", 1, "not spam"),
    ("D", 2, "not spam"),
    ("E", 3, "not spam"),
    ("F", 2, "spam"),
    ("G", 4, "spam"),
    ("H", 5, "spam"),
    ("I", 6, "spam"),
    ("J", 8, "spam"),
]

# New emails the model has never seen
NEW_EMAILS = [("K", 7), ("L", 0), ("M", 3)]


def predict(links, k):
    return "spam" if links >= k else "not spam"


def count_mistakes(k):
    return sum(1 for _, links, label in TRAINING if predict(links, k) != label)


def train():
    print("k  | mistakes on the 10 training emails")
    print("---+-----------------------------------")
    results = {}
    for k in range(0, 10):
        results[k] = count_mistakes(k)
        print(f"{k:<2} | {results[k]}")
    best_mistakes = min(results.values())
    best_k = min(k for k, m in results.items() if m == best_mistakes)  # smallest k on a tie
    print(f"\nLearned rule: IF links >= {best_k} THEN spam   "
          f"({best_mistakes} mistake(s) out of {len(TRAINING)})")
    return best_k


if __name__ == "__main__":
    k = train()
    print("\nPredictions for new emails:")
    for name, links in NEW_EMAILS:
        print(f"  {name}: {links} links -> {predict(links, k)}")
