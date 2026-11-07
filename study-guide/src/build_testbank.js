// Builds SilkMind_Caravan_Test_Bank_V1.0.docx  (run: node build_testbank.js)
const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell, WidthType, ShadingType,
  AlignmentType, PageBreak, BorderStyle, Footer, PageNumber, TableOfContents, LevelFormat,
} = require("docx");
const { TF, MC, OE } = require("./testbank_data");

const NAVY = "1F3A5F", AMBER = "B07A1E", GREEN = "2E7D32", GREY = "55606F";
const W = 9638; // A4 content width in DXA with 2 cm margins
const font = "Calibri";

const P = (text, o = {}) => new Paragraph({ spacing: { after: o.after ?? 100 }, ...o.p, children: Array.isArray(text) ? text : [new TextRun({ text, ...o.r })] });
const R = (text, o = {}) => new TextRun({ text, ...o });
const H1 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_1, spacing: { before: 240, after: 120 }, children: [R(t)] });
const H2 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_2, spacing: { before: 200, after: 100 }, children: [R(t)] });
const tag = (s) => R(`  [${s}]`, { color: GREY, italics: true, size: 18 });
const rule = () => new Paragraph({ border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "C9D2DE", space: 1 } }, spacing: { after: 120 }, children: [] });

function table(widths, rows, headerFill = "E8EEF7") {
  return new Table({
    width: { size: W, type: WidthType.DXA }, columnWidths: widths,
    rows: rows.map((cells, ri) => new TableRow({
      tableHeader: ri === 0,
      children: cells.map((c, ci) => new TableCell({
        width: { size: widths[ci], type: WidthType.DXA },
        shading: ri === 0 ? { type: ShadingType.CLEAR, color: "auto", fill: headerFill } : undefined,
        margins: { top: 50, bottom: 50, left: 90, right: 90 },
        children: [new Paragraph({ children: [R(String(c), { bold: ri === 0, size: 19, color: ri === 0 ? NAVY : undefined })] })],
      })),
    })),
  });
}

const L = ["a", "b", "c", "d"];
const children = [];

// ---------- title block ----------
children.push(
  P([R("The SilkMind Caravan", { bold: true, size: 48, color: NAVY, font: "Georgia" })], { after: 40 }),
  P([R("Test Bank V1.0 · Software & Symbolic AI", { bold: true, size: 30, color: AMBER })], { after: 80 }),
  P([R("Team SilkMind · Stage 2 · November 2026 · Companion to the Study Guide V1.0 (built from Markdown Content V2.0)", { size: 19, color: GREY })], { after: 160 }),
  rule(),
  P([R("How to use this test bank. ", { bold: true }), R("Questions come first; the answer key with explanations starts at Part D. Every question shows the guide section it tests in [brackets], e.g. [S2 · Mission 2.1] = Stop 2, Mission 2.1. All data needed (rules, tables) is on the Reference Sheet, so no website is needed. Multiple-choice questions say whether to choose ONE answer or ALL that apply.")]),
  table([2400, 1400, 5838], [
    ["Part", "Questions", "What it checks"],
    ["A · True / False", `${TF.length}`, "Meaningful understanding; false statements are corrected in the key"],
    ["B · Multiple choice", `${MC.length}`, "Applying ideas: traces, predictions, finding errors"],
    ["C · Open-ended", `${OE.length}`, "Explaining, comparing, evaluating (aim for 120–250 words or worked steps)"],
    ["D · Answer key", "–", "Answers, explanations, expected key points and sample answers"],
  ]),
  P(""),
);

// ---------- coverage ----------
const secOf = (s) => s.slice(0, 2);
const cov = ["S1", "S2", "S3", "S4", "S5"].map((s) => [
  { S1: "Stop 1 · Software & logic (LO1–2)", S2: "Stop 2 · Rules & inference, Labs 2A/2B (LO3–4)", S3: "Stop 3 · Machine learning, Lab 3 (LO5)", S4: "Stop 4 · History & AI winters (LO6)", S5: "Stop 5 · Modern software, Lab 5 (LO7)" }[s],
  TF.filter((q) => secOf(q[0]) === s).length, MC.filter((q) => secOf(q[0]) === s).length, OE.filter((q) => secOf(q[0]) === s).length]);
