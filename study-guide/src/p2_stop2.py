from kit import *

RULES_TABLE = """<table><tr><th>Rule</th><th>IF …</th><th>THEN …</th></tr>
<tr><td><b>R1</b></td><td>has feathers</td><td>is a bird</td></tr>
<tr><td><b>R2</b></td><td>gives milk</td><td>is a mammal</td></tr>
<tr><td><b>R3</b></td><td>is a bird AND cannot fly AND swims</td><td>is a penguin</td></tr>
<tr><td><b>R4</b></td><td>is a bird AND can fly AND hunts at night</td><td>is an owl</td></tr>
<tr><td><b>R5</b></td><td>is a mammal AND eats meat AND has black stripes</td><td>is a tiger</td></tr>
<tr><td><b>R6</b></td><td>is a mammal AND has hooves AND has black stripes</td><td>is a zebra</td></tr></table>"""

STOP2 = stop_head(2, "Bukhara", "BEK's Book of Rules",
    "Can a machine act like an expert if all it does is follow rules?",
    "Markdown source: <code>02-rules-and-inference.md</code> · Outcomes LO3, LO4 · ≈ 80 min · Missions 2.1–2.3 · Labs 2A (Prolog), 2B (ELIZA)") + f"""

{tale("""<p>Bukhara has been a city of scholars for over a thousand years; the great physician Ibn Sina was born nearby. In an old library,
a scholar hands BEK a notebook: <i>"Travellers describe strange animals. Use my rules to tell them what they saw."</i>
The notebook holds six rules. BEK cannot see the animals; he only hears descriptions.</p>""")}
{RULES_TABLE}
{say("bek", "A traveller says: <i>it has feathers, it cannot fly, it swims</i>. No rule says \"penguin\" from those words directly. Must I give up?")}
{say("nodira", "No: you can <b>chain</b> rules. One rule's conclusion can become another rule's condition.")}

{predict("""<p>Using only R1–R6, what will BEK conclude from <i>has feathers, cannot fly, swims</i>? How many rules will he need to use, and in what order?</p><div class="writein"></div>""")}

{real("the parts of a rule-based system", """
<p>BEK is now an <b>expert system</b>: a program that solves problems in one specialised area, the kind usually needing a human expert, using a
<b>knowledge base</b> of rules and an <b>inference engine</b> <span class="small">(Britannica: Expert systems)</span>.</p>
<table><tr><th>Part</th><th>What it is</th><th>In BEK's library</th></tr>
<tr><td><b>Symbol</b></td><td>A label that stands for something. The computer does <b>not</b> know what it means.</td><td><code>has feathers</code></td></tr>
<tr><td><b>Fact</b></td><td>A statement taken as true for the current case</td><td>"cannot fly"</td></tr>
<tr><td><b>Rule</b></td><td>IF (all conditions true) THEN (add a conclusion)</td><td>R1–R6</td></tr>
<tr><td><b>Knowledge base</b></td><td>All the rules; <b>the same</b> for every case</td><td>The scholar's notebook</td></tr>
<tr><td><b>Working memory</b></td><td>The facts for <b>this</b> case: starting facts + new ones</td><td>BEK's notepad</td></tr>
<tr><td><b>Inference engine</b></td><td>The loop that finds rules whose IF part is true and <b>fires</b> them</td><td>BEK's "brain"</td></tr></table>""")}
{fig("../../assets/topic02-expert-system-architecture.png", "Figure 2.1 Parts of a rule-based system. Only the inference engine \"does\" anything; the knowledge base stays fixed while working memory changes for each case.", "70%")}

