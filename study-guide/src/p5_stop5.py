from kit import *

STOP5 = stop_head(5, "Kashgar", "The Modern Bazaar",
    "Where are BEK's rules hiding in the apps you use every day?",
    "Markdown source: <code>05-symbolic-ai-in-modern-software.md</code> · Outcome LO7 · ≈ 60 min · Missions 5.1–5.3 · Lab 5 (Prolog knowledge graph)") + f"""

{tale("""<p>Kashgar's great bazaar has traded for centuries; today half the stalls take payment by phone. BEK expected to find himself in a museum.
Instead he finds his rules everywhere: in the payment app, in the game the stall-keeper's son is playing, in the delivery app's fee calculator.</p>""")}
{say("bek", "They don't call me \"AI\" any more. They call me \"business logic\". I'm not sure if that's a promotion.")}
{say("toti", "And look: some apps use <i>both</i> of us. I guess the delivery time, then a rule adds 10 minutes when it rains!")}

{predict("""<p>Name <b>three</b> decisions an app on your phone makes that you think are simple IF–THEN rules (not learning). Keep your list for Mission 5.1.</p><div class="writein"></div>""")}

{mission("5.1", "Rule hunt: forms and apps", "10 min",
 "Recognise rule-based decisions in everyday software and write them as IF–THEN rules.",
 "Any website with a sign-up or contact form; one app you use often.",
 """<ol><li>Open a web form and press <b>Submit</b> while a required box is empty. Write down exactly what happens.</li>
<li>Write that behaviour as one IF–THEN rule.</li>
<li>In your app, find <b>two</b> more rule-based decisions and <b>one</b> feature that probably uses machine learning.</li></ol>""",
 "Table: <i>feature · rule or learning? · your evidence</i>.",
 "What made you decide that a feature was \"learning\" and not \"rules\"? Could any feature be both?",
 "Hint: browsers check a field marked <code>required</code> before a form is sent <span class=\"small\">(MDN Web Docs)</span>. Answers → Feedback Corner, Mission 5.1.")}

{real("rules inside modern software", """
<p><b>Forms.</b> When a required field is empty, the browser blocks the form and shows a message such as "Please fill out this field"
<span class="small">(MDN: Client-side form validation)</span>: <code>IF field is required AND empty THEN block AND show message</code>.</p>
<p><b>Business rules engines</b> keep an organisation's decision rules separate from the program so staff can change them. Commercial products
such as Salesforce's Business Rules Engine organise them in <b>decision tables</b> and use them for eligibility, discounts and quotes <span class="small">(Salesforce Trailhead)</span>.
A <b>decision table</b> has one rule per row: conditions on the left, result on the right. A good table covers every case <b>exactly once</b>.</p>
<p><b>Game characters</b> often use a <b>finite state machine</b>: the character is in one <b>state</b> (Wander, Attack, Flee) and a <b>transition rule</b> moves it to another;
game-design teaching material calls this the most common pattern for game AI <span class="small">(Principles of Computer Game Design, Lecture 23)</span>.</p>
<table><tr><th>Rule</th><th>IF current state is…</th><th>AND…</th><th>THEN new state</th></tr>
<tr><td>G1</td><td>Wander</td><td>player is seen</td><td>Attack</td></tr><tr><td>G2</td><td>Attack</td><td>health is low</td><td>Flee</td></tr>
<tr><td>G3</td><td>Attack</td><td>no player is present</td><td>Wander</td></tr><tr><td>G4</td><td>Flee</td><td>no player is present</td><td>Wander</td></tr></table>
<p>If no rule matches, the character <b>stays in its current state</b>.</p>""")}

{mission("5.2", "Guard duty (role-play a finite state machine)", "12 min",
 "Trace a rule-based game character through events, and discover behaviour the rules <b>don't</b> cover.",
 "Rules G1–G4 above. Two players: the <b>Guard</b> (holds a card showing the current state) and the <b>Game</b> (announces events).",
 """<p>The Guard starts in <b>Wander</b> with full health and may only change state using G1–G4. The Game announces five moments:</p>
<ol><li>Player seen, health full</li><li>Player not present, health full</li><li>Player seen, health low</li><li>Player seen, health low</li><li>Player not present, health low</li></ol>
<p>Before playing, <b>predict</b> the Guard's state after each moment. Then play it.</p>""",
 "Record: moment · state before · rule used · state after. Compare with your prediction.",
 "At which moment did your prediction go wrong (if any)? Write the missing rule a designer would need so a fleeing guard with recovered health attacks again.",
 "Hint: in each moment only rules for the <b>current</b> state can apply. Answers → Feedback Corner, Mission 5.2.")}

