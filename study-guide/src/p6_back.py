from kit import *
import re

FINALE = stop_head("★", "The caravanserai", "The Grand Caravan Challenge",
    "Can you build your own small expert system, and find its weak spots before anyone else does?",
    "Uses everything from Stops 1–5 · ≈ 40 min · Lab in SWISH or on paper", "nodira") + f"""
{say("nodira", "Your turn to be the scholar of Bukhara. Build a tiny expert system about something <b>you</b> know well.")}
{mission("★", "Build, test and break your own expert system", "40 min",
 "Bring together rules (Stop 1), chaining and explanation (Stop 2), the rules-vs-learning choice (Stop 3) and gaps and conflicts (Stops 2 and 4).",
 "SWISH (or paper). Lab 2A finished. Example solution: <code>supporting-files/lab-files/finale_tea_expert_example.pl</code>. Look at it only <i>after</i> trying!",
 """<ol><li>Choose a small topic you know: which tea to serve, which bus to take, which plant needs water, which game character to pick…</li>
<li>Write <b>at least 5 rules</b> (at least two with AND) and facts for <b>at least 4 test cases</b>.</li>
<li>Include on purpose: one case your rules <b>cannot</b> answer (a gap) and one case where <b>two rules</b> fire.</li>
<li>Run every case in SWISH (or trace on paper) and write the "because…" explanation for one answer.</li></ol>""",
 "Table: <i>test case · expected answer · actual answer · rules fired</i>.",
 """<ul><li>What did your gap case show about expert systems?</li>
<li>If you had 10,000 examples of real decisions instead of an expert, would you rather <b>write rules</b> or <b>train a model</b>? Why?</li>
<li>Which of your rules would be hardest to keep up to date?</li></ul>""",
 """<p><b>Checklist for a strong answer:</b> ☐ ≥ 5 rules, ≥ 2 using AND ☐ ≥ 4 test cases with expected answers written <i>before</i> running ☐ a gap case and a two-rule case
☐ one full explanation chain ☐ a reasoned answer to the rules-or-model question.</p>
<p><b>Example result</b> (our tea system, tested in SWISH on 3 Nov 2026): <code>findall(P-T, recommend(P,T), L)</code> gave
<code>[aziz-hot_black_tea, lola-mint_tea, timur-ginger_honey_tea, timur-ginger_honey_tea]</code>. Timur appears <b>twice</b> because rules T4 and T5 both fire;
Guli is missing because no rule works without a temperature (a gap).</p>""")}
"""

GLOSS_SRC = open("../../content/glossary.md").read()
rows = re.findall(r"^\| \*\*(.+?)\*\* \| (.+?) \| (.+?) \|$", GLOSS_SRC, re.M)
EXTRA = [("Finite state machine", "A rule-based design where a character is always in one state and transition rules move it between states.", "5"),
         ("Prolog", "A programming language for logic: you write facts and rules, then ask queries; it answers by backward chaining.", "2 (Lab 2A)"),
         ("Query (Prolog)", "A question to a Prolog program, e.g. <code>is_a(pingu, What).</code>", "2 (Lab 2A)"),
         ("Variable (Prolog)", "A word starting with a capital letter (<code>X</code>, <code>What</code>) that stands for \"something\" Prolog must find.", "2 (Lab 2A)"),
         ("ELIZA", "A 1966 chatbot by Joseph Weizenbaum that replies using keyword pattern rules; it does not understand language.", "2 (Lab 2B)")]
allrows = sorted([(a, b, c.replace("1, 2", "1–2")) for a, b, c in rows] + EXTRA, key=lambda r: r[0].lower())
GLOSSARY = "<h1 class='page-break' id='glossary'>Glossary</h1><p class='small'>One definition per term, the same in this guide, the Markdown content, the slides, the videos and the test bank. \"Stop\" = where the term is introduced.</p><table><tr><th style='width:34mm'>Term</th><th>Meaning</th><th style='width:16mm'>Stop</th></tr>" + \
    "".join(f"<tr><td><b>{a}</b></td><td>{b.replace('`', '')}</td><td>{c}</td></tr>" for a, b, c in allrows) + "</table>"