{mission("2.1", "Rule Cards: be the inference engine", "20 min",
 "Experience <b>forward chaining</b> from the inside: fire rules cycle by cycle, record a <b>trace table</b>, and see when the engine stops.",
 "Rule cards R1–R6 and fact cards (Appendix A), or the table above. Groups of 3: <b>Memory keeper</b> (holds fact cards), <b>Engine</b> (checks rules), <b>Recorder</b>.",
 """<ol><li>Memory keeper lays down the starting facts: <b>has feathers · cannot fly · swims</b>.</li>
<li>Engine checks the rule cards <b>in order R1 → R6</b>. The first rule whose IF part is <b>completely</b> on the table <b>and</b> whose THEN fact is not yet on the table <b>fires</b>: the Memory keeper adds its THEN card.</li>
<li>That is one <b>cycle</b>. Start again from R1. Stop when a whole cycle adds nothing new.</li>
<li>Play again with: <b>gives milk · has hooves · has black stripes</b>.</li>
<li>Last round: <b>gives milk · eats meat · has hooves · has black stripes</b>. Predict the result before you play!</li></ol>""",
 """<p>Recorder fills a trace table for each round:</p>
<table><tr><th>Cycle</th><th>Facts on table at start</th><th>Rule fired</th><th>New fact</th></tr><tr><td>1</td><td></td><td></td><td></td></tr><tr><td>2</td><td></td><td></td><td></td></tr><tr><td>3</td><td></td><td></td><td></td></tr><tr><td>4</td><td></td><td></td><td></td></tr></table>""",
 "Why can't R3 fire in cycle 1 of round 1? What went strange in the last round: is the <b>engine</b> wrong, or the <b>rules</b>?",
 "Hint: new facts only become usable in the <i>next</i> cycle. Answers → Feedback Corner, Mission 2.1.")}
{fig("../../assets/topic02-forward-chaining.png", "Figure 2.2 Round 1 as a picture: R1 turns \"has feathers\" into \"is a bird\"; then R3 combines three facts into \"is a penguin\".", "92%")}

{real("forward chaining, backward chaining and explanations", """
<p><b>Forward chaining</b> starts from facts and fires rules until nothing new can be added. It is <b>data-driven</b>.
<b>Backward chaining</b> starts from a <b>goal</b> ("is it a penguin?") and works backwards to the facts needed to prove it. It is <b>goal-driven</b>,
and it can <b>ask</b> the user only the questions that matter. <span class="small">(Wikipedia: Forward chaining)</span></p>
<p>Because every new fact was added by a named rule, the system can <b>explain</b> itself: <i>"penguin, because R3; bird, because R1; the rest you told me."</i>
Real systems such as MYCIN could explain their reasoning on request <span class="small">(Britannica: Expert systems)</span>.</p>""")}

{mission("2.2", "Twenty Questions, rule-style (backward chaining)", "10 min",
 "Use backward chaining to ask only the questions needed to prove or reject a goal.",
 "R1–R6. A partner secretly picks one of the animal descriptions from Mission 2.1.",
 """<ol><li>Choose a goal, for example <b>"is a tiger?"</b>. Find the only rule that concludes it (R5) and list its conditions.</li>
<li>For each condition that is itself a conclusion (<i>is a mammal</i>), find <i>its</i> rule (R2) and list <i>its</i> conditions.</li>
<li>Now ask your partner <b>only</b> those questions, in order. Stop as soon as one answer is "no".</li></ol>""",
 "Write your question list for the goal \"tiger\". Count how many questions you needed. How many would \"ask about everything\" need?",
 "Why would a doctor's diagnosis system prefer backward chaining?",
 "Answers → Feedback Corner, Mission 2.2.")}