{mission("5.3", "The delivery-fee bug (find the error in a decision table)", "8 min",
 "Check a decision table for gaps and overlaps, the same boundary skill as Stop 1's 18 °C.",
 "Stop 1, Mission 1.3 Task B.",
 """<table><tr><th>Rule</th><th>Distance (km)</th><th>Fee</th></tr><tr><td>F1</td><td>less than 5</td><td>€2</td></tr>
<tr><td>F2</td><td>more than 5 and at most 10</td><td>€4</td></tr><tr><td>F3</td><td>more than 10</td><td>€6</td></tr></table>
<p>A customer exactly 5 km away gets an error. Test the distances 4, 5, 5.5, 10 and 11 km against each rule, find the problem and fix the table.</p>""",
 "For each test distance write which rules match. Every distance must match <b>exactly one</b> rule.",
 "What would go wrong if you fixed the gap by changing F1 to \"at most 5\" <i>and</i> F2 to \"at least 5\"?",
 "Answers → Feedback Corner, Mission 5.3.")}

{real("knowledge graphs and neuro-symbolic AI", """
<p>A <b>knowledge graph</b> stores facts as <b>things</b> connected by named <b>relationships</b> (<i>Registan → located in → Samarkand</i>).
Google's Knowledge Graph, introduced in 2012 to help search understand "things, not strings", started with over 500 million objects and
3.5 billion facts <span class="small">(Google, 2012)</span>. With one rule, a system can <b>derive</b> facts nobody stored:</p>
<pre>L1: IF X is located in Y AND Y is located in Z THEN X is located in Z</pre>
<p><b>Neuro-symbolic AI</b> combines a learned model with symbolic reasoning. In <b>AlphaGeometry</b> (Google DeepMind, 2024) a symbolic deduction engine
proves geometry facts step by step, like forward chaining; when it gets stuck, a language model suggests one useful new construction (a point, line or circle).
It solved 25 of 30 olympiad geometry problems in the time limit; the previous best automatic method solved 10, and the average human gold medallist 25.9
<span class="small">(DeepMind, 2024)</span>. BEK provides checkable proof; To'ti provides intuition.</p>""")}

{lab("5 · The Silk Road knowledge graph (SWISH Prolog)", f"""
<p><b>Goal.</b> Store a tiny knowledge graph in Prolog, let a rule derive facts nobody typed in, extend the graph, and investigate a rule that never stops.
<b>Platform:</b> SWISH, as in Lab 2A. <b>File:</b> <code>supporting-files/lab-files/lab5_silk_road_graph.pl</code>. Tested 3 Nov 2026.</p>
<pre>located_in(registan,   samarkand).
located_in(samarkand,  uzbekistan).
located_in(uzbekistan, central_asia).

inside(X, Y) :- located_in(X, Y).                   % directly located in
inside(X, Z) :- located_in(X, Y), inside(Y, Z).     % rule L1: follow the links</pre>
<h3>Investigate (predict, then run)</h3>
<table><tr><th>#</th><th>Query</th><th>Prediction</th><th>Result</th></tr>
<tr><td>1</td><td><code>located_in(registan, central_asia).</code></td><td></td><td></td></tr>
<tr><td>2</td><td><code>inside(registan, central_asia).</code></td><td></td><td></td></tr>
<tr><td>3</td><td><code>inside(registan, Where).</code> (press Next)</td><td></td><td></td></tr></table>
{fig("../img/swish-lab5-graph.png", "Figure L5.1 Our SWISH run. The fact is <b>not</b> stored (<code>false</code>), yet the rule <b>derives</b> it (<code>true</code>). <code>findall</code> collects every answer into one list.")}
<p><b>Extend:</b> add <code>located_in(ark_of_bukhara, bukhara).</code> and <code>located_in(bukhara, uzbekistan).</code> <b>next to the other facts</b>, then ask
<code>inside(ark_of_bukhara, central_asia).</code> and <code>inside(What, central_asia).</code></p>
<p><b>Break it (on purpose):</b> change the second rule to <code>inside(X, Z) :- inside(X, Y), inside(Y, Z).</code> and ask <code>inside(registan, mongolia).</code>
Read the error message. What do you think Prolog was doing?</p>
<p><b>Fallback:</b> Figures L5.1 and L5.2 show our runs; trace rule L1 on paper using the table method from Stop 2.</p>""")}

{box("watch", "🎬 Watch / explore", """<p><b>AlphaGeometry: An Olympiad-level AI system for geometry</b>, Google DeepMind blog, 17 January 2024:
<a href="https://deepmind.google/blog/alphageometry-an-olympiad-level-ai-system-for-geometry/">deepmind.google/blog/alphageometry-an-olympiad-level-ai-system-for-geometry/</a></p>
<table><tr><th style="width:24mm">Why use it?</th><td>A real, recent system where BEK-style rules and To'ti-style learning work as a team.</td></tr>
<tr><th>Which part?</th><td>The opening section and the diagram/animation showing the loop between the language model and the symbolic engine.</td></tr>
<tr><th>Your task</th><td>Draw the loop as a cycle with two boxes. Label which box is "symbolic" and which is "learned", and what each passes to the other.</td></tr>
<tr><th>Watch out</th><td>It's written by the company that built the system, so it emphasises successes. The geometry itself is advanced; you only need the loop.</td></tr></table>""")}