RULE_CARDS = "".join(f'<div class="card rule"><div class="ct">{r}</div>IF {i}<br><b>THEN {t}</b></div>' for r, i, t in [
    ("R1", "has feathers", "is a bird"), ("R2", "gives milk", "is a mammal"), ("R3", "is a bird AND cannot fly AND swims", "is a penguin"),
    ("R4", "is a bird AND can fly AND hunts at night", "is an owl"), ("R5", "is a mammal AND eats meat AND has black stripes", "is a tiger"),
    ("R6", "is a mammal AND has hooves AND has black stripes", "is a zebra")])
FACT_CARDS = "".join(f'<div class="card fact" style="min-height:14mm"><div class="ct">{f}</div></div>' for f in [
    "has feathers", "cannot fly", "swims", "can fly", "hunts at night", "gives milk", "eats meat", "has hooves", "has black stripes",
    "is a bird", "is a mammal", "is a penguin", "is an owl", "is a tiger", "is a zebra"])
MSG = [("A", 0, "not"), ("B", 1, "not"), ("C", 1, "not"), ("D", 2, "not"), ("E", 3, "not"), ("F", 2, "scam"), ("G", 4, "scam"),
       ("H", 5, "scam"), ("I", 6, "scam"), ("J", 8, "scam"), ("N", 3, "scam")]
MSG_CARDS = "".join(f'<div class="card {"event" if l == "scam" else "fact"}" style="min-height:16mm"><div class="ct">Message {m}</div>🔗 {k} link{"s" if k != 1 else ""}<br>label: <b>{l}</b>{" <i>(new, for retraining)</i>" if m == "N" else ""}</div>' for m, k, l in MSG)
EVENTS = ["Dartmouth summer workshop: the term \"artificial intelligence\" is used for the project", "DENDRAL, often called the first expert system, begins at Stanford",
          "MYCIN begins: diagnosing blood infections with about 500 rules", "The Lighthill report criticises AI for the UK Science Research Council",
          "DARPA cancels a large speech-recognition grant", "XCON goes into everyday use at Digital Equipment Corporation",
          "Japan's Fifth Generation Computer Systems project starts", "The LISP-machine market collapses within about a year",
          "US Strategic Computing stops new spending on AI"]
EVENT_CARDS = "".join(f'<div class="card event" style="min-height:22mm"><div class="ct">Event {i+1}</div>{e}<br><span class="small">Year: ______</span></div>' for i, e in enumerate(EVENTS))

APPENDIX_A = f"""
<h1 class="page-break" id="cards">Appendix A · Printable cards</h1>
<p class="small">Print this page and the next on card, cut along the dashed lines. Rule cards are green, fact cards blue, scam/event cards amber.</p>
<h3>A1 · Rule cards (Mission 2.1)</h3><div class="cards">{RULE_CARDS}</div>
<h3>A2 · Fact cards (Mission 2.1): conclusions in the bottom row are added by the "engine"</h3><div class="cards">{FACT_CARDS}</div>
<h3 class="page-break">A3 · Message cards (Mission 3.1)</h3><div class="cards">{MSG_CARDS}</div>
<h3>A4 · Event cards (Mission 4.1): years are in the Feedback Corner of Stop 4. Shuffle before playing!</h3><div class="cards">{EVENT_CARDS}</div>
"""