{lab("2A · BEK's rules in real Prolog (SWISH)", f"""
<p><b>Goal.</b> Run the same six rules in <b>Prolog</b>, a real programming language for logic, predict its answers, add a rule, and investigate surprising results.
<b>Platform:</b> SWISH (SWI-Prolog in the browser), <a href="https://swish.swi-prolog.org">swish.swi-prolog.org</a>. Free, no account. Tested 3 Nov 2026 (Appendix E).
<b>File:</b> <code>supporting-files/lab-files/lab2_animal_expert.pl</code>.</p>
<h3>Just enough Prolog</h3>
<table><tr><th>You write</th><th>Read it as</th></tr>
<tr><td><code>fact(pingu, swims).</code></td><td>A <b>fact</b>: "Pingu swims." Every line ends with a full stop.</td></tr>
<tr><td><code>is_a(X, bird) :- fact(X, has_feathers).</code></td><td>A <b>rule</b>: "X is a bird <b>IF</b> X has feathers." <code>:-</code> means IF; a comma means AND.</td></tr>
<tr><td><code>X</code>, <code>What</code>, <code>Who</code></td><td>Words starting with a <b>capital letter</b> are <b>variables</b> ("something"). Lower-case words are fixed names.</td></tr>
<tr><td><code>is_a(pingu, What).</code></td><td>A <b>query</b>: "What is Pingu?" Prolog answers by searching the rules.</td></tr>
<tr><td><code>% text</code></td><td>A comment, ignored by Prolog.</td></tr></table>
<h3>Steps</h3>
<ol><li>Open SWISH → click <b>Program</b> (top of the left panel). Delete anything in the editor.</li>
<li>Paste the whole of <code>lab2_animal_expert.pl</code> into the left editor.</li>
<li>Type a query in the bottom-right box (<i>Your query goes here…</i>), e.g. <code>is_a(pingu, What).</code>, and press <b>Run!</b></li>
<li>Prolog shows the first answer. Click <b>Next</b> for more, or <b>Stop</b> when done. <i>Tip: if SWISH says "Too many open queries", press Stop on old queries.</i></li></ol>
{fig("../img/swish-lab2-pingu.png", "Figure L2.1 Our test run in SWISH: the program on the left; the query <code>is_a(pingu, What).</code> gave <code>What = bird</code>, then (after Next) <code>What = penguin</code>.")}
<h3>Investigate (predict first, then run)</h3>
<table><tr><th>#</th><th>Query</th><th>Your prediction</th><th>Prolog's answer</th></tr>
<tr><td>1</td><td><code>is_a(pingu, penguin).</code></td><td></td><td></td></tr>
<tr><td>2</td><td><code>is_a(Who, bird).</code> (press Next until it stops)</td><td></td><td></td></tr>
<tr><td>3</td><td><code>is_a(tweety, What).</code></td><td></td><td></td></tr>
<tr><td>4</td><td><code>is_a(mystery, What).</code></td><td></td><td></td></tr>
<tr><td>5</td><td><code>is_a(Pingu, penguin).</code> (capital P!)</td><td></td><td></td></tr></table>
<p><b>Build:</b> add a giraffe called <code>gerald</code>. Add three facts (gives milk, has a long neck, has hooves) and a rule R7 that concludes
<code>giraffe</code>. Test with <code>is_a(gerald, What).</code> Then deliberately misspell one fact (e.g. <code>has_long_nek</code>) and run it again.</p>
<p><b>Reflect:</b> Prolog answers <code>is_a(pingu, penguin)</code> by starting from the <b>goal</b>. Which kind of chaining is that? Why did Tweety get only one answer?</p>
<p><b>Fallback (no internet):</b> read the outputs in the Feedback Corner and Figure L2.2, or run <code>supporting-files/examples/topic02_mini_rule_engine.py</code> (forward chaining in Python, same rules).</p>""")}

