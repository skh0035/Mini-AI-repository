from kit import *

GENUINE = ["Your order of twenty silk scarves will arrive on Tuesday", "Can we meet at the bazaar at noon to agree the price",
           "The camel caravan is delayed by one day because of a sandstorm", "Thank you for your payment, here is your receipt",
           "Please bring the spice samples to my shop tomorrow", "We have new carpets from Bukhara, visit us this week",
           "Your room at the caravanserai is booked for three nights", "The market closes early on Friday for the festival"]
SCAM = ["Congratulations you have won a free camel, click this link now", "URGENT your account is locked, send your password today",
        "You are selected for a secret gold prize, pay a small fee to claim", "Cheap silk 90 percent off only today, send money first",
        "Final warning: your parcel is held, pay the release fee now", "Click here to claim free gold coins, limited time",
        "Your bank details are needed to receive your inheritance", "Win win win, act now, free prize waiting"]
TESTS = ["Free tea tasting at our shop on Friday", "Your parcel from Samarkand will arrive tomorrow", "Send your password to unlock your prize",
         "Please confirm the meeting time for the silk delivery", "CONGRATULATIONS", "The weather in Kashgar is sunny"]


def _ol(items):
    return "<ol>" + "".join(f"<li>{x}</li>" for x in items) + "</ol>"


STOP3 = stop_head(3, "Samarkand", "To'ti's Market",
    "What if nobody writes the rules, and the machine works them out from examples?",
    "Markdown source: <code>03-symbolic-ai-vs-machine-learning.md</code> · Outcome LO5 · ≈ 65 min · Missions 3.1–3.2 · Lab 3 (Machine Learning for Kids)", "toti") + f"""

{tale("""<p>Samarkand's Siyob Bazaar is loud and busy, and so is the merchants' message board. Mixed in with real trade offers are scams.
BEK writes rules: <code>IF message contains "FREE MONEY" THEN scam</code>. By lunchtime the scammers are writing "FR3E M0NEY" and BEK's rule catches nothing.</p>
<p>To'ti the parrot has watched the merchants all morning. Nobody gave him rules, but he has seen hundreds of messages and heard
which ones the merchants called "scam". He starts squawking at suspicious messages, and he is mostly right.</p>""")}
{say("toti", "I don't know any rules. I just noticed that scams tend to have lots of links. Seen it before!")}
{say("nodira", "To'ti is doing <b>machine learning</b>: instead of a person writing the rule, the rule is <b>chosen from labelled examples</b>. Let's do exactly what he did, by hand.")}

{predict("""<p>You will see ten messages, each with its number of links and a label (scam / not). To'ti may learn one rule: <code>IF links ≥ k THEN scam</code>.
Guess now: which <b>k</b> will make the fewest mistakes? Will the best rule be perfect?</p><div class="writein"></div>""")}

{mission("3.1", "Teach To'ti: learn a rule from data", "20 min",
 "See what <b>training</b> means: try possible rules, count mistakes on <b>labelled data</b>, keep the best one. Then see how new data changes the <b>model</b>.",
 "Message cards A–J and N (Appendix A), a pencil as the \"threshold marker\", or just the table below.",
 """<table><tr><th>Message</th><th>A</th><th>B</th><th>C</th><th>D</th><th>E</th><th>F</th><th>G</th><th>H</th><th>I</th><th>J</th></tr>
<tr><td>Links</td><td>0</td><td>1</td><td>1</td><td>2</td><td>3</td><td>2</td><td>4</td><td>5</td><td>6</td><td>8</td></tr>
<tr><td>Label</td><td>not</td><td>not</td><td>not</td><td>not</td><td>not</td><td><b>scam</b></td><td><b>scam</b></td><td><b>scam</b></td><td><b>scam</b></td><td><b>scam</b></td></tr></table>
<ol><li>Lay the cards in a line, sorted by number of links.</li>
<li>Place the pencil just before the cards with <b>k = 2</b> links: every card from the pencil onwards is predicted "scam". Count the mistakes (wrong in <i>either</i> direction).</li>
<li>Repeat for every k from 0 to 9. Choose the k with the fewest mistakes: that is your <b>model</b>.</li>
<li><b>Predict</b> three new messages: K (7 links), L (0 links), M (3 links).</li>
<li><b>Retrain:</b> a new labelled card arrives: <b>N, 3 links, scam</b>. Add it and recount for k = 2, 3, 4 and 5.</li></ol>""",
 """<table><tr><th>k</th><th>0</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th></tr>
