"""Draws assets/topic04-ai-timeline.png. Run from the repository root:
python3 assets/diagram-sources/topic04_timeline.py   (needs matplotlib)"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots(figsize=(9.5, 6.2), dpi=170)
ax.set_xlim(1951, 1996); ax.set_ylim(-3.9, 4.1); ax.axis("off")

# periods
periods = [(1956, 1974, "Early optimism", "#e8eef7", "#1f3a5f"),
           (1974, 1980, "First AI winter", "#dde6f0", "#3a5a80"),
           (1980, 1987, "Expert-system boom", "#fff4d6", "#8a5a10"),
           (1987, 1993, "Second AI winter", "#dde6f0", "#3a5a80")]
for a, b, name, fill, txt in periods:
    ax.add_patch(Rectangle((a, -0.45), b - a, 0.9, facecolor=fill, edgecolor="#8899aa", lw=1))
    ax.text((a + b) / 2, 0, name, ha="center", va="center", fontsize=9.3, color=txt, weight="bold")
for y in range(1955, 1996, 10):
    ax.text(y, -0.75, str(y), ha="center", va="top", fontsize=9, color="#555")
    ax.plot([y, y], [-0.45, -0.6], color="#8899aa", lw=1)

events = [  # label x-position, text (starts with the real year), level (+ above / - below)
    (1957, "1956\nDartmouth workshop:\n'artificial intelligence'\nnamed", 2.9),
    (1965, "1965\nDENDRAL begins\n(first expert system)", 1.35),
    (1972, "1972\nMYCIN begins", 3.1),
    (1967.5, "1973\nLighthill report (UK)", -1.45),
    (1977.5, "1974\nDARPA cuts speech-\nrecognition grant", -2.95),
    (1980, "1980\nXCON in use\nat DEC", 1.45),
    (1984, "1982–1992\nJapan's Fifth\nGeneration project", 3.05),
    (1986, "1987\nLISP-machine\nmarket collapses", -1.55),
    (1991, "1988\nUS Strategic Computing\ncuts new AI funding", -3.05),
]
for x, label, lvl in events:
    year = int(label[:4])                     # the dot always sits on the real year
    edge = 0.45 if lvl > 0 else -0.45
    ax.plot([year, x], [edge, lvl], color="#666", lw=1, zorder=1)
    ax.plot(year, edge, "o", color="#b03a2e", ms=5, zorder=3)
    ax.text(x, lvl, label, ha="center", va="center", fontsize=10, zorder=2,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#b8c2cf"))
ax.set_title("Figure 4.1  Symbolic AI, 1956–1993: two cycles of promise and disappointment",
             fontsize=13, color="#1f3a5f", weight="bold", loc="left")
fig.text(0.01, 0.01, "Start and end years of the AI winters are approximate; historians give slightly different ranges.",
         fontsize=8.5, color="#555")
plt.tight_layout()
plt.savefig("assets/topic04-ai-timeline.png", facecolor="white")
