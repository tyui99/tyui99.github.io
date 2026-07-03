from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable

W, H = A4

def hr():
    return HRFlowable(width="100%", thickness=0.5, color=HexColor("#cccccc"), spaceAfter=6, spaceBefore=4)

styles = getSampleStyleSheet()

name_style = ParagraphStyle('Name', parent=styles['Title'], fontSize=20, leading=24, spaceAfter=2, alignment=TA_CENTER)
contact_style = ParagraphStyle('Contact', parent=styles['Normal'], fontSize=9, leading=12, alignment=TA_CENTER, textColor=HexColor("#555555"))
section_style = ParagraphStyle('Section', parent=styles['Heading2'], fontSize=12, leading=16, spaceBefore=14, spaceAfter=4, textColor=HexColor("#1a56db"))
sub_style = ParagraphStyle('Sub', parent=styles['Normal'], fontSize=10.5, leading=14, spaceAfter=1)
body_style = ParagraphStyle('Body', parent=styles['Normal'], fontSize=9.5, leading=13, textColor=HexColor("#333333"), leftIndent=8)
bullet_style = ParagraphStyle('Bullet', parent=body_style, leftIndent=16, bulletIndent=8, spaceBefore=0, spaceAfter=1)

doc = SimpleDocTemplate(
    "files/Jiachi_ZHANG_CV.pdf",
    pagesize=A4,
    leftMargin=22*mm, rightMargin=22*mm,
    topMargin=20*mm, bottomMargin=20*mm
)

story = []

# Header
story.append(Paragraph("Jingzhi Zhang (Jiachi ZHANG)", name_style))
story.append(Paragraph("Tel: +86 15816658985 &nbsp;|&nbsp; Email: jingzhizhang569@gmail.com &nbsp;|&nbsp; GitHub: github.com/tyui99 &nbsp;|&nbsp; <font color='#1a56db'>tyui99.github.io</font>", contact_style))
story.append(Spacer(1, 10))

# Research Interests
story.append(Paragraph("RESEARCH INTERESTS", section_style))
story.append(hr())
story.append(Paragraph("Efficient AI, Model Compression &amp; Acceleration, Medical Image Analysis, Prediction-Space Learning, Brain-Computer Interface", body_style))

# Education
story.append(Paragraph("EDUCATION", section_style))
story.append(hr())
story.append(Paragraph("<b>South China University of Technology</b> &nbsp;|&nbsp; 09/2023–06/2027", sub_style))
story.append(Paragraph("B.Eng. in Information Engineering &nbsp;|&nbsp; Average Score: 84.52/100", body_style))
story.append(Paragraph("Core Courses: Signals &amp; Systems, Analog Electronics, Digital Electronics, Digital Signal Processing, Principle of Communications, Microcomputer System and Interface Technology, Programming in C++", body_style))
story.append(Spacer(1, 6))
story.append(Paragraph("<b>&Eacute;cole Polytechnique de l'Universit&eacute; de Nantes, France</b> &nbsp;|&nbsp; 07/2025", sub_style))
story.append(Paragraph("Summer Study Program &nbsp;|&nbsp; Fran&ccedil;ais, Th&eacute;orie de l'Information", body_style))

# Internship
story.append(Paragraph("INTERNSHIP EXPERIENCE", section_style))
story.append(hr())
story.append(Paragraph("<b>Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences</b> &nbsp;|&nbsp; 10/2025–Present", sub_style))
story.append(Paragraph("Visiting Research Intern &nbsp;|&nbsp; Advisors: Dr. Wenqi Fang &amp; PhD candidate Zhuoyu Wu", body_style))
for line in [
    "Conducted independent research by identifying research gaps, developing hypotheses, designing experimental protocols, and performing hands-on experiments and data analysis.",
    "Authored and revised two first-author manuscripts submitted to ICONIP 2026 and APSIPA ASC 2026.",
    "Compiled academic materials by reviewing relevant literature and drafting concise, structured experimental summaries."
]:
    story.append(Paragraph("&bull; " + line, bullet_style))

# Publications
story.append(Paragraph("PUBLICATIONS &amp; RESEARCH", section_style))
story.append(hr())

