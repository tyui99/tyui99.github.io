from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, KeepTogether

W, H = A4

def hr():
    return HRFlowable(width="100%", thickness=0.5, color=HexColor("#0000FF"), spaceAfter=4, spaceBefore=2)

styles = getSampleStyleSheet()

# Minimal professional style based on new template (Times New Roman, blue accent #0000FF)
name_style = ParagraphStyle('Name', parent=styles['Title'], fontName='Times-Bold', fontSize=22, leading=26, spaceAfter=2, alignment=TA_CENTER)
contact_style = ParagraphStyle('Contact', parent=styles['Normal'], fontName='Times-Roman', fontSize=10, leading=12, alignment=TA_CENTER, textColor=HexColor("#000000"))
section_style = ParagraphStyle('Section', parent=styles['Heading2'], fontName='Times-Bold', fontSize=12.5, leading=16, spaceBefore=12, spaceAfter=2, textColor=HexColor("#0000FF"))
sub_style = ParagraphStyle('Sub', parent=styles['Normal'], fontName='Times-Bold', fontSize=10.5, leading=14, spaceAfter=1)
body_style = ParagraphStyle('Body', parent=styles['Normal'], fontName='Times-Roman', fontSize=10, leading=13.5, textColor=HexColor("#000000"), leftIndent=10)
bullet_style = ParagraphStyle('Bullet', parent=body_style, fontName='Times-Roman', leftIndent=18, bulletIndent=8, spaceBefore=0, spaceAfter=2)
entry_header_style = ParagraphStyle('Entry', parent=styles['Normal'], fontName='Times-Bold', fontSize=10.5, leading=14, spaceAfter=1, spaceBefore=4)

doc = SimpleDocTemplate(
    "files/Jiachi_ZHANG_CV.pdf",
    pagesize=A4,
    leftMargin=22*mm, rightMargin=22*mm,
    topMargin=18*mm, bottomMargin=18*mm
)

story = []

# Header
story.append(Paragraph("Jiachi ZHANG", name_style))
story.append(Paragraph("Tel: +86 15816658985 &nbsp;&nbsp;|&nbsp;&nbsp; Email: 15816658985@163.com &nbsp;&nbsp;|&nbsp;&nbsp; Homepage: <font color='#0000FF'>tyui99.github.io</font>", contact_style))
story.append(Spacer(1, 8))

# Education
story.append(Paragraph("EDUCATION", section_style))
story.append(hr())
edu = [
    ("South China University of Technology", "09/2023 – 06/2027"),
]
for school, period in edu:
    story.append(Paragraph(f"<b>{school}</b> <font color='#0000FF'>............................................................</font> {period}", entry_header_style))
story.append(Paragraph("Qualification: Bachelor of Engineering", body_style))
story.append(Paragraph("Major: Information Engineering", body_style))
story.append(Paragraph("Average Score: 84.52/100", body_style))
story.append(Paragraph("Core Courses: Signals &amp; Systems, Analog Electronics, Digital Electronics, Digital Signal Processing, Principle of Communications, Microcomputer System and Interface Technology, Programming in C++", body_style))

story.append(Spacer(1, 4))
story.append(Paragraph("SUMMER STUDY PROGRAM", section_style))
story.append(hr())
story.append(Paragraph("<b>&Eacute;cole Polytechnique de l'Universit&eacute; de Nantes, France</b> <font color='#0000FF'>................................</font> 07/2025", entry_header_style))
story.append(Paragraph("Core Courses: Fran&ccedil;ais, Th&eacute;orie de l'Information", body_style))

# Internship
story.append(Paragraph("INTERNSHIP EXPERIENCE", section_style))
story.append(hr())
story.append(Paragraph("<b>Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences</b> <font color='#0000FF'>.......</font> 10/2025 – Present", entry_header_style))
story.append(Paragraph("Position: Visiting Research Intern &nbsp;|&nbsp; Advisors: Dr. Wenqi Fang &amp; PhD candidate Zhuoyu Wu", body_style))
for line in [
    "Carried out independent research by identifying research gaps, developing research hypotheses, designing experimental protocols, and conducting hands-on experiments and data analysis.",
    "Compiled academic materials by reviewing relevant literature and drafting concise and structured experimental summaries.",
    "Authored and revised the thesis, ensuring a clear, logically rigorous scientific narrative grounded in experimental results."
]:
    story.append(Paragraph("&bull; " + line, bullet_style))

# Research Experience (new section from updated CV)
story.append(Paragraph("RESEARCH EXPERIENCE", section_style))
story.append(hr())