{trap("""<table><tr><th>Trap</th><th>The truth</th></tr>
<tr><td>"If it isn't machine learning, it isn't AI."</td><td>Rule-based reasoning is the original AI; it's just rarely called that today.</td></tr>
<tr><td>"A clever game character must be learning."</td><td>Most follow hand-written state rules. Mission 5.2's moment 3 shows behaviour coming only from the rules.</td></tr>
<tr><td>"A knowledge graph only knows what was typed in."</td><td>Rules derive new facts from links (Lab 5, query 2).</td></tr>
<tr><td>"Neuro-symbolic means learning replaced rules."</td><td>Both stay: in AlphaGeometry the symbolic engine does the proof.</td></tr></table>""")}

{check("""<ol><li>A guard in <b>Attack</b> sees the player and has full health for three moments. Which state is it in afterwards, and why?</li>
<li>A cinema charges: child <i>under 12</i> €5, adult <i>over 12 and under 65</i> €10, senior <i>65 or over</i> €7. Which age is not covered?</li>
<li>Facts: Bishkek → Kyrgyzstan, Kyrgyzstan → Central Asia. What can rule L1 derive?</li>
<li>In AlphaGeometry, which part is symbolic AI?</li></ol>""")}

{feedback_corner(f"""
<p><b>Mission 5.1.</b> The browser blocks the form and shows a message (e.g. "Please fill out this field"): <code>IF required field is empty THEN block submission AND show message</code>.
Typical rules: minimum order value disables Checkout; closed shop hides "Order"; password too short shows an error. Typical ML: "recommended for you",
face unlock, spam filtering, voice typing. Evidence for learning: it adapts to you or to millions of users and no fixed rule could list all cases.
Many features are <b>both</b> (a learned estimate plus a fixed rule).</p>
<p><b>Mission 5.2.</b></p>
<table><tr><th>Moment</th><th>State before</th><th>Rule</th><th>State after</th></tr>
<tr><td>1</td><td>Wander</td><td>G1</td><td>Attack</td></tr><tr><td>2</td><td>Attack</td><td>G3</td><td>Wander</td></tr>
<tr><td>3</td><td>Wander</td><td>G1 (health doesn't matter in Wander)</td><td><b>Attack</b></td></tr><tr><td>4</td><td>Attack</td><td>G2</td><td>Flee</td></tr>
<tr><td>5</td><td>Flee</td><td>G4</td><td>Wander</td></tr></table>
<p>The usual wrong prediction is moment 3 ("it should flee"); but G2 needs state <i>Attack</i>, so the guard attacks first and flees at moment 4.
Missing rule: <code>G5: IF state is Flee AND health is not low AND player is seen THEN Attack</code>.</p>
<p><b>Mission 5.3.</b> 4 km → F1; <b>5 km → no rule</b> (not "less than 5", not "more than 5"): a <b>gap</b>; 5.5 → F2; 10 → F2; 11 → F3.
Fix: F2 = <b>at least 5</b> and at most 10. Changing F1 to "at most 5" <i>and</i> F2 to "at least 5" creates an <b>overlap</b>: 5 km matches two rules with different fees.</p>
<p><b>Lab 5 (our SWISH results).</b> 1: <b>false</b>: that fact is not stored. 2: <b>true</b>: derived with rule L1 (Registan → Samarkand → Uzbekistan → Central Asia).
3: <code>samarkand</code>, <code>uzbekistan</code>, <code>central_asia</code>. Extend: <code>inside(ark_of_bukhara, central_asia)</code> is true, and
<code>inside(What, central_asia)</code> lists uzbekistan, registan, samarkand, ark_of_bukhara, bukhara.
Break it: SWISH reports <b>"Stack limit exceeded … Probable infinite recursion"</b> (Figure L5.2). The broken rule's first step is <code>inside(X, Y)</code>, the very thing it is trying to prove,
so Prolog keeps calling the same rule without ever reaching a fact: it never stops. Our working rule always takes one real step (<code>located_in</code>) first.
Lesson: rule order and wording matter, and a rule base can fail in ways that have nothing to do with "knowledge".</p>
{fig("../img/swish-lab5-error.png", "Figure L5.2 Our SWISH run of the broken rule: the extended graph works (top right), but the broken rule makes Prolog recurse until it runs out of memory.")}
<p><b>Checkpoint.</b> 1: <b>Attack</b>: no rule for Attack matches (health not low, player present), so it stays. 2: age <b>12</b>; fix with "12 or over and under 65".
3: Bishkek is located in Central Asia. 4: the symbolic deduction engine.</p>""")}

{postcard("""<p><b>Greetings from Kashgar!</b> BEK's rules live on in <b>forms, decision tables, game characters</b> and <b>knowledge graphs</b>, and in
<b>neuro-symbolic</b> systems where rules and learning work together. One last challenge before the caravan rests…</p>""")}
"""