story.append(Paragraph("<b>Gain-Aware Prediction-Space Recursive Controller for Lightweight Polyp Segmentation</b>", sub_style))
story.append(Paragraph("<i>Submitted to ICONIP 2026</i> &nbsp;|&nbsp; <b>Jingzhi Zhang (Jiachi ZHANG)</b> et al.", body_style))
for line in [
    "Formulated segmentation refinement as prediction-space recursive correction with only <b>189 parameters</b> and negligible GMACs overhead.",
    "Designed a three-stage recursive controller: Evidence Encoding, Gain-Aware State Update, State-Guided Residual Correction.",
    "Evaluated across <b>7 lightweight backbones</b> on 4 datasets, consistently outperforming training-side baselines (+LL/+DS/+Mutation/+LoMix) and +Harmonizing."
]:
    story.append(Paragraph("&bull; " + line, bullet_style))

story.append(Spacer(1, 8))

story.append(Paragraph("<b>RIGS-Refiner: Risk-Guided Recursive Refinement in Prediction Space for Polyp Segmentation</b>", sub_style))
story.append(Paragraph("<i>Submitted to APSIPA ASC 2026</i> &nbsp;|&nbsp; <b>Jingzhi Zhang (Jiachi ZHANG)</b> et al.", body_style))
for line in [
    "Proposed a lightweight post-refinement plugin with <b>519 parameters</b> combining image priors, prediction cues, risk-guided update, and residual correction.",
    "Tested on PraNet and SegFormer-B0 across 4 datasets, achieving favorable efficiency–accuracy trade-offs against SegFix, rNCA, and CascadePSP (&times;2600 parameter reduction)."
]:
    story.append(Paragraph("&bull; " + line, bullet_style))

story.append(Spacer(1, 8))

story.append(Paragraph("<b>Glomerular Pathological Image Detection via YOLO11 with Stain Normalization</b>", sub_style))
story.append(Paragraph("04/2024–03/2025", body_style))
story.append(Paragraph("&bull; Designed color clustering and transfer modules to mitigate staining variance; built YOLO11-based detection framework with EMA attention and Focal Loss, achieving 94% mAP.", bullet_style))

# Projects
story.append(Paragraph("PROJECT EXPERIENCE", section_style))
story.append(hr())
story.append(Paragraph("<b>Macroeconomic Indicator Forecasting via SAITS and Time-Series LLMs</b> &nbsp;|&nbsp; 07/2025–08/2025", sub_style))
story.append(Paragraph("&bull; Built multivariate time-series imputation and forecasting system; integrated TimeLLM and ChatTS with cross-modal alignment. <b>Top 10</b> in E Fund FinTech Challenge.", bullet_style))

story.append(Spacer(1, 6))
story.append(Paragraph("<b>FPGA-Based Shooting Confrontation Game</b> &nbsp;|&nbsp; 03/2026", sub_style))
story.append(Paragraph("&bull; Developed dual-mode FPGA game with 1280&times;800@60fps HDMI output, infrared control, AABB collision detection, and 7-state FSM. <b>Excellent Course Design Award</b>.", bullet_style))

# Honors
story.append(Paragraph("HONORS &amp; AWARDS", section_style))
story.append(hr())
honors = [
    "3rd Prize Scholarship, South China University of Technology (2025)",
    "Merit Student, South China University of Technology (2025)",
    "Advanced Individual in Student Work, SCUT (2025)",
    "10th Place, Pazhou Algorithm Competition — E Fund Cup FinTech Challenge (2025)",
    "Outstanding League Cadre, SCUT (2025)",
    "Excellent Course Design Award, SCUT (2026)"
]
for h in honors:
    story.append(Paragraph("&bull; " + h, bullet_style))

# Skills
story.append(Paragraph("ADDITIONAL SKILLS", section_style))
story.append(hr())
story.append(Paragraph("<b>Languages:</b> French (basic), English (fluent, can be used as a studying language)", body_style))
story.append(Paragraph("<b>Programming:</b> Python, PyTorch, Keil, MATLAB, Vivado", body_style))

doc.build(story)
print("PDF created successfully.")