story.append(Paragraph("<b>Efficient Medical Image Segmentation via Recursive Parameter Reuse</b> <font color='#0000FF'>.............</font> 09/2025 – Present", entry_header_style))
for line in [
    "Studied medical image segmentation efficiency under extreme parameter scales, and adopted recursive parameter reuse to preserve segmentation fidelity with minimal parameter consumption.",
    "Built a multi-granularity recursive lightweight model family, enabling the <b>1.3K-parameter</b> model to attain over <b>0.71 mean Dice</b> and <b>21,009&times; parameter efficiency</b> against U-Net (work under review at <i>ACM Multimedia 2026</i>).",
    "Designed a plug-and-play recursive refinement module with only <b>~0.00019M parameters</b> and zero static computation, raising the Dice score by over <b>1.3 percentage points</b> (work under review at <i>ICONIP 2026</i>).",
    "Boosted incremental parameter efficiency by <b>four orders of magnitude</b> over conventional segmentation refinement blocks, with negligible memory and latency overhead."
]:
    story.append(Paragraph("&bull; " + line, bullet_style))

story.append(Spacer(1, 6))
story.append(Paragraph("<b>Deep Learning-based Glomerular Pathological Image Detection</b> <font color='#0000FF'>.................</font> 04/2024 – 03/2025", entry_header_style))
for line in [
    "Designed color clustering and color transfer modules to mitigate staining variance and augment glomerular pathological image datasets.",
    "Constructed a YOLO11-based detection framework effectively and adopted Focal Loss to balance positive-and-negative samples in the glomerular detection task.",
    "Integrated EMA multi-scale attention to enhance feature fusion and suppress tissue noise; validated via ablation, achieving <b>94% mAP</b>, outperforming baseline models."
]:
    story.append(Paragraph("&bull; " + line, bullet_style))

# Project Experience
story.append(Paragraph("PROJECT EXPERIENCE", section_style))
story.append(hr())
story.append(Paragraph("<b>Macroeconomic Indicator Forecasting System via SAITS and Time-Series LLMs</b> <font color='#0000FF'>.....</font> 07/2025 – 08/2025", entry_header_style))
for line in [
    "Adopted the SAITS algorithm for multivariate time-series imputation, reconstructing high-fidelity continuous feature spaces under limited labeled data.",
    "Integrated TimeLLM and ChatTS, designed cross-modal alignment modules to capture temporal evolution trends and enhance prediction accuracy.",
    "Constructed a modular training and evaluation system; <b>Top 10</b> in the E Fund FinTech Challenge."
]:
    story.append(Paragraph("&bull; " + line, bullet_style))

story.append(Spacer(1, 4))
story.append(Paragraph("<b>FPGA-Based Shooting Confrontation Game</b> <font color='#0000FF'>....................................</font> 03/2026", entry_header_style))
for line in [
    "Developed a dual-mode FPGA shooting game supporting 1280&times;800@60fps HDMI output, infrared control, and real-time score display.",
    "Designed HDMI display drivers and SDRAM caching logic; implemented AABB-based collision detection for game objects.",
    "Used finite state machines to control seven game states; received the <b>Excellent Course Design Award</b>."
]:
    story.append(Paragraph("&bull; " + line, bullet_style))

# Extracurricular
story.append(Paragraph("EXTRACURRICULAR EXPERIENCE", section_style))
story.append(hr())
story.append(Paragraph("<b>President, Art Troupe, Youth League Committee</b> <font color='#0000FF'>.....................................</font> 11/2024 – 11/2025", entry_header_style))
for line in [
    "Participated in the production and singing of the department song; performed in the college band on various occasions.",
    "Managed departmental affairs; key organizer of the college graduation gala for multiple years."
]:
    story.append(Paragraph("&bull; " + line, bullet_style))

story.append(Spacer(1, 4))
story.append(Paragraph("<b>Study Representative, Class Committee</b> <font color='#0000FF'>.............................................</font> 09/2023 – 10/2025", entry_header_style))
for line in [
    "Collected and distributed daily assignments; completed the liaison work for academic affairs.",
    "Communicated actively between teachers and classmates; released official university notifications in a timely manner."
]:
    story.append(Paragraph("&bull; " + line, bullet_style))

# Honors
story.append(Paragraph("HONORS &amp; AWARDS", section_style))
story.append(hr())
honors = [
    ("3rd Prize Scholarship, South China University of Technology", "12/2025"),
    ("Merit Student, South China University of Technology", "12/2025"),
    ("Advanced Individual in Student Work, SCUT", "09/2025"),
    ("Active Participant in Student Work, SCUT", "09/2025"),
    ("10th Place, Pazhou Algorithm Competition — E Fund Cup FinTech Challenge", "08/2025"),
    ("Outstanding League Cadre, SCUT", "05/2025"),
]
for h, d in honors:
    story.append(Paragraph(f"&bull; {h} <font color='#0000FF'>{('.' * max(2, 95 - len(h)))}</font> {d}", bullet_style))

# Skills
story.append(Paragraph("ADDITIONAL SKILLS", section_style))
story.append(hr())
story.append(Paragraph("<b>Language Ability:</b> French (basic), English (fluent, can be used as a studying language)", body_style))
story.append(Paragraph("<b>Programming &amp; Development:</b> Python, PyTorch, Keil, MATLAB, Vivado", body_style))

doc.build(story)
print("PDF created successfully.")
