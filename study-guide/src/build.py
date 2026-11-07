"""Build the SilkMind Caravan Study Guide PDF.
Run from study-guide/src:  python3 build.py
Needs: Google Chrome/Chromium (headless printing), pypdf, reportlab.
"""
import io, os, re, subprocess
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from p0_front import COVER, WELCOME
from p1_stop1 import STOP1
from p2_stop2 import STOP2
from p3_stop3 import STOP3
from p4_stop4 import STOP4
from p5_stop5 import STOP5
from p6_back import FINALE, GLOSSARY, APPENDIX_A, TESTING, REFS

OUT = "../SilkMind_Caravan_Study_Guide_V1.0.pdf"
CHROME = os.environ.get("CHROME", "google-chrome")

# (level, label, search text used to find the page in the rendered PDF)
TOC = [
    (1, "Welcome aboard the caravan", "Welcome aboard the caravan"),
    (2, "What you need · How every stop works", "How every stop works"),
    (2, "Your route · learning goals · choose your route", "Choose your route"),
    (1, "Stop 1 · Khiva: The Gate That Says No", "How does a machine decide who may pass"),
    (2, "Mission 1.1 Be BEK: the Exact Instructions game", "the Exact Instructions game"),
    (2, "Mission 1.2 The Gatekeeper's rulebook", "The Gatekeeper's rulebook"),
    (2, "Mission 1.3 Keep the caravanserai warm", "Keep the caravanserai warm"),
    (1, "Stop 2 · Bukhara: BEK's Book of Rules", "Can a machine act like an expert"),
    (2, "Mission 2.1 Rule Cards: be the inference engine", "Rule Cards: be the inference engine"),
    (2, "Mission 2.2 Twenty Questions, rule-style", "Twenty Questions, rule-style"),
    (2, "Lab 2A BEK's rules in real Prolog (SWISH)", "rules in real Prolog"),
    (2, "Lab 2B ELIZA: rules that pretend to understand", "rules that pretend to understand"),
    (2, "Mission 2.3 Explain like the scholar", "Explain like the scholar"),
    (1, "Stop 3 · Samarkand: To'ti's Market", "What if nobody writes the rules"),
    (2, "Mission 3.1 Teach To'ti: learn a rule from data", "Teach To'ti: learn a rule from data"),
    (2, "Lab 3 Train a scam detector (Machine Learning for Kids)", "Train a scam detector"),
    (2, "Mission 3.2 BEK or To'ti? Choose the right tool", "Choose the right tool"),
    (1, "Stop 4 · Otrar: The Frozen Caravanserai", "Why did the world stop believing"),
    (2, "Mission 4.1 Timeline cards: boom or winter?", "Timeline cards: boom or winter"),
    (2, "Mission 4.2 Crack the lock", "Crack the lock"),
    (2, "Mission 4.3 The fact-checker's desk", "The fact-checker's desk"),
    (2, "Mission 4.4 It's 1985: pitch an expert system", "pitch an expert system"),
    (1, "Stop 5 · Kashgar: The Modern Bazaar", "Where are BEK's rules hiding"),
    (2, "Mission 5.1 Rule hunt: forms and apps", "Rule hunt: forms and apps"),
    (2, "Mission 5.2 Guard duty", "Guard duty (role-play"),
    (2, "Mission 5.3 The delivery-fee bug", "The delivery-fee bug"),
    (2, "Lab 5 The Silk Road knowledge graph (SWISH)", "The Silk Road knowledge graph"),
    (1, "The Grand Caravan Challenge", "Can you build your own small expert system"),
    (1, "Glossary", "One definition per term"),
    (1, "Appendix A · Printable cards", "Print this page and the next on card"),
    (1, "Appendix B · How we tested this guide", "This is our record for"),
    (1, "Resources, references and acknowledgements", "Learning platforms used in labs"),
]


def toc_html(pages=None):
    items = []
    for i, (lvl, label, _) in enumerate(TOC):
        num = f'<span class="pg">{pages[i]}</span>' if pages and pages[i] else ""
        items.append(f'<div class="lvl{lvl}"><span>{label}</span>{num}</div>')
    return '<h1>Contents</h1><div class="toc">' + "".join(items) + "</div>"


def page_html(pages=None):
    sym = open("symbols.svg.html").read()
    body = "".join([COVER, toc_html(pages), '<div class="page-break"></div>', WELCOME, STOP1, STOP2, STOP3, STOP4, STOP5,
                    FINALE, GLOSSARY, APPENDIX_A, TESTING, REFS])
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>The SilkMind Caravan: Study Guide V1.0</title>'
            f'<link rel="stylesheet" href="guide.css"></head><body>{sym}{body}</body></html>')


def render(html, pdf):
    with open("guide.html", "w", encoding="utf-8") as f:
        f.write(html)
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    "--generate-pdf-document-outline", f"--print-to-pdf={pdf}", "file://" + os.path.abspath("guide.html")],
                   check=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)


def find_pages(pdf):
    texts = [re.sub(r"\s+", " ", (p.extract_text() or "")).lower() for p in PdfReader(pdf).pages]
    out = []
    for _, label, needle in TOC:
        n = needle.lower()
        hit = next((i + 1 for i, t in enumerate(texts) if i >= 2 and n in t), None)
        out.append(hit)
        if hit is None:
            print("  ! not found in PDF:", label)
    return out


def stamp(pdf_in, pdf_out):
    reader = PdfReader(pdf_in)
    writer = PdfWriter()
    for i, page in enumerate(reader.pages):
        if i > 0:
            buf = io.BytesIO()
            c = canvas.Canvas(buf, pagesize=A4)
            c.setFont("Helvetica", 7.5)
            c.setFillColorRGB(0.35, 0.38, 0.44)
            c.drawString(42, 22, "The SilkMind Caravan · Study Guide V1.0 · Team SilkMind")
            c.drawRightString(A4[0] - 42, 22, f"{i + 1}")
            c.save()
            buf.seek(0)
            page.merge_page(PdfReader(buf).pages[0])
        writer.add_page(page)
    if reader.outline:
        pass
    writer.add_metadata({"/Title": "The SilkMind Caravan: Study Guide V1.0", "/Author": "Team SilkMind"})
    with open(pdf_out, "wb") as f:
        writer.write(f)


if __name__ == "__main__":
    render(page_html(), "_pass1.pdf")
    pages = find_pages("_pass1.pdf")
    render(page_html(pages), "_pass2.pdf")
    pages2 = find_pages("_pass2.pdf")
    if pages2 != pages:
        render(page_html(pages2), "_pass2.pdf")
    stamp("_pass2.pdf", OUT)
    print("pages:", len(PdfReader(OUT).pages), "->", OUT)
