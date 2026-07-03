"""
Rewrite the user's CV using the new template's visual style
(Times New Roman, 16pt name, 13pt section headers, 12pt body,
bold headers, italic field labels) with the CURRENT CV's content.

Strategy: open the new template DOCX, clear its body, then re-add
paragraphs preserving Times New Roman as the default font.

Output:
  - files/Jiachi_ZHANG_CV.docx
  - files/Jiachi_ZHANG_CV.pdf
"""

import os
from copy import deepcopy
from docx import Document
from docx.shared import Pt
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

SRC_DOCX = "/Users/zjc/Documents/个人资料/主页/Jiachi ZHANG-CV(6).docx"
OUT_DOCX = "/Users/zjc/Documents/个人资料/主页/files/Jiachi_ZHANG_CV.docx"
OUT_PDF  = "/Users/zjc/Documents/个人资料/主页/files/Jiachi_ZHANG_CV.pdf"

# ----- Content -----
NAME = "Jiachi ZHANG"
CONTACT = ("Tel: +86 15816658985     Email: jingzhizhang569@gmail.com     "
           "GitHub: github.com/tyui99     Web: tyui99.github.io     "
           "Google Scholar: scholar.google.com/citations?user=4BDSTP8AAAAJ&hl=en")

# (header, [(kind, text), ...])
# kind: "bold" (12pt bold sub), "italic" (12pt bold italic), "body" (12pt), "blank" (spacer)
SECTIONS = [
    ("EDUCATION", [
        ("bold",   "South China University of Technology                                          09/2023 - 06/2027"),
        ("italic", "Qualification:        Bachelor of Engineering"),
        ("italic", "Major:                Information Engineering"),
        ("italic", "Average Score:        84.52/100"),
        ("italic", "Core Courses:        Signals & Systems, Analog Electronics, Digital Electronics, Digital Signal Processing, Principle of Communications, Microcomputer System and Interface Technology, Programming in C++"),
    ]),
    ("SUMMER STUDY PROGRAM", [
        ("bold",   "École Polytechnique de l'Université de Nantes, France                              07/2025"),
        ("italic", "Core Courses:        Français, Théorie de l'Information"),
    ]),
    ("INTERNSHIP EXPERIENCE", [
        ("bold", "Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences    10/2025 - Present"),
        ("body", "Position: Visiting Research Intern (Advisors: Dr. Wenqi Fang & PhD candidate Zhuoyu Wu)"),
        ("body", "Carried out independent research by identifying research gaps, developing research hypotheses, designing experimental protocols, and conducting hands-on experiments and data analysis."),
        ("body", "Compiled academic materials by reviewing relevant literature and drafting concise and structured experimental summaries."),
        ("body", "Authored and revised the thesis, ensuring a clear, logically rigorous scientific narrative grounded in experimental results."),
    ]),
    ("PUBLICATIONS & RESEARCH", [
        ("bold",  "Gain-Aware Prediction-Space Recursive Controller for Lightweight Polyp Segmentation        09/2025 - Present"),
        ("body",  "Submitted to ICONIP 2026."),
        ("body",  "Formulated segmentation refinement as a prediction-space recursive correction task, shifting correction entirely into logit space to avoid re-engaging heavy feature hierarchies."),
        ("body",  "Designed a three-stage recursive controller (Prediction Evidence Encoding → Gain-Aware State Update → State-Guided Residual Correction) with only 189 parameters and negligible GMACs overhead."),
        ("body",  "Evaluated across 7 lightweight backbones (UltraLBM-UNet, Mobile-PolypNet, EGE-UNet, CGNet, ULite, CMUNeXt-S, I2U-Net) on 4 polyp segmentation datasets under a unified Kvasir-trained protocol."),
        ("body",  "Achieved consistent source-domain improvements and competitive performance against both training-side baselines (+LL/+DS/+Mutation/+LoMix) and the heavier structural refiner +Harmonizing."),
        ("blank",),
        ("bold",  "RIGS-Refiner: Risk-Guided Recursive Refinement in Prediction Space for Polyp Segmentation      10/2025 - Present"),
        ("body",  "Submitted to APSIPA ASC 2026."),
        ("body",  "Proposed a lightweight post-refinement plugin for risk-guided recursive correction directly in prediction space, built on frozen host predictions."),
        ("body",  "Designed a shared recursive cell combining image priors (Sobel edge, average pooling), prediction cues, risk-guided update, and residual correction with only 519 parameters and +0.631 GFLOPs."),
        ("body",  "Tested on PraNet and SegFormer-B0 across Kvasir-SEG, ClinicDB, ColonDB, and ETIS, achieving consistent IoU/HD95/clDice improvements with a favorable efficiency–accuracy trade-off against SegFix, rNCA, and CascadePSP."),
        ("blank",),
        ("bold",  "Glomerular Pathological Image Detection via YOLO11 with Stain Normalization                    04/2024 - 03/2025"),
        ("body",  "Designed color clustering and color transfer modules to mitigate staining variance and augment glomerular pathological image datasets."),
        ("body",  "Constructed a YOLO11-based detection framework and adopted Focal Loss to balance positive-and-negative samples in the glomerular detection task."),
        ("body",  "Integrated EMA multi-scale attention to enhance feature fusion and suppress tissue noise; validated via ablation experiments, achieving 94% mAP that outperformed baseline models."),
    ]),
    ("PROJECT EXPERIENCE", [
        ("bold",  "Macroeconomic Indicator Forecasting System via SAITS and Time-Series LLMs          07/2025 - 08/2025"),
        ("body",  "Adopted the SAITS algorithm to conduct multivariate time-series imputation, and reconstructed high-fidelity continuous feature spaces under limited labeled data."),
        ("body",  "Integrated TimeLLM and ChatTS, designed cross-modal alignment modules to capture temporal evolution trends and enhance prediction accuracy."),
        ("body",  "Constructed a modular training and evaluation system, and developed high-precision interpretable time-series models, securing top 10 in the E Fund FinTech Challenge."),
        ("blank",),
        ("bold",  "FPGA-Based Shooting Confrontation Game                                                              03/2026"),
        ("body",  "Developed a dual-mode FPGA shooting game supporting 1280×800@60fps HDMI output, infrared control and real-time score display."),
        ("body",  "Designed HDMI display drivers and SDRAM caching logic, and implemented AABB-based collision detection for game objects."),
        ("body",  "Used finite state machines to control seven game states and ensure synchronization between peripherals and display modules."),
        ("body",  "Completed project validation and received the Excellent Course Design award for outstanding academic performance."),
    ]),
    ("EXTRACURRICULAR EXPERIENCE", [
        ("bold",  "President, Art Troupe, Youth League Committee                                          11/2024 - 11/2025"),
        ("body",  "Participated in the production and singing of the department song, and performed in the college band on various occasions."),
        ("body",  "Managed and coordinated internal departmental affairs, and took charge of the college graduation gala as a key organizer for multiple times."),
        ("blank",),
        ("bold",  "Study Representative, Class Committee                                                    09/2023 - 10/2025"),
        ("body",  "Collected and distributed daily assignments, and completed the liaison work for academic affairs."),
        ("body",  "Communicated actively between teachers and classmates, and released official university notifications in a timely manner."),
    ]),
    ("HONORS & AWARDS", [
        ("bold", "3rd Prize Scholarship, South China University of Technology                                          12/2025"),
        ("bold", "Merit Student, South China University of Technology                                                    12/2025"),
        ("bold", "Advanced Individual in Student Work, South China University of Technology                            09/2025"),
        ("bold", "Active Participant in Student Work, South China University of Technology                              09/2025"),
        ("bold", "10th Place, Pazhou Algorithm Competition - E Fund Cup FinTech Challenge                              08/2025"),
        ("bold", "Outstanding League Cadre, South China University of Technology                                       05/2025"),
    ]),
    ("ADDITIONAL SKILLS", [
        ("bold", "Language Ability:        French (basic), English (fluent, can be used as a studying language)"),
        ("bold", "Programming & Development: Python, PyTorch, Keil, MATLAB, Vivado"),
    ]),
]