<tr><td>Mistakes (10 cards)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>Mistakes (11 cards, with N)</td><td>–</td><td>–</td><td></td><td></td><td></td><td></td><td>–</td><td>–</td><td>–</td><td>–</td></tr></table>""",
 """<p>Was your Predict-box guess right? Is the best rule perfect? Who "wrote" the number k? What happened after card N arrived?
A classmate says: <i>"It made only 1 mistake in 10, so it will be 90% right on every future message."</i> What is wrong with that claim?</p>""",
 "Hint: check message F carefully. Full table and explanation → Feedback Corner, Mission 3.1. Optional check: <code>supporting-files/examples/topic03_learn_a_rule.py</code>.")}

{real("machine learning in a nutshell", """
<p><b>Machine learning (ML)</b> is a branch of AI in which software learns patterns from data, instead of following rules a programmer wrote
in advance <span class="small">(Britannica: Machine learning; IBM Developer)</span>.</p>
<table><tr><th>Term</th><th>Meaning</th><th>In Mission 3.1</th></tr>
<tr><td>Labelled data</td><td>Examples that come with the correct answer</td><td>10 cards marked scam / not</td></tr>
<tr><td>Feature</td><td>A measurable property the program may use</td><td>number of links</td></tr>
<tr><td>Training</td><td>Searching for the pattern that best fits the labelled data</td><td>counting mistakes for each k</td></tr>
<tr><td>Model</td><td>The result of training: a learned "rule"</td><td><code>IF links ≥ 4 THEN scam</code></td></tr>
<tr><td>Prediction</td><td>The model's answer for a new example</td><td>K → scam</td></tr></table>
<p>Real models use thousands of features and millions of examples, and their learned "rule" is stored as huge numbers of values.
That is why they are flexible but hard to explain, even though the core idea is the one you just did by hand.</p>""")}
{fig("../../assets/topic03-rules-vs-learning.png", "Figure 3.1 Two ways to give a computer knowledge: people write the rules (BEK), or training finds them in labelled examples (To'ti).", "78%")}

{lab("3 · Train a scam detector (Machine Learning for Kids)", f"""
<p><b>Goal.</b> Train a real text classifier, test it on messages it has never seen, investigate its mistakes, and improve the training data.
<b>Platform:</b> Machine Learning for Kids by Dale Lane: <a href="https://machinelearningforkids.co.uk">machinelearningforkids.co.uk</a>.
<b>Access:</b> free; choose <b>Get started → Try it now</b> to work without an account. A Cloudflare <b>"Verify you are human"</b> box appears first: tick it yourself.
"Try it now" projects are temporary, so finish in one session. Button names below follow the site's own worksheets; small wording differences are possible.</p>
<h3>Steps</h3>
<ol><li><b>+ Add a new project</b> → name <code>Caravan messages</code> → type <b>recognising text</b> → <b>Create</b>. Open the project → <b>Train</b>.</li>
<li><b>+ Add new label</b> twice: <code>genuine</code> and <code>scam</code>.</li>
<li>Use <b>+ Add example</b> to type these 16 training messages into the right labels:</li></ol>
<div class="two"><div><b>genuine</b>{_ol(GENUINE)}</div><div><b>scam</b>{_ol(SCAM)}</div></div>
<ol start="4"><li><b>&lt; Back to project</b> → <b>Learn &amp; Test</b> → <b>Train new machine learning model</b>. Wait until training finishes (it can take a few minutes).</li>
<li>Type each <b>test message</b> into the test box, one at a time. Record the label and how confident the model says it is.</li></ol>
<table><tr><th>#</th><th>Test message (never seen in training)</th><th>Your prediction</th><th>Model says</th><th>Right?</th></tr>
{"".join(f"<tr><td>T{i+1}</td><td>{t}</td><td></td><td></td><td></td></tr>" for i, t in enumerate(TESTS))}</table>
<h3>Investigate</h3>
<ol><li>Which test messages did the model get wrong? For each, find the <b>words</b> it shares with the training examples of the other label.</li>
<li>Improve the data: add <b>three</b> genuine messages that contain "free", "parcel" or "prize" in an honest way (e.g. <i>"Free delivery for orders over ten carpets"</i>). Retrain and retest T1 and T2.</li>
<li>T6 is about the weather: neither genuine trade nor scam. What does the model do with a message unlike anything it has seen?</li>
<li>Could BEK have written rules for this? Which would be easier to keep up to date when scammers change their words?</li></ol>
<p><b>Fallback</b> (no access, blocked site, or the human check fails): open the notebook <code>SilkMind_Labs.ipynb</code>, <b>Part 3</b>. It trains a tiny
word-counting scam detector on exactly these 16 messages and tests T1–T6, so you can answer every Investigate question offline. It is much simpler than
Machine Learning for Kids, so its answers can differ; the Feedback Corner explains both.</p>""")}

{watch("How AI Actually Learns (first published as \"How Machines Learn\")", "CGP Grey (YouTube, 8 min 54 s, December 2017)", "https://www.youtube.com/watch?v=R9OHn5ZF4Uo",
 "A funny, animated explanation of why people stopped writing every rule by hand for big problems, and how \"teacher bots\" test \"student bots\" against an answer key.",
 "Watch from the start to about <b>7:20</b>. From 0:16: why hand-written if-this-then-that bots don't scale. The middle section: builder bots, teacher bots and tests. <b>5:12</b>: why more data means better tests.",
 "Compare: the teacher bot's answer key ↔ our labels; keeping the best student ↔ keeping the k with fewest mistakes. Write one similarity and one difference.",
 "The builder/teacher-bot story is a <b>simplified analogy</b>. Grey's own follow-up video, <i>How AI, Like ChatGPT, *Really* Learns</i>, explains that most real systems are trained by gradually adjusting numbers (gradient descent), not by breeding bots. No YouTube? Mission 3.1 covers the same idea.")}

{mission("3.2", "BEK or To'ti? Choose the right tool", "10 min",
 "Compare symbolic AI and ML and <b>justify</b> a choice using clear criteria.",
 "The comparison table below.",
 """<p>For each job, decide: <b>BEK</b> (rules), <b>To'ti</b> (learning) or <b>both</b>. Then argue it out with a partner who must disagree.</p>
<ol><li>Checking whether a student meets a course's published entry grades.</li>
<li>Recognising which animal is in a photo.</li>
<li>Calculating a delivery fee from a published price list.</li>
<li>Recommending songs from what millions of users have played.</li>
<li>A hospital system that reads X-ray images <b>and</b> must flag any result breaking a fixed safety guideline.</li></ol>""",
 "Record your choice and a reason for each, using a criterion from the table.",
 "Which criterion decided most of your choices?",
 "Answers → Feedback Corner, Mission 3.2.")}
<table><tr><th>Question</th><th>BEK: symbolic AI</th><th>To'ti: machine learning</th></tr>
<tr><td>Where does knowledge come from?</td><td>People write rules</td><td>Patterns in labelled data</td></tr>
<tr><td>Needs to start</td><td>Experts who can state rules</td><td>Enough good, labelled data</td></tr>
<tr><td>Can it explain an answer?</td><td><b>Yes</b>: it lists the rules that fired</td><td>Often difficult at real-world scale</td></tr>
<tr><td>Unusual case</td><td>Fails if no rule covers it (brittle)</td><td>May cope if similar examples existed; may be confidently wrong</td></tr>
<tr><td>Updating</td><td>Edit rules by hand</td><td>Collect data and retrain</td></tr></table>

{trap("""<table><tr><th>Trap</th><th>The truth</th></tr>
<tr><td>"ML means the computer understands."</td><td>In Mission 3.1 the program never knew what a link or a scam is. It reduced mistakes.</td></tr>
<tr><td>"A model trained on real data is always right."</td><td>Our best model still gets F wrong, and a model is only as good as its data.</td></tr>
<tr><td>"ML doesn't use rules."</td><td>A model <i>is</i> a kind of rule (ours literally is). The difference is <b>who writes it</b>.</td></tr>
<tr><td>"Symbolic AI has been replaced."</td><td>Rules are still used wherever exact, explainable decisions are required (Stop 5).</td></tr></table>""")}

{check("""<ol><li>What is a <b>label</b>? Give an example from Mission 3.1.</li>
<li>How many training mistakes does <code>IF links ≥ 5 THEN scam</code> make, and which messages?</li>
<li>Why did adding message N change the best rule?</li>
<li>A bank must explain every loan refusal using its published criteria. BEK or To'ti? Why?</li></ol>""")}

{feedback_corner("""
<p><b>Mission 3.1.</b> Mistakes for k = 0…9: <b>5, 4, 2, 2, 1, 2, 3, 4, 4, 5</b>. Best: <b>k = 4</b> with 1 mistake (message F: 2 links but scam).
So the model is <code>IF links ≥ 4 THEN scam</code>. It is <b>not</b> perfect, and nobody wrote the number 4: the data chose it.
Predictions: K → scam, L → not, M → not. With N (3 links, scam) added: k = 2 → 2 mistakes (D, E); k = 3 → 2 (E, F); k = 4 → 2 (F, N); k = 5 → 3 (F, G, N).
Now k = 2, 3 and 4 <b>tie</b>: one new example changed the model, and training needs a tie-break rule (our program picks the smallest k).
The "90% on every future message" claim is wrong: the 1-in-10 was measured on the <b>same</b> messages used to choose k, and 10 examples are far too few.
Real accuracy must be measured on <b>new labelled messages not used in training</b>. (All numbers checked with <code>topic03_learn_a_rule.py</code>.)</p>
<p><b>Lab 3 (expected outcomes).</b> Every training run starts fresh, so your exact results and confidence values can differ from a classmate's.
The model learns which <b>words</b> go with which label. Watch especially <b>T1</b> ("Free tea tasting…") and <b>T2</b> ("Your parcel…"): they are genuine but share words
(<i>free</i>, <i>parcel</i>) with the scam examples, so the model may call them scam. <b>T3</b> and <b>T5</b> share many scam words and are likely to be labelled scam.
<b>T6</b> is unlike every example; the model must still pick one of its two labels. It cannot say "neither", which shows that a model only knows the
categories it was trained on. Adding honest examples containing "free"/"parcel"/"prize" and retraining usually moves T1/T2 towards <i>genuine</i>:
better data, better model. BEK's word rules would need constant hand-editing as scammers change spelling; retraining on new labelled messages is easier to keep up to date,
but harder to explain.</p>
<p><b>Offline version (notebook Part 3, our run):</b> T1 genuine, T2 genuine, T3 scam, T4 genuine, T5 scam, <b>T6 genuine</b>. T6 is called genuine only because it contains
<i>the</i> and <i>is</i>, words that appeared more often in genuine training messages. The model learned "the = genuine", an accident of a small data set.
A model learns whatever patterns are in its data, sensible or not.</p>
<p><b>Mission 3.2.</b> 1 BEK: explicit published rules; must be explainable. 2 To'ti: no one can write rules for every photo. 3 BEK: exact price list.
4 To'ti: patterns too complex to write; plenty of data. 5 Both: ML reads images; the fixed guideline is a rule that must be checked and explained.
Accept other answers that use a criterion from the table.</p>
<p><b>Checkpoint.</b> 1: the correct answer attached to an example, e.g. message F → "scam". 2: <b>2</b> (F and G: both scam with fewer than 5 links).
3: the model depends on the data; N made several thresholds equally good. 4: <b>BEK</b>: published criteria and a required explanation.</p>""")}

{postcard("""<p><b>Greetings from Samarkand!</b> To'ti showed that a computer can <b>learn</b> a rule: try options, count mistakes on <b>labelled data</b>, keep the best.
The result is a <b>model</b>: flexible, but imperfect, data-hungry and harder to explain. BEK writes rules; To'ti learns them. Next stop: the ruins
where people stopped believing in BEK…</p>""")}
"""
