from kit import *

STOP1 = stop_head(1, "Khiva", "The Gate That Says No",
    "How does a machine decide who may pass, and why does it never \"get the idea\"?",
    "Markdown source: <code>01-software-and-logic.md</code> · Outcomes LO1, LO2 · ≈ 45 min · Missions 1.1–1.3") + f"""

{tale("""<p>The caravan reaches Khiva, whose old inner town, Itchan Kala, is still surrounded by tall clay walls. The guards are tired, so the city hires
<b>BEK</b> as a gatekeeper. BEK is given one sheet of instructions and told: <i>"Let in only people who belong here."</i></p>
<p>On his first morning, BEK lets in a goat (nobody said goats were not allowed), refuses the mayor (he forgot his pass), and
spends twenty minutes trying to "check the weather" because the sheet said <i>"close the gate if it looks bad outside."</i></p>""")}
{say("bek", "I did exactly what the sheet said. Is that not what a good machine does?")}
{say("nodira", "It is! That is the whole point of this stop: a computer does <b>exactly</b> what its instructions say, nothing more. So the instructions must be perfect.")}

{predict("""<p>Before you start, write down your guess: <b>why</b> did BEK spend twenty minutes on <i>"close the gate if it looks bad outside"</i>?
What would you change in that instruction so a machine could follow it?</p><div class="writein"></div>""")}

{mission("1.1", "Be BEK: the Exact Instructions game", "15 min",
 "Discover that computers follow instructions <b>literally</b>, and that a good instruction is precise, ordered and complete (an <b>algorithm</b>).",
 "A partner, two sheets of paper, a pen. No prior knowledge.",
 """<ol><li><b>Writer</b> (back-to-back with BEK, so BEK cannot see): draw a simple <i>caravan tent</i>: a square with a triangle on top and a door. Hide it.</li>
<li>The Writer writes <b>at most 8 instructions</b> so BEK can draw the same picture without seeing it.</li>
<li><b>BEK</b> follows each instruction <b>exactly as written</b>. If it is unclear, BEK does the strangest thing it could mean, and does <b>not</b> ask questions.</li>
<li>Compare the two drawings. Then swap roles and try again with improved instructions.</li></ol>""",
 """<p>Record in a small table: <i>instruction number · what the Writer meant · what BEK did</i>. Mark each instruction that failed.</p>
<p>Count: how many failed in round 1? In round 2?</p>""",
 """<p>Which words caused most failures (e.g. "small", "near", "a bit")? What did you add in round 2 to make instructions work: numbers? order? a stop condition?</p>""",
 "Hint: look for missing <b>start points</b>, <b>sizes</b> and <b>order</b>. Explained outcome → Feedback Corner, Mission 1.1.")}

{watch("Exact Instructions Challenge – THIS is why my kids hate me", "Josh Darnit (YouTube)", "https://www.youtube.com/watch?v=cDA3_5982h8",
 "A father makes a sandwich by following his children's written instructions <i>literally</i>. It is the same game you just played, and very funny.",
 "Watch the whole video (it is short).",
 "Pause after each instruction the children give. Predict what Dad will do. Then list two instructions you would rewrite, and how.",
 "Dad is pretending to be a machine for comedy; real computers don't \"choose\" the silliest meaning. They simply cannot fill gaps at all. Not available? Mission 1.1 teaches the same idea.")}

{real("software, algorithms and conditions", """
<p><b>Software</b> is the set of instructions (programs) that tell a computer what to do; <b>hardware</b> is the physical machine:
screen, processor, sensors, keyboard. You cannot touch software. <span class="small">(Britannica: Software)</span></p>
<p>An <b>algorithm</b> is a step-by-step procedure that solves a problem in a finite number of clear steps. A recipe is an algorithm for people;
a program is an algorithm a computer can run. <span class="small">(Britannica: Algorithm)</span></p>
<p>Many steps are <b>decisions</b>, such as <i>"IF the password is correct THEN let the user in, ELSE refuse."</i> The question
"is the password correct?" has only two answers, <b>true</b> or <b>false</b>. It is a <b>Boolean condition</b>, named after George Boole, who set out this logic in 1847.
<span class="small">(Britannica: Boolean algebra)</span> Conditions are combined with three operators:</p>
<table><tr><th>Operator</th><th>True when…</th><th>Example</th></tr>
<tr><td><b>AND</b></td><td><b>both</b> parts are true</td><td>account exists AND password matches</td></tr>
<tr><td><b>OR</b></td><td><b>at least one</b> part is true (including both)</td><td>is a student OR is over 65</td></tr>
<tr><td><b>NOT</b></td><td>flips true ↔ false</td><td>NOT account is locked</td></tr></table>
<p>A <b>truth table</b> lists every combination of true/false inputs and the result for each, so no case is forgotten.</p>""")}

{mission("1.2", "The Gatekeeper's rulebook (login logic)", "15 min",
 "Trace a real decision (an app's login) step by step, check it with a truth table, and <b>find the error</b> in a faulty rule.",
 "The Real Thing box above. Optional: two cards marked <b>T</b> and two marked <b>F</b>.",
 """<p><b>Part A: trace.</b> An email app receives an email address and a password. It checks: <b>(1)</b> does an account exist for this email?
