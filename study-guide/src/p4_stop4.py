from kit import *

STOP4 = stop_head(4, "Otrar", "The Frozen Caravanserai",
    "Why did the world stop believing in rule-based AI, twice?",
    "Markdown source: <code>04-history-and-ai-winters.md</code> · Outcome LO6 · ≈ 55 min · Missions 4.1–4.4", "nodira") + f"""

{tale("""<p>The caravan camps beside the ruins of Otrar, once a great trading city on the Syr Darya river, now silent mounds of earth.
Around the fire, Nodira tells a story about trading towns that boom when everyone believes in them, then empty when the promises fail.
<i>"The same thing happened to BEK's kind,"</i> she says. <i>"Twice."</i></p>
<p class="small">(The city is real; the comparison between a deserted trading town and an "AI winter" is our analogy, not history.)</p>""")}
{say("bek", "Twice? But rules work! You saw me identify penguins!")}
{say("nodira", "You identify penguins well, BEK. The trouble came when people promised you could do <i>everything</i>. Let's rebuild the story ourselves.")}

{real("what is an AI winter?", """<p>An <b>AI winter</b> is a period in which funding for and interest in AI research fall sharply, usually after expectations were set too high and
results did not match <span class="small">(Wikipedia: AI winter)</span>. Symbolic AI went through the same cycle twice:</p>
<p class="center serif" style="font-size:12pt">big promises → funding → results fall short → funding cut ("winter")</p>""")}

{mission("4.1", "Timeline cards: boom or winter?", "12 min",
 "Place the key events of 1956–1993 in order and spot the two cycles of promise and disappointment.",
 "Event cards 1–9 (Appendix A), a long strip of paper as a timeline.",
 """<ol><li>Without looking at Figure 4.1, put the nine event cards in time order.</li>
<li>Sort each card into <b>Optimism / Boom</b> (green) or <b>Winter / Disappointment</b> (blue) and mark your timeline.</li>
<li>Now compare with Figure 4.1 and fix any mistakes.</li></ol>""",
 "How many events did you place correctly the first time? Where on your strip do the two \"winters\" begin?",
 "Name one thing that happened just <b>before</b> each winter started. Is there a pattern?",
 "Answers → Feedback Corner, Mission 4.1.")}
{fig("../../assets/topic04-ai-timeline.png", "Figure 4.1 Symbolic AI 1956–1993: two cycles of promise and disappointment. Winter start and end years are approximate.")}

{mission("4.2", "Crack the lock: meet the combinatorial explosion", "10 min",
 "Feel why some problems become impossible to solve by checking every possibility, a key reason for the first AI winter.",
 "Calculator or phone. There are 86,400 seconds in a day and about 31.5 million in a year.",
 """<p>A thief tries every code on a lock with digits 0–9 at <b>one guess per second</b>.</p>
<table><tr><th>Digits</th><th>Possible codes</th><th>Time to try them all</th></tr>
<tr><td>1</td><td>10</td><td>10 seconds</td></tr><tr><td>2</td><td>100</td><td></td></tr><tr><td>4</td><td></td><td></td></tr>
<tr><td>6</td><td></td><td></td></tr><tr><td>8</td><td></td><td></td></tr></table>
<p><b>Then:</b> a computer a <b>million</b> times faster tries a <b>16-digit</b> code. How long now?</p>""",
 "What happens to the number of codes each time you add one digit? Did the million-times-faster computer \"solve\" the problem?",
 "Early AI programs searched through possibilities (moves, plans, sentences). Why did programs that worked on small \"toy\" problems fail on real ones?",
 "Answers → Feedback Corner, Mission 4.2.")}

{real("why the winters happened", """
<p><b>First winter (≈1974–1980).</b> Early researchers promised human-like intelligence within a generation. Programs worked on small toy problems
but failed on real ones such as understanding ordinary language. In <b>1973</b> Sir James Lighthill's review for the UK Science Research Council
concluded that <i>"in no part of the field have the discoveries made so far produced the major impact that was then promised"</i> and pointed to the
<b>combinatorial explosion</b> (Mission 4.2). UK funding was sharply reduced, and in the USA DARPA cut grants such as a large speech-recognition project (1974).</p>
<p><b>The boom (1980s).</b> Expert systems such as XCON (in use from 1980) made money, and companies built many more. Japan's
<b>Fifth Generation</b> project (1982–1992) aimed at computers built for knowledge-based reasoning.</p>
<p><b>Second winter (≈1987–1993).</b> Expert systems ran into exactly what you saw at Stop 2: they were <b>brittle</b> (gaps, like Tweety),
<b>costly to maintain</b> (conflicts, like the mystery animal) and could not <b>learn</b>. The market for special LISP-machine computers collapsed in 1987
as cheaper ordinary computers caught up, and new US Strategic Computing funding for AI stopped in 1988. The Fifth Generation project fell well short of its goals.</p>
<p><b>Afterwards:</b> rules did not disappear: they became an ordinary software tool (Stop 5), while research moved toward learning from data (Stop 3).</p>
<p class="small">Sources: Lighthill (1973); Wikipedia: AI winter; IPSJ Computer Museum; Nature 356 (1992); McDermott (1981).</p>""")}

{mission("4.3", "The fact-checker's desk", "12 min",
 "Check a historical claim against more than one source, and decide what to do when sources disagree.",
 "Internet access. The two sources below.",
 """<p>A website says: <i>"Japan's Fifth Generation project ran from 1981 to 1991 and cost $850 million."</i></p>