{lab("2B · ELIZA: rules that <i>pretend</i> to understand", f"""
<p><b>Goal.</b> Discover how a famous 1966 program held "conversations" using nothing but <b>pattern rules</b>, and find where the illusion breaks.
<b>Platform:</b> ELIZA in JavaScript by Norbert Landsteiner (2005), a re-creation of Joseph Weizenbaum's 1966 DOCTOR script:
<a href="https://www.masswerk.at/elizabot/eliza.html">masswerk.at/elizabot/eliza.html</a> → click <b>open ELIZA terminal</b>. No account.
(Other versions, including the reconstructed original listed by the ELIZA history project at elizagen.org, may answer differently.)</p>
<h3>Steps</h3>
<ol><li>Open the terminal and type each of the seven test lines below, pressing Enter after each. Use your own words afterwards.</li>
<li>Record ELIZA's reply next to each line, and <b>circle the word</b> in your input that you think triggered it.</li></ol>
{fig("../img/eliza-transcript.png", "Figure L2.3 Our test conversation (3 Nov 2026). In the version we tested, ELIZA's replies can vary between runs; even its opening line changed when we reloaded.", "88%")}
<table><tr><th>#</th><th>We typed</th><th>ELIZA replied</th></tr>
<tr><td>1</td><td>i am worried about my exams</td><td>Is it important to you that you have your exams ?</td></tr>
<tr><td>2</td><td>my mother does not understand me</td><td>Your mother ?</td></tr>
<tr><td>3</td><td>i think computers are scary</td><td>What do you think about machines ?</td></tr>
<tr><td>4</td><td>the bus to samarkand leaves at nine</td><td>Lets discuss further why your exams.</td></tr>
<tr><td>5</td><td>i am worried about my exams <i>(again)</i></td><td>Does that suggest anything else which belongs to you ?</td></tr>
<tr><td>6</td><td>what is two plus two</td><td>What do you think ?</td></tr>
<tr><td>7</td><td>i am a robot made of cheese</td><td>Do you know anyone else who is a robot made of cheese ?</td></tr></table>
<h3>Investigate</h3>
<ol><li><b>Keywords:</b> which input words seem to trigger which kind of reply (lines 2, 3, 6)?</li>
<li><b>Copying:</b> in lines 1 and 7, which of your words came back? What changed (look at <i>my → your</i>)?</li>
<li><b>Memory:</b> line 4 has no keyword at all. Where did "your exams" come from? Why is the grammar broken?</li>
<li><b>Repeats:</b> why is reply 5 different from reply 1?</li>
<li><b>Break it:</b> find your own input that makes ELIZA's lack of understanding obvious. Write it down.</li></ol>
<p><b>Fallback:</b> analyse the printed transcript above; it contains everything needed.</p>""")}

{watch("Symbolic AI: Crash Course AI #10", "CrashCourse with PBS Digital Studios (YouTube, 13 min, 2019)", "https://www.youtube.com/watch?v=WHCo4m2VOws",
 "A lively recap of everything at this stop: symbols, knowledge bases, truth tables, IF–THEN inference and expert systems, including their limits.",
 "<b>03:45–07:15</b> \"How does it work\": propositional logic, truth tables, AND/OR/NOT. <b>07:15–end</b> \"Implications\": if-then rules, inference, expert systems and why they are limited.",
 "While watching 07:15–end, write down one <b>advantage</b> and one <b>limit</b> of expert systems the video gives. Compare with Section \"Real expert systems\" below.",
 "The video computes AND and OR with multiplication and addition of 1s and 0s. That is a neat trick, but in Boolean logic \"1 + 1\" still just means <i>true</i>. Its symbols and examples differ from ours; the ideas are the same. Captions are available.")}

{real("real expert systems, and their limits", """
<table><tr><th>System</th><th>When / where</th><th>What it did</th></tr>
<tr><td><b>DENDRAL</b></td><td>from 1965, Stanford</td><td>Suggested molecular structures from spectrograph data; often called the first expert system</td></tr>
<tr><td><b>MYCIN</b></td><td>from 1972, Stanford</td><td>Diagnosed blood infections with about 500 rules; explained its reasoning; about as good as specialists</td></tr>
<tr><td><b>XCON (R1)</b></td><td>Carnegie Mellon for DEC; in use from January 1980</td><td>Configured computer orders; estimated to save DEC about $25 million a year by 1986</td></tr></table>
<p class="small">Sources: Britannica: Expert systems; McDermott (1981); Middlesex University XCON notes.</p>
<p><b>Strengths:</b> explainable; uses expert knowledge directly; predictable. <b>Limits:</b> no common sense: told about a patient
bleeding from a gunshot wound, MYCIN would still look for a bacterial cause <span class="small">(Britannica)</span>. Systems know only what their rules cover
(<b>brittle</b>), and big rule bases are hard to maintain because new rules can <b>conflict</b> with old ones.</p>""")}