TESTING = """
<h1 class="page-break" id="testing">Appendix B · How we tested this guide</h1>
<p>The brief asks us to test every activity ourselves and to say which version we used. This is our record for <b>V1.0</b>. Team members add their own learner tests below
before submission and in later versions.</p>
<table><tr><th>Activity</th><th>Platform / version</th><th>Date</th><th>What we checked</th><th>Result</th></tr>
<tr><td>Lab 2A</td><td>SWISH, swish.swi-prolog.org (SWI-Prolog web version live on the test date)</td><td>3 Nov 2026</td><td>All five queries, giraffe extension, typo, capital-letter variable, "Too many open queries" message</td><td>✔ Outputs as printed. Found and fixed: without <code>:- discontiguous</code>, adding facts at the end of the file gave confusing warnings; directive added to the starter file.</td></tr>
<tr><td>Lab 5</td><td>SWISH (same)</td><td>3 Nov 2026</td><td>Queries 1–3, Bukhara extension, broken rule</td><td>✔ Broken rule gives "Stack limit (0.2Gb) exceeded … Probable infinite recursion".</td></tr>
<tr><td>Grand Challenge example</td><td>SWISH (same)</td><td>3 Nov 2026</td><td><code>findall</code> over all travellers</td><td>✔ As printed in the challenge.</td></tr>
<tr><td>Lab 2B</td><td>elizabot.js by N. Landsteiner (2005), masswerk.at</td><td>3 Nov 2026</td><td>7 test inputs</td><td>✔ Transcript as printed. Opening line varied between page loads, so replies can vary.</td></tr>
<tr><td>Lab 3</td><td>Machine Learning for Kids, "Try it now"</td><td>3 Nov 2026</td><td>Access route</td><td>⚠ Our automated test stopped at the Cloudflare "Verify you are human" box (a person must tick it). <b>Training steps still to be tested by a team member</b>; record below.</td></tr>
<tr><td>Missions 2.1, 3.1, Test Bank traces</td><td><code>supporting-files/examples/*.py</code>, Python 3</td><td>3 Nov 2026</td><td>Every trace and mistakes table</td><td>✔ Program output matches every answer.</td></tr>
<tr><td>Video links</td><td>YouTube IDs checked against video listings</td><td>3 Nov 2026</td><td>Title, creator, length, chapter times (Crash Course AI #10, CGP Grey)</td><td>✔ Team members must watch each recommended part before submission (record below).</td></tr></table>
<h3>Learner tests and member checks (to be completed by Team SilkMind)</h3>
<table><tr><th>Section tried</th><th>Tester (did not write it)</th><th>Date</th><th>Could they complete it? What confused them?</th><th>What we changed</th></tr>
<tr><td>Lab 3 (Machine Learning for Kids), full run</td><td></td><td></td><td></td><td></td></tr>
<tr><td>Mission 2.1 (Rule Cards)</td><td></td><td></td><td></td><td></td></tr>
<tr><td>Mission 3.1 (Teach To'ti)</td><td></td><td></td><td></td><td></td></tr>
<tr><td>Videos: watched recommended parts</td><td></td><td></td><td></td><td></td></tr></table>
"""