# ===================== DOCX =====================
def set_run_font(run, name="Times New Roman", size_pt=12.0, bold=False, italic=False):
    run.font.name = name
    run.font.size = Pt(size_pt)
    run.font.bold = bold
    run.font.italic = italic
    # Force East Asian / complex script to also use Times New Roman
    rPr = run._element.get_or_add_rPr()
    rFonts = rPr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = OxmlElement('w:rFonts')
        rPr.insert(0, rFonts)
    rFonts.set(qn('w:ascii'), name)
    rFonts.set(qn('w:hAnsi'), name)
    rFonts.set(qn('w:cs'), name)
    rFonts.set(qn('w:eastAsia'), name)


def add_para(doc, text, *, size_pt=12.0, bold=False, italic=False, alignment=None, space_after=None):
    p = doc.add_paragraph()
    if alignment is not None:
        p.alignment = alignment
    if space_after is not None:
        p.paragraph_format.space_after = Pt(space_after)
    if text:
        run = p.add_run(text)
        set_run_font(run, size_pt=size_pt, bold=bold, italic=italic)
    return p


# Open template and clear all existing body paragraphs (keep the document defaults)
doc = Document(SRC_DOCX)
body = doc.element.body
# Remove all <w:p> elements except sectPr (which defines page layout)
for child in list(body):
    if child.tag == qn('w:p'):
        body.remove(child)

