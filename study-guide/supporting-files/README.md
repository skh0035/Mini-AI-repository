# The SilkMind Caravan: supporting files and setup

Companion files for **The SilkMind Caravan Study Guide V1.0** (Team SilkMind, Software & Symbolic AI).
Everything here is optional: every result these files produce is also printed in the guide.

| File | Used in | What it is | How to run |
|---|---|---|---|
| `lab-files/lab2_animal_expert.pl` | Stop 2, Lab 2A | BEK's six animal rules (R1–R6) in Prolog | Open <https://swish.swi-prolog.org> → **Program** → paste the file → type a query (e.g. `is_a(pingu, What).`) → **Run!** |
| `lab-files/lab5_silk_road_graph.pl` | Stop 5, Lab 5 | Tiny Silk Road knowledge graph + rule L1 | Same as above; query e.g. `inside(registan, Where).` |
| `lab-files/finale_tea_expert_example.pl` | Grand Caravan Challenge | Example solution (look only after trying!) | Same as above; query `recommend(timur, Tea).` |
| `examples/topic02_mini_rule_engine.py` | Stop 2 (fallback for Lab 2A) | Forward chaining + "why?" explanations in Python | `python3 topic02_mini_rule_engine.py` |
| `examples/topic03_learn_a_rule.py` | Stop 3, Mission 3.1 | Learns the threshold rule from the 10 messages | `python3 topic03_learn_a_rule.py` |
| `SilkMind_Labs.ipynb` | Stops 2–3 (fallback for Lab 3) | Notebook: Part 1 rule engine, Part 2 threshold learning, Part 3 word-counting scam detector | Google Colab: *File → Upload notebook* (works on your own copy), or Jupyter. Run cells with Shift+Enter. |

## Requirements

- **SWISH labs:** any modern browser; no account or installation. If SWISH says *"Too many open queries"*, press **Stop** on earlier queries.
- **Python files and notebook:** Python 3.8 or newer; **no extra packages**.
- **ELIZA lab:** a browser; <https://www.masswerk.at/elizabot/eliza.html> → click *open ELIZA terminal*.
- **Machine Learning for Kids lab:** a browser; <https://machinelearningforkids.co.uk> → *Get started* → *Try it now* (no account; tick the "Verify you are human" box). "Try it now" projects are temporary.

## Tested

SWISH labs, ELIZA and all Python/notebook code were run on 3 November 2026; outputs match the guide (see the guide's Appendix B).
The Machine Learning for Kids training steps must still be tried by a team member; record the result in Appendix B.