{mission("2.3", "Explain like the scholar (write the 'why?')", "10 min",
 "Produce an <b>explanation chain</b> for a conclusion, the strength that makes rule-based systems trustworthy.",
 "Your trace from Mission 2.1 round 2 (zebra).",
 "Write BEK's answer to a traveller who asks <i>\"Why do you say zebra?\"</i> as an indented \"because…\" chain, ending at the facts the traveller gave.",
 "Check that every line names a rule or says \"you told me\".",
 "Show your chain to a partner. Could they spot a wrong step from your chain alone? Why is that valuable for a doctor using MYCIN?",
 "Model chain → Feedback Corner, Mission 2.3.")}

{trap("""<table><tr><th>Trap</th><th>The truth</th></tr>
<tr><td>"The system understands animals."</td><td>It matches symbols. Rename every word to <code>X17</code> and it reasons the same way (ELIZA shows the same illusion with language).</td></tr>
<tr><td>"If the answer is right, the reasoning is right."</td><td>A trace can reach "tiger" by firing R5 too early. Check the steps, not just the answer.</td></tr>
<tr><td>"A strange answer means the engine is broken."</td><td>Usually the <b>knowledge base</b> has a gap (Tweety) or a conflict (mystery).</td></tr>
<tr><td>"Forward and backward chaining reach different conclusions."</td><td>Same rules and facts give the same conclusions; they differ in direction and in which questions they ask.</td></tr></table>""")}

{check("""<ol><li>Which part changes for every new case: the knowledge base or working memory?</li>
<li>When does forward chaining stop?</li>
<li>Rule <code>IF A AND B THEN C</code>; working memory holds only A. Does it fire?</li>
<li>In Prolog, why does <code>is_a(Pingu, penguin).</code> answer <code>Pingu = pingu</code> instead of <code>true</code>?</li>
<li>Name one thing ELIZA's conversation does <b>not</b> show, even though it looks clever.</li></ol>""")}

{feedback_corner(f"""
<p><b>Predict box.</b> Two rules, in this order: R1 (has feathers → is a bird), then R3 (bird + cannot fly + swims → penguin).</p>
<p><b>Mission 2.1.</b></p>
<div class="two"><div><table><tr><th colspan="3">Round 1: penguin</th></tr><tr><th>Cycle</th><th>Fired</th><th>New fact</th></tr>
<tr><td>1</td><td>R1</td><td>is a bird</td></tr><tr><td>2</td><td>R3</td><td>is a penguin</td></tr><tr><td>3</td><td>–</td><td>stop</td></tr></table></div>
<div><table><tr><th colspan="3">Round 2: zebra</th></tr><tr><th>Cycle</th><th>Fired</th><th>New fact</th></tr>
<tr><td>1</td><td>R2</td><td>is a mammal</td></tr><tr><td>2</td><td>R6</td><td>is a zebra</td></tr><tr><td>3</td><td>–</td><td>stop</td></tr></table></div></div>
<p>R3 cannot fire in cycle 1 because <i>is a bird</i> is not yet on the table. <b>Last round:</b> cycle 1 R2 → mammal; cycle 2 R5 → <b>tiger</b>; cycle 3 R6 → <b>zebra</b>; cycle 4 stop.
The animal is "both a tiger and a zebra"! The engine is fine: the <b>knowledge base</b> has a <b>rule conflict</b> (R5 and R6 both accept a striped mammal).
A fix: add <i>does not have hooves</i> to R5, then re-test every earlier round. (Checked with <code>topic02_mini_rule_engine.py</code>.)</p>
<p><b>Mission 2.2.</b> Goal tiger → R5 needs <i>is a mammal</i>, <i>eats meat</i>, <i>has black stripes</i>; <i>is a mammal</i> → R2 needs <i>gives milk</i>.
Questions: "Does it give milk?" → "Does it eat meat?" → "Does it have black stripes?": 3 questions, stopping early at any "no". Asking about every fact would take 8 questions.
A diagnosis system prefers backward chaining because it tests one suspected illness and asks only relevant questions.</p>
<p><b>Lab 2A (our SWISH results).</b> 1: <code>true</code> (Prolog proves the goal backwards: penguin needs bird, which needs has_feathers). 2: <code>pingu</code>, <code>hoot</code>, <code>tweety</code>.
3: only <code>bird</code>: no rule covers a flying bird that does not hunt at night (a <b>gap</b>). 4: <code>mammal</code>, <code>tiger</code>, <code>zebra</code>: the <b>rule conflict</b> (Figure L2.2).
5: <code>Pingu = pingu</code>: the capital letter made <code>Pingu</code> a <b>variable</b>, so Prolog answered "which animal is a penguin?". Lower-case names matter!
<b>Build:</b> <code>fact(gerald, gives_milk). fact(gerald, has_long_neck). fact(gerald, has_hooves).</code> and
<code>is_a(X, giraffe) :- is_a(X, mammal), fact(X, has_long_neck), fact(X, has_hooves).</code> gives <code>mammal</code>, then <code>giraffe</code>. With the typo, Prolog simply answers <b>false</b>,
because to a computer <code>has_long_nek</code> and <code>has_long_neck</code> are different symbols; it never "guesses" what you meant.
<b>Reflect:</b> Prolog starts from the goal, so this is <b>backward chaining</b>.</p>
{fig("../img/swish-lab2-mystery.png", "Figure L2.2 Our SWISH run of query 4: <code>mystery</code> is a mammal, a tiger <i>and</i> a zebra. The rules conflict.", "100%")}
<p><b>Lab 2B (ELIZA).</b> ELIZA works with a <b>script</b> of rules: it looks for a <b>keyword</b> (e.g. <i>mother</i>, <i>computer</i>, <i>what</i>, <i>my</i>, <i>I am</i>), breaks the sentence
into parts with a matching <b>pattern</b>, and builds a reply from a <b>template</b>, swapping pronouns (my → your, I → you) <span class="small">(Weizenbaum, 1966)</span>.
1/7: your own words came back with pronouns swapped, even nonsense such as "a robot made of cheese": no understanding involved.
2/3/6: keyword families (family words → "Your mother?"; computer → machines; a question → "What do you think?"). ELIZA did <b>not</b> calculate 2 + 2.
4: no keyword, so ELIZA reused a phrase it <b>stored earlier</b> from a "my …" sentence; pasting it into a template broke the grammar.
5: a keyword usually has several reply templates, so the same input can get a different reply.
<b>What it does not show:</b> understanding, memory of facts, reasoning, or knowing what any word means. It is a powerful example of how <b>rules over symbols</b> can <i>look</i> intelligent.</p>
<p><b>Mission 2.3 (model chain).</b> "Zebra, because R6: it is a mammal AND has hooves AND has black stripes. → It is a mammal because R2: it gives milk.
→ 'gives milk', 'has hooves' and 'has black stripes' are what you told me." A doctor can check each line, so a wrong step is easy to spot.</p>
<p><b>Checkpoint.</b> 1: working memory. 2: when a whole cycle adds no new fact. 3: no; AND needs both.
4: capitalised words are variables in Prolog. 5: e.g. it does not understand meaning, cannot answer factual questions, or does not know a robot can't be made of cheese.</p>""")}

{postcard("""<p><b>Greetings from Bukhara!</b> BEK became an <b>expert system</b>: a <b>knowledge base</b> of IF–THEN rules plus an <b>inference engine</b> that
<b>chains</b> them, forwards from facts or backwards from a goal, and can <b>explain</b> every conclusion. But BEK knows only what his rules say:
gaps and conflicts are his weak spots. Next stop: a parrot who has no rules at all…</p>""")}
"""