<b>(2)</b> does the password match? Only if both are true does it open the inbox. Follow the flowchart below for these three visitors and write the result:</p>
<table><tr><th>Visitor</th><th>Account exists?</th><th>Password matches?</th><th>Result?</th></tr>
<tr><td>Aziz</td><td>True</td><td>True</td><td></td></tr><tr><td>Bekzod</td><td>True</td><td>False</td><td></td></tr><tr><td>A stranger</td><td>False</td><td>–</td><td></td></tr></table>
<p><b>Part B: find the error.</b> A trainee writes the rule as <code>access = account_exists OR password_matches</code>.
Lay your T/F cards out in all four combinations and fill in a truth table. Find the row where <b>the wrong person gets in</b>. Fix the rule.</p>""",
 "Write the truth table for the trainee's OR rule and circle every row whose result is dangerous.",
 "Why do both failure paths in the flowchart show the <i>same</i> message, \"Invalid email or password\"? (Think like an attacker.)",
 "Hint: OR is true when at least one part is true. Answers → Feedback Corner, Mission 1.2.")}

{fig("../../assets/topic01-login-flowchart.png", "Figure 1.1 The login decision. Each diamond is one Boolean test with exactly two exits. Only YES + YES reaches \"Access granted\".", "62%")}

{mission("1.3", "Keep the caravanserai warm (write your own rule)", "15 min",
 "Write a complete algorithm containing one IF–THEN–ELSE rule, and test its <b>boundary</b>.",
 "Mission 1.2 done. Pen and paper.",
 """<p>The caravanserai has a smart thermostat with a temperature sensor and a heater switch.</p>
<ol><li><b>Task A:</b> write a <b>3-step algorithm</b> that turns the heater ON when the temperature is <b>below 18 °C</b>:
(1) get the input, (2) test a true/false condition, (3) act on the result with <b>one IF–THEN–ELSE rule</b>.</li>
<li><b>Task B (predict, then check):</b> what does your rule do at 15 °C, <b>18 °C</b> and 21 °C?</li>
<li><b>Task C (stretch):</b> change the rule so the heater turns on only if it is below 18 °C <b>and</b> someone is staying in the room. Write its truth table.</li></ol>""",
 "Fill in: <i>reading · condition true/false · heater</i> for 15, 18, 21 °C.",
 "Did anyone in your group get 18 °C \"wrong\"? What does that tell you about the word \"below\"?",
 "Hint: \"below 18\" means strictly less than 18. Answers → Feedback Corner, Mission 1.3.")}

{trap("""<table><tr><th>Trap</th><th>The truth</th></tr>
<tr><td>"OR means one or the other, not both."</td><td>In Boolean logic OR is true when <b>at least one</b> part is true, including both.</td></tr>
<tr><td>"The computer understands what a password is."</td><td>It only compares two stored pieces of data and gets true or false. Meaning comes from the people who wrote the rules.</td></tr>
<tr><td>"Pseudocode is a programming language."</td><td>Pseudocode is plain-language steps used to plan an algorithm. It cannot be run.</td></tr>
<tr><td>"Close enough is fine for a computer."</td><td>"Below 18" and "18 or below" are different rules. One character changes the behaviour.</td></tr></table>""")}

{check("""<ol><li>Is a phone's camera app hardware or software? The lens?</li>
<li>Why is "turn the heater on if it's chilly" a bad instruction for a computer?</li>
<li><code>has_ticket = True</code>, <code>ticket_expired = True</code>. What is <code>has_ticket AND NOT ticket_expired</code>?</li>
<li>A café gives a discount to students <b>or</b> people over 65. Does a 70-year-old student get it?</li></ol>""")}

{feedback_corner("""
<p><b>Predict box.</b> "Looks bad" is not a true/false condition. BEK cannot measure "bad". A machine-ready version: <code>IF wind_speed &gt; 40 km/h THEN close gate</code>.</p>
<p><b>Mission 1.1 (expected outcome).</b> Most first-round failures come from missing <b>sizes</b> ("draw a square": how big?), <b>positions</b> ("put a triangle on top": where exactly?),
<b>order</b>, and vague words. Second-round instructions usually work better because they add numbers, a start point and a clear order.
That is what an <b>algorithm</b> is: finite, clear, ordered steps. A computer, like BEK, cannot fill gaps.</p>
<p><b>Mission 1.2.</b> Part A: Aziz → granted; Bekzod → denied; stranger → denied (step 1 fails, so step 2 is never reached).
Part B: the trainee's OR rule gives <b>True</b> when the account exists but the password is wrong:
<b>anyone who types a real user's email gets in with any password.</b> Correct rule: <code>access = account_exists AND password_matches</code>.
Reflection: one generic message stops attackers from learning which email addresses have accounts; this is recommended practice
<span class="small">(OWASP Authentication Cheat Sheet)</span>.</p>
<p><b>Mission 1.3.</b> Task A: <code>T = read sensor</code> → test <code>T &lt; 18</code> → <code>IF T &lt; 18 THEN heater = ON ELSE heater = OFF</code>.
Task B: 15 °C → ON; <b>18 °C → OFF</b> (18 is not less than 18); 21 °C → OFF. Writing <code>T &lt;= 18</code> changes the rule.
Task C: <code>IF (T &lt; 18) AND (someone_staying) THEN ON ELSE OFF</code>; the only ON row is True/True.
Common mistakes: skipping the input step; vague words such as "cold"; forgetting the ELSE.</p>
<p><b>Checkpoint.</b> 1: app = software, lens = hardware. 2: "chilly" has no exact true/false meaning; use <code>T &lt; 18</code>.
3: <code>NOT True</code> = False, so <code>True AND False</code> = <b>False</b>. 4: <b>Yes</b>: OR is true when at least one part is true (here both).</p>""")}

{postcard("""<p><b>Greetings from Khiva!</b> BEK learned that a machine does <b>exactly</b> what it is told. Decisions are <b>Boolean conditions</b>
(true/false) joined with <b>AND / OR / NOT</b>, written as <b>IF–THEN–ELSE rules</b> and checked with <b>truth tables</b>.
Next stop: what happens when you give BEK <i>hundreds</i> of rules?</p>""")}
"""