<ol><li>Open the <b>IPSJ Computer Museum</b> page: <a href="https://museum.ipsj.or.jp/en/computer/other/0002.html">museum.ipsj.or.jp/en/computer/other/0002.html</a>. Find the start year, end year and cost.</li>
<li>Open the <b>Nature</b> news report of 26 March 1992: <a href="https://www.nature.com/articles/356273b0.pdf">nature.com/articles/356273b0.pdf</a>. What does it say about the dates, spending and results?</li></ol>""",
 "Fill a table: <i>claim part · IPSJ says · Nature says · confirmed?</i> for dates, cost and outcome.",
 "When two good sources give different numbers, what should a careful writer do?",
 "No internet? The key facts are in the Feedback Corner. Answers → Feedback Corner, Mission 4.3.")}

{mission("4.4", "It's 1985: pitch an expert system", "12 min",
 "Use Stop 2 evidence to <b>predict</b> why an over-ambitious expert-system project would struggle.",
 "Stop 2 Feedback Corner (Tweety gap, mystery conflict). Groups of 3: one <b>Pitcher</b>, two <b>Critics</b>.",
 """<p>The Pitcher has 1 minute to sell: <i>"An expert system that answers <b>any</b> customer question about <b>any</b> of our 5,000 products!"</i>
The Critics have 2 minutes to predict problems, each backed by something you <b>saw</b> at Stop 2. Then swap roles once.</p>""",
 "List the Critics' predicted problems and the Stop 2 evidence for each.",
 "Which problem would get <b>worse</b> as the product list grows? Connect it to Mission 4.2.",
 "Answers → Feedback Corner, Mission 4.4.")}

{box("watch", "📜 Explore a primary source", """<p><b>Artificial Intelligence: A General Survey</b>, Sir James Lighthill, Science Research Council (UK), 1973. Copy hosted by the University of Edinburgh:
<a href="https://www.aiai.ed.ac.uk/events/lighthill1973/lighthill.pdf">aiai.ed.ac.uk/events/lighthill1973/lighthill.pdf</a></p>
<table><tr><th style="width:24mm">Why use it?</th><td>This is the actual report that helped start the first AI winter, not someone's summary of it.</td></tr>
<tr><th>Which part?</th><td>Use your PDF viewer's search (Ctrl+F) for <b>"major impact"</b> and <b>"combinatorial explosion"</b>; read the paragraph around each.</td></tr>
<tr><th>Your task</th><td>In one sentence each: what did Lighthill say had gone wrong, and what is the combinatorial explosion in his words?</td></tr>
<tr><th>Watch out</th><td>It is a 1970s academic report: long and formal. Read only those two passages. Lighthill's view was also strongly disputed by AI researchers at the time.</td></tr></table>""")}