# Set default font on Normal style to Times New Roman 12pt
normal = doc.styles['Normal']
normal.font.name = 'Times New Roman'
normal.font.size = Pt(12)

# --- Build content ---
add_para(doc, NAME, size_pt=16.0, bold=True, alignment=1)  # 1 = WD_ALIGN_PARAGRAPH.CENTER
add_para(doc, CONTACT, size_pt=12.0, bold=True, alignment=1, space_after=10)

for header, items in SECTIONS:
    add_para(doc, header, size_pt=13.0, bold=True, space_after=4)
    for kind, *rest in items:
        if kind == "blank":
            add_para(doc, "", size_pt=6)
        else:
            text = rest[0]
            if kind == "bold":
                add_para(doc, text, size_pt=12.0, bold=True, space_after=1)
            elif kind == "italic":
                add_para(doc, text, size_pt=12.0, bold=True, italic=True, space_after=1)
            elif kind == "body":
                add_para(doc, text, size_pt=12.0, bold=False, space_after=1)

os.makedirs(os.path.dirname(OUT_DOCX), exist_ok=True)
doc.save(OUT_DOCX)
print(f"DOCX saved -> {OUT_DOCX}")


# ===================== PDF (reportlab, matching style) =====================
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

name_style     = ParagraphStyle('Name',     fontName='Times-Bold',      fontSize=16, leading=20, alignment=TA_CENTER, spaceAfter=4)
contact_style  = ParagraphStyle('Contact',  fontName='Times-Bold',      fontSize=12, leading=15, alignment=TA_CENTER, spaceAfter=10)
section_style  = ParagraphStyle('Section',  fontName='Times-Bold',      fontSize=13, leading=16, spaceBefore=10, spaceAfter=4)
sub_style      = ParagraphStyle('Sub',      fontName='Times-Bold',      fontSize=12, leading=15, spaceBefore=4, spaceAfter=1)
italic_style   = ParagraphStyle('Italic',   fontName='Times-BoldItalic',fontSize=12, leading=15, spaceAfter=1)
body_style     = ParagraphStyle('Body',     fontName='Times-Roman',     fontSize=12, leading=15, spaceAfter=1)

doc_pdf = SimpleDocTemplate(
    OUT_PDF,
    pagesize=A4,
    leftMargin=22*mm, rightMargin=22*mm,
    topMargin=20*mm, bottomMargin=20*mm,
)

def xe(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

story = []
story.append(Paragraph(xe(NAME), name_style))
story.append(Paragraph(xe(CONTACT), contact_style))
for header, items in SECTIONS:
    story.append(Paragraph(xe(header), section_style))
    for kind, *rest in items:
        text = rest[0] if rest else ""
        if kind == "blank":
            story.append(Spacer(1, 6))
        elif kind == "bold":
            story.append(Paragraph(xe(text), sub_style))
        elif kind == "italic":
            story.append(Paragraph(xe(text), italic_style))
        elif kind == "body":
            story.append(Paragraph(xe(text), body_style))

doc_pdf.build(story)
print(f"PDF  saved -> {OUT_PDF}")
