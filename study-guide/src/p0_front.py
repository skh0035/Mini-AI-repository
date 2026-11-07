from kit import *

ROUTEMAP = open("routemap.svg.html").read()

COVER = f"""
<div class="cover">
  <img class="logo" src="../../assets/silkmind-logo.png" alt="SilkMind logo">
  <h1>The SilkMind Caravan</h1>
  <div class="tag">Old routes. New roots.</div>
  <div class="sub">A hands-on study guide to <b>Software &amp; Symbolic AI</b>: travel the Silk Road with a robot who follows rules,
  a parrot who learns from examples, and a navigator who explains what is really going on.</div>
  <div class="cast">
    <div><svg width="92" height="100" viewBox="0 0 100 110"><use href="#bek"/></svg><br>BEK</div>
    <div><svg width="92" height="100" viewBox="0 0 100 110"><use href="#toti"/></svg><br>To'ti</div>
    <div><svg width="92" height="92" viewBox="0 0 100 100"><use href="#nodira"/></svg><br>Navigator Nodira</div>
  </div>
  <div class="meta">
    <b>Study Guide V1.0</b> · Stage 2 · November 2026<br>
    Team <b>SilkMind</b>: Afandiyeva Hayat · Khaydarov Sarvarbek · Nabizadehshahrbabak Arsalan · Egemberdiyeva Aliya ·
    Kenzhebolat Anel · Mukhtarov Mukhammadshakhruz · Bakatov Madi<br>
    Module: Software &amp; Symbolic AI · Built from Markdown Content V2.0 · github.com/skh0035/Mini-AI-repository<br>
    Companion files: Test Bank (Word) · lab files (.pl, .py, .ipynb) · printable cards (Appendix A)
  </div>
</div>
"""