{trap("""<table><tr><th>Trap</th><th>The truth</th></tr>
<tr><td>"In an AI winter, all AI research stopped."</td><td>Funding and interest fell sharply, but research continued on a smaller scale; some systems (XCON) stayed in use.</td></tr>
<tr><td>"Symbolic AI failed, so it was abandoned."</td><td>It failed to deliver <i>general</i> intelligence, but rule-based methods are still everywhere (Stop 5).</td></tr>
<tr><td>"The winters were only about slow computers."</td><td>Over-promising mattered as much: both winters followed promises far ahead of results.</td></tr>
<tr><td>"History dates are fixed facts."</td><td>Sources disagree (Mission 4.3). Prefer original records, give ranges, and cite.</td></tr></table>""")}

{check("""<ol><li>Put in order: XCON enters use · Lighthill report · Dartmouth workshop · LISP-machine market collapses.</li>
<li>Give one <b>expectations</b> cause and one <b>technology</b> cause of the second AI winter.</li>
<li>True or false: "During the AI winters, all expert systems were switched off." Explain.</li>
<li>How does Stop 2's "mystery animal" help explain why big expert systems were costly?</li></ol>""")}

{feedback_corner("""
<p><b>Mission 4.1.</b> 1956 Dartmouth workshop ("artificial intelligence" named) → 1965 DENDRAL begins → 1972 MYCIN begins → 1973 Lighthill report → 1974 DARPA cuts →
1980 XCON in use → 1982 Fifth Generation project starts → 1987 LISP-machine collapse → 1988 Strategic Computing cuts.
Boom/optimism: 1956, 1965, 1972, 1980, 1982. Winter: 1973–74 and 1987–88. Pattern: each winter followed a period of big promises (general AI soon; the 1980s expert-system and Fifth Generation hopes).</p>
<p><b>Mission 4.2.</b> 2 digits: 100 codes, 100 s. 4: 10,000 codes ≈ 2.8 hours. 6: 1,000,000 codes ≈ 11.6 days. 8: 100,000,000 codes ≈ 3.2 years.
Each extra digit multiplies the work by 10: that is the <b>combinatorial explosion</b>. 16 digits at a million guesses per second: 10<sup>16</sup> ÷ 10<sup>6</sup> = 10<sup>10</sup> seconds ≈ <b>317 years</b>.
A faster computer does not solve the problem, it only moves the wall. Toy problems had few possibilities; real problems have explosively many.</p>
<p><b>Mission 4.3.</b> IPSJ: project <b>1982–1992</b> (11 years), led by ICOT under MITI, about <b>¥54 billion</b>; built several parallel inference machines.
<i>Nature</i> (March 1992): launched 1982, a ten-year project extended by a year; "over $400 million" spent; far short of its goals.
So the <b>dates</b> in the claim are wrong (1981–1991) and the <b>$850 million</b> figure is not supported by either source; the claim that it fell short <b>is</b> confirmed.
A careful writer prefers the project's own records and reports from the time, gives a range or says "about", and cites the source. (Our own Markdown V1.1 had the wrong dates; we corrected them this way.)</p>
<p><b>Mission 4.4.</b> Good predictions: <b>gaps</b>: customers ask things no rule covers, as with Tweety; <b>conflicts and maintenance</b>: thousands of rules, every new product
needs new rules that may clash, like R5/R6; <b>expert time</b>: experts must state every rule and may disagree; <b>language</b>: understanding free-form questions defeated early AI.
Conflicts and maintenance get worse as the list grows: the number of rule combinations that could clash grows explosively (Mission 4.2).</p>
<p><b>Checkpoint.</b> 1: Dartmouth (1956) → Lighthill (1973) → XCON (1980) → LISP-machine collapse (1987).
2: expectations, e.g. expert systems and the Fifth Generation project promised far more than they delivered; technology, e.g. brittle, costly to maintain, could not learn, or LISP machines overtaken by cheaper computers.
3: <b>False</b>: funding fell, but research continued and some systems stayed in use. 4: rules can conflict (tiger <i>and</i> zebra); finding and fixing conflicts among thousands of rules is expensive.</p>""")}

{postcard("""<p><b>Greetings from Otrar!</b> Rule-based AI went through two <b>AI winters</b> (≈1974–80, ≈1987–93). The causes were promises far ahead of results, the
<b>combinatorial explosion</b>, and expert systems that were <b>brittle</b> and costly to maintain. But BEK's kind survived… Next stop: where rules live today.</p>""")}
"""