REFS = """
<h1 class="page-break" id="refs">Resources, references and acknowledgements</h1>
<h3>Learning platforms used in labs</h3>
<ul><li>SWISH: SWI-Prolog for SHaring. https://swish.swi-prolog.org (Lab 2A, Lab 5, Grand Challenge)</li>
<li>Landsteiner, N. (2005). ELIZA (elizabot.js), after Weizenbaum's DOCTOR script. https://www.masswerk.at/elizabot/eliza.html (Lab 2B)</li>
<li>Lane, D. Machine Learning for Kids. https://machinelearningforkids.co.uk (Lab 3)</li></ul>
<h3>Videos and pages recommended</h3>
<ul><li>Josh Darnit. <i>Exact Instructions Challenge – THIS is why my kids hate me.</i> YouTube. https://www.youtube.com/watch?v=cDA3_5982h8</li>
<li>CrashCourse &amp; PBS Digital Studios (2019). <i>Symbolic AI: Crash Course AI #10.</i> https://www.youtube.com/watch?v=WHCo4m2VOws</li>
<li>CGP Grey (2017). <i>How AI Actually Learns</i> (first published as "How Machines Learn"). https://www.youtube.com/watch?v=R9OHn5ZF4Uo</li>
<li>Lighthill, J. (1973). <i>Artificial Intelligence: A General Survey.</i> Science Research Council. https://www.aiai.ed.ac.uk/events/lighthill1973/lighthill.pdf</li>
<li>Google DeepMind (17 Jan 2024). <i>AlphaGeometry: An Olympiad-level AI system for geometry.</i> https://deepmind.google/blog/alphageometry-an-olympiad-level-ai-system-for-geometry/</li></ul>
<h3>Sources for the explanations</h3>
<ul><li>Encyclopaedia Britannica: <i>Software</i>; <i>Algorithm</i>; <i>Boolean algebra</i>; <i>Expert system</i>; <i>Artificial intelligence: Expert systems</i>; <i>Machine learning</i>.</li>
<li>BBC Bitesize. <i>What is software?</i> · EBSCO Research Starters. <i>Boolean algebra.</i></li>
<li>OWASP Foundation. <i>Authentication Cheat Sheet.</i> · NIST SP 800-63B-4 (2025).</li>
<li>IBM Developer. <i>What is machine learning?</i> · Wikipedia: <i>Forward chaining</i>; <i>AI winter</i>; <i>Xcon</i>.</li>
<li>McDermott, J. (1981). R1: The formative years. <i>AI Magazine</i> 2(2). · McDermott, J. (1982). R1: A rule-based configurer of computer systems. <i>Artificial Intelligence</i> 19(1), 39–88.</li>
<li>Huyck, C. <i>Configuration with R1/XCon.</i> Middlesex University course notes.</li>
<li>IPSJ Computer Museum. <i>Fifth Generation Computer Systems.</i> · <i>Nature</i> 356, 273 (26 March 1992).</li>
<li>Hertog, J. <i>The Birth of Artificial Intelligence.</i> Dartmouth Alumni Magazine.</li>
<li>Weizenbaum, J. (1966). ELIZA: a computer program for the study of natural language communication between man and machine. <i>Communications of the ACM</i> 9(1), 36–45.</li>
<li>MDN Web Docs. <i>Client-side form validation.</i> · Salesforce Trailhead. <i>Get to Know Business Rules Engine.</i></li>
<li><i>Principles of Computer Game Design and Implementation</i>, Lecture 23 (University of Liverpool course material).</li>
<li>Singhal, A. (2012). <i>Introducing the Knowledge Graph: things, not strings.</i> Google.</li></ul>
<p class="small">Full links for every source are in the reference section of each Markdown topic file (<code>content/01</code>–<code>05</code>).</p>
<h3>Our own material</h3>
<p>The characters BEK, To'ti and Navigator Nodira, the route map, all stories, missions, cards, rule sets, datasets, Prolog and Python files and the diagrams
(Figures 1.1–4.1) were created by Team SilkMind. The Silk Road cities are real places; the caravan stories are fiction and analogies, marked 🐪. Screenshots of SWISH and ELIZA
were taken by the team while testing; SWISH and ELIZA belong to their creators.</p>
<h3>Team SilkMind and contributions</h3>
<table><tr><th>Member</th><th>Role</th><th>Contribution to this guide</th></tr>
<tr><td>Afandiyeva Hayat</td><td>Team lead</td><td></td></tr><tr><td>Khaydarov Sarvarbek</td><td>Repository &amp; information lead</td><td></td></tr>
<tr><td>Nabizadehshahrbabak Arsalan</td><td>Quality lead</td><td></td></tr><tr><td>Egemberdiyeva Aliya</td><td>Content lead</td><td></td></tr>
<tr><td>Kenzhebolat Anel</td><td>Visual design &amp; video lead</td><td></td></tr><tr><td>Mukhtarov Mukhammadshakhruz</td><td>Visual design lead</td><td></td></tr>
<tr><td>Bakatov Madi</td><td>Video lead</td><td></td></tr></table>
<p class="small"><b>AI assistance.</b> Drafting of this guide, its activities, the lab files and the test bank was assisted by an AI model (Claude, Anthropic), which also ran the SWISH and ELIZA tests recorded in Appendix B.
Details, verification and member decisions are recorded in the project AI-use log (<code>docs/ai-use-log.md</code>) and members' personal logs.</p>
<h3>Where this guide comes from</h3>
<table><tr><th>Guide section</th><th>Markdown Content V2.0 source</th></tr>
<tr><td>Stop 1</td><td><code>01-software-and-logic.md</code> §2–§8</td></tr><tr><td>Stop 2, Labs 2A/2B</td><td><code>02-rules-and-inference.md</code> §2–§9</td></tr>
<tr><td>Stop 3, Lab 3</td><td><code>03-symbolic-ai-vs-machine-learning.md</code> §1–§7</td></tr><tr><td>Stop 4</td><td><code>04-history-and-ai-winters.md</code> §1–§7</td></tr>
<tr><td>Stop 5, Lab 5</td><td><code>05-symbolic-ai-in-modern-software.md</code> §1–§7</td></tr><tr><td>Glossary</td><td><code>glossary.md</code></td></tr></table>
"""