WELCOME = f"""
<h1>Welcome aboard the caravan</h1>
{say("nodira", "Salom! I'm Nodira, navigator of this caravan. Over five stops you will <b>build, break and fix</b> small rule-based systems, train a model, and find out why the world twice stopped believing in rule-based AI. You will spend more time <i>doing</i> than reading.")}
{say("bek", "I am BEK. I follow rules. Exactly. Every time. If the rule is wrong, I am wrong. Please write good rules.")}
{say("toti", "And I'm To'ti! Nobody gives me rules: I copy patterns from examples. Usually that works. Sometimes... squawk.")}

<h2>Who this guide is for</h2>
<p>First-year students from <b>any</b> subject with <b>no</b> programming, computer-science or AI background. If you can use a phone, read a table
and compare two numbers (is 15 smaller than 18?), you are ready.</p>

<h2>What you need</h2>
<table>
<tr><th>For</th><th>You need</th><th>If you can't get it</th></tr>
<tr><td>Every stop</td><td>Pen, paper, this guide, a partner if possible</td><td>Work alone: play every role yourself</td></tr>
<tr><td>Card missions (Stops 2–4)</td><td>Printed and cut cards from <b>Appendix A</b> (or copy them onto paper)</td><td>Use the tables in the mission instead of cards</td></tr>
<tr><td>Labs 2A, 5 (Prolog)</td><td>A browser and <a href="https://swish.swi-prolog.org">swish.swi-prolog.org</a>. No account or install needed. Starter files are in <code>supporting-files/lab-files/</code>.</td><td>Use the screenshots and outputs printed in the lab, or run <code>supporting-files/examples/topic02_mini_rule_engine.py</code></td></tr>
<tr><td>Lab 2B (ELIZA)</td><td>A browser and <a href="https://www.masswerk.at/elizabot/eliza.html">masswerk.at/elizabot</a></td><td>Analyse the printed transcript in the lab</td></tr>
<tr><td>Lab 3 (Machine Learning for Kids)</td><td>A browser, <a href="https://machinelearningforkids.co.uk">machinelearningforkids.co.uk</a> → "Try it now" (no account; you must tick a "Verify you are human" box)</td><td>Run <code>supporting-files/examples/topic03_learn_a_rule.py</code> or the notebook <code>SilkMind_Labs.ipynb</code></td></tr>
<tr><td>Optional code</td><td>Python 3 (no extra packages) or Google Colab / Jupyter for the notebook</td><td>Every result is also printed in this guide</td></tr>
</table>
<p class="small">Access note: our testing record is in Appendix E. Some sites (YouTube in particular) are not reachable on every network, so every video and lab has a written summary, screenshots or a fallback, and you can always continue without it.</p>

<h2>How every stop works</h2>
<p>Each stop is built around <b>one question</b> and follows the same rhythm:</p>
<p class="center serif" style="font-size:12pt">Meet a problem → <b>predict</b> → <b>try</b> it → <b>observe</b> → understand the <b>real thing</b> → <b>apply</b> it → <b>check</b></p>
<div class="legend">
 {box("tale","🐪 Caravan tale","Story and analogy. Fun, but not a technical claim.")}
 {box("real","🧭 The real thing","The accurate technical explanation. This is what you are tested on.")}
 {box("predict","🔮 Predict first","Write a guess <i>before</i> you try. Wrong guesses teach the most.")}
 {box("check","✅ Checkpoint","Quick questions; answers in the Feedback Corner at the end of the stop.")}
 <div class="mission" style="margin:0"><div class="mhead"><span class="num">M</span>Mission</div><div class="row"><div class="k">6 parts</div><div class="v" style="font-size:9pt">Goal · Preparation · Task · Observation · Reflection · Feedback</div></div></div>
 {box("lab","🧪 Lab","A real online tool, with exact steps, screenshots and a fallback.")}
 {box("watch","🎬 Watch / explore","A short video or page, with what to watch for.")}
 {box("trap","⚠️ Traps","Mistakes beginners often make, and the truth.")}
</div>

<h2>Your route</h2>
{ROUTEMAP}
<h3>What you will be able to do</h3>
<table>
<tr><th>#</th><th>By the end you can…</th><th>Stop</th></tr>
<tr><td>LO1</td><td>Explain what software, an algorithm and a Boolean condition are, using an everyday example.</td><td>1</td></tr>
<tr><td>LO2</td><td>Write a decision as an IF–THEN rule and check it with a truth table.</td><td>1</td></tr>
<tr><td>LO3</td><td>Describe the parts of a rule-based (symbolic) AI system: facts, rules, knowledge base, working memory, inference engine.</td><td>2</td></tr>
<tr><td>LO4</td><td>Trace forward and backward chaining by hand, and in Prolog, and explain a conclusion.</td><td>2</td></tr>
<tr><td>LO5</td><td>Contrast symbolic AI with machine learning, trace how a simple model learns a rule from data, and choose an approach.</td><td>3</td></tr>
<tr><td>LO6</td><td>Explain why symbolic AI rose, fell (the "AI winters") and changed, using evidence.</td><td>4</td></tr>
<tr><td>LO7</td><td>Find and trace rule-based reasoning in modern software, including systems that mix rules and learning.</td><td>5</td></tr>
</table>

<h3>Choose your route</h3>
<table>
<tr><th>Route</th><th>What to do</th><th>Time</th></tr>
<tr><td><b>Full caravan</b> (recommended)</td><td>Every mission, lab and checkpoint, in order, then the Grand Caravan Challenge</td><td>≈ 5 h, over 2–3 sessions</td></tr>
<tr><td><b>Express route</b></td><td>Missions 1.2, 2.1, 3.1, 4.1, 5.2 + all checkpoints + Lab 2A</td><td>≈ 2.5 h</td></tr>
<tr><td><b>Lab lover</b></td><td>Express route + Labs 2B, 3, 5 + the Grand Challenge in SWISH</td><td>≈ 4 h</td></tr>
</table>
<p>Stops must be taken <b>in order</b>: each one uses what you discovered at the stop before. The test bank (separate document) checks every learning outcome.</p>
"""
