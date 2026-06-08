from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

pdf = SimpleDocTemplate("analysis_report.pdf")
styles = getSampleStyleSheet()

content = [
    Paragraph("Electrical Circuit Analysis Report", styles["Title"]),
    Paragraph("Ohm's Law Analysis", styles["Heading2"]),
    Paragraph("Voltage = 12 V, Resistance = 6 Ω, Current = 2 A", styles["BodyText"])
]

pdf.build(content)