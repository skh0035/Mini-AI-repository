"""Small HTML helpers so every stop uses the same identity (boxes, characters, missions)."""

NAMES = {"bek": "BEK the rule-robot", "toti": "To'ti the parrot", "nodira": "Navigator Nodira"}


def say(who, text):
    return (f'<div class="say {who}"><svg viewBox="0 0 100 110"><use href="#{who}"/></svg>'
            f'<div class="bubble"><span class="who">{NAMES[who]}</span>{text}</div></div>')


def box(kind, label, html, extra=""):
    return f'<div class="box {kind} {extra}"><span class="label">{label}</span>{html}</div>'


def tale(html):
    return box("tale", "🐪 Caravan tale (story, not a technical claim)", html)


def real(title, html):
    return box("real allow-break", f"🧭 The real thing: {title}", html)


def predict(html):
    return box("predict", "🔮 Predict first", html)


def trap(html):
    return box("trap", "⚠️ Traps on the road (common misunderstandings)", html)


def check(html):
    return box("check", "✅ Checkpoint (answers in the Feedback Corner)", html)


def postcard(html):
    return box("postcard", "📮 Postcard from this stop", html)


def watch(title, who, url, why, part, do, careful):
    return box("watch", "🎬 Watch / explore", f"""
<p><b>{title}</b> by {who}<br><a href="{url}">{url}</a></p>
<table><tr><th style="width:24mm">Why use it?</th><td>{why}</td></tr>
<tr><th>Which part?</th><td>{part}</td></tr>
<tr><th>Your task</th><td>{do}</td></tr>
<tr><th>Watch out</th><td>{careful}</td></tr></table>""")


def mission(num, title, time, goal, prep, task, observe, reflect, feedback):
    rows = [("Goal", goal, ""), ("Preparation", prep, ""), ("Task", task, ""),
            ("Observation", observe, ""), ("Reflection", reflect, ""), ("Feedback", feedback, "fb")]
    body = "".join(f'<div class="row {c}"><div class="k">{k}</div><div class="v">{v}</div></div>' for k, v, c in rows)
    return (f'<div class="mission"><div class="mhead"><span class="num">{num}</span>{title}'
            f'<span class="time">⏱ {time}</span></div>{body}</div>')


def lab(title, html):
    return box("lab allow-break", f"🧪 Lab: {title}", html)


def feedback_corner(html):
    return f'<h2>🗝️ Feedback Corner</h2><p class="small">Try everything first. Then check here: every answer explains <i>why</i>.</p>{html}'


def stop_head(n, city, title, question, meta, mascot="bek"):
    return (f'<div class="stop-head" id="stop{n}"><svg class="mascot" viewBox="0 0 100 110"><use href="#{mascot}"/></svg>'
            f'<div class="kicker">Stop {n} · {city}</div><h1>{title}</h1>'
            f'<div class="q">{question}</div><div class="meta">{meta}</div></div>')


def fig(src, cap, width="100%"):
    return f'<figure><img src="{src}" style="width:{width}"><figcaption>{cap}</figcaption></figure>'