children.push(H2("Coverage"), table([4838, 1600, 1600, 1600], [["Guide stop (learning outcomes)", "True/False", "Multiple choice", "Open-ended"], ...cov]));

// ---------- reference sheet ----------
children.push(new Paragraph({ children: [new PageBreak()] }), H1("Reference Sheet"),
  P("Use these exactly as in the Study Guide."),
  H2("Rules R1–R6 (Stop 2)"),
  table([900, 5638, 3100], [["Rule", "IF …", "THEN …"], ["R1", "has feathers", "is a bird"], ["R2", "gives milk", "is a mammal"],
    ["R3", "is a bird AND cannot fly AND swims", "is a penguin"], ["R4", "is a bird AND can fly AND hunts at night", "is an owl"],
    ["R5", "is a mammal AND eats meat AND has black stripes", "is a tiger"], ["R6", "is a mammal AND has hooves AND has black stripes", "is a zebra"]]),
  P("Forward chaining: in each cycle, check R1→R6 in order and fire the first rule whose IF part is completely in working memory and whose THEN fact is new; stop when a cycle adds nothing.", { r: { size: 19 } }),
  H2("Training messages (Stop 3, Mission 3.1)"),
  table([2038, 760, 760, 760, 760, 760, 760, 760, 760, 760, 760],
    [["Message", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"], ["Links", "0", "1", "1", "2", "3", "2", "4", "5", "6", "8"],
     ["Label", "not", "not", "not", "not", "not", "scam", "scam", "scam", "scam", "scam"]]),
  P("Model shape: IF links ≥ k THEN scam ELSE not. Extra message for retraining: N, 3 links, scam.", { r: { size: 19 } }),
  H2("Guard rules G1–G4 (Stop 5)"),
  table([900, 2900, 3000, 2838], [["Rule", "IF current state is …", "AND …", "THEN new state"], ["G1", "Wander", "player is seen", "Attack"],
    ["G2", "Attack", "health is low", "Flee"], ["G3", "Attack", "no player is present", "Wander"], ["G4", "Flee", "no player is present", "Wander"]]),
  P("If no rule matches, the character stays in its current state.", { r: { size: 19 } }),
);

// ---------- Part A ----------
children.push(new Paragraph({ children: [new PageBreak()] }), H1("Part A · True / False"), P("Write T or F. In the key, every false statement is corrected."));
TF.forEach((q, i) => children.push(P([R(`TF-${String(i + 1).padStart(2, "0")}  `, { bold: true, color: NAVY }), R(q[1]), tag(q[0]), R("     T / F", { bold: true, color: GREY })])));

// ---------- Part B ----------
children.push(new Paragraph({ children: [new PageBreak()] }), H1("Part B · Multiple choice"));
MC.forEach((q, i) => {
  children.push(new Paragraph({ keepNext: true, spacing: { before: 120, after: 40 }, children: [
    R(`MC-${String(i + 1).padStart(2, "0")}  `, { bold: true, color: NAVY }), R(q[2]),
    R(q[1] === "one" ? "  (Choose ONE answer.)" : "  (Choose ALL that apply.)", { bold: true, color: q[1] === "one" ? GREEN : AMBER, size: 19 }), tag(q[0])] }));
  q[3].forEach((opt, j) => children.push(new Paragraph({ keepNext: j < q[3].length - 1, indent: { left: 567 }, spacing: { after: 20 }, children: [R(`${L[j]})  `, { bold: true }), R(opt)] })));
});

// ---------- Part C ----------
children.push(new Paragraph({ children: [new PageBreak()] }), H1("Part C · Open-ended"),
  P("Answer in full sentences (normally 120–250 words), or with worked steps, tables or diagrams where asked. Use evidence from the guide's activities."));
OE.forEach((q, i) => children.push(new Paragraph({ spacing: { before: 140, after: 140 }, children: [R(`OE-${i + 1}  `, { bold: true, color: NAVY }), R(q[1]), tag(q[0])] })));

// ---------- Part D: answer key ----------
children.push(new Paragraph({ children: [new PageBreak()] }), H1("Part D · Answer key"),
  P([R("Checked by: ", { bold: true }), R("answers verified against the Study Guide Feedback Corners, the SWISH/ELIZA test runs (3 Nov 2026) and the demo programs examples/topic02_mini_rule_engine.py and topic03_learn_a_rule.py. Peer review by a second team member: see the review record at the end.")]),
  H2("A · True / False"));
children.push(table([1000, 900, 7738], [["#", "Answer", "Explanation / correction"],
  ...TF.map((q, i) => [`TF-${String(i + 1).padStart(2, "0")}`, q[2] ? "T" : "F", q[3]])]));
children.push(H2("B · Multiple choice"));
children.push(table([1000, 1100, 7538], [["#", "Answer", "Reasoning"],
  ...MC.map((q, i) => [`MC-${String(i + 1).padStart(2, "0")}`, q[4].join(", "), q[5]])]));
children.push(H2("C · Open-ended: key points and sample answers"),
  P("Award credit for any well-reasoned answer that covers most key points; sample answers show one good response, and other valid examples are accepted.", { r: { italics: true, size: 19 } }));
OE.forEach((q, i) => {
  children.push(new Paragraph({ keepNext: true, spacing: { before: 160, after: 60 }, children: [R(`OE-${i + 1}  `, { bold: true, color: NAVY }), R("Expected key points", { bold: true }), tag(q[0])] }));
  q[2].forEach((k) => children.push(new Paragraph({ numbering: { reference: "keys", level: 0 }, spacing: { after: 30 }, children: [R(k, { size: 20 })] })));
  children.push(new Paragraph({ spacing: { before: 60, after: 120 }, shading: { type: ShadingType.CLEAR, color: "auto", fill: "F2F6FB" },
    children: [R("Sample answer: ", { bold: true, color: NAVY, size: 20 }), R(q[3], { size: 20 })] }));
});

// ---------- review record ----------
children.push(H2("Review record (complete before submission)"),
  P("The brief requires another member to attempt and review every question."),
  table([2600, 2200, 1600, 3238], [["Part reviewed", "Reviewer (did not write it)", "Date", "Problems found / changes made"],
    ["A · True/False", "", "", ""], ["B · Multiple choice", "", "", ""], ["C · Open-ended", "", "", ""]]),
  P(""), P([R("AI assistance: ", { bold: true }), R("drafted with AI assistance (Claude, Anthropic) and checked against the guide and programs; see docs/ai-use-log.md.", { size: 19 })]));

const doc = new Document({
  creator: "Team SilkMind", title: "The SilkMind Caravan: Test Bank V1.0",
  styles: {
    default: { document: { run: { font, size: 21 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: "Georgia", size: 32, bold: true, color: NAVY }, paragraph: { outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: "Georgia", size: 25, bold: true, color: AMBER }, paragraph: { outlineLevel: 1 } },
    ],
  },
  numbering: { config: [{ reference: "keys", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 567, hanging: 283 } } } }] }] },
  sections: [{
    properties: { page: { margin: { top: 1134, bottom: 1134, left: 1134, right: 1134 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [R("The SilkMind Caravan · Test Bank V1.0 · page ", { size: 16, color: GREY }), new TextRun({ children: [PageNumber.CURRENT], size: 16, color: GREY })] })] }) },
    children,
  }],
});
Packer.toBuffer(doc).then((b) => { fs.writeFileSync("../SilkMind_Caravan_Test_Bank_V1.0.docx", b); console.log("TF", TF.length, "MC", MC.length, "OE", OE.length); });
