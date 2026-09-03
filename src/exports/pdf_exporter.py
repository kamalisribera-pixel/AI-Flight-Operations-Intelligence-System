from io import BytesIO

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from src.exceptions import ExportError


class PDFExporter:
    """Exports engineering reports as PDF."""

    def export(self, report: dict) -> bytes:
        try:
            buffer = BytesIO()
            doc = SimpleDocTemplate(buffer)
            styles = getSampleStyleSheet()
            story = [
                Paragraph(
                    f"<b>{report.get('system', 'Flight Operations Intelligence System')}</b>",
                    styles["Title"]
                ),
                Paragraph(str(report.get("title", "Engineering Report")), styles["Heading2"]),
                Spacer(1, 20),
                Paragraph("<b>Summary</b>", styles["Heading2"]),
                Paragraph(str(report.get("summary", "N/A")), styles["BodyText"]),
                Spacer(1, 12),
                Paragraph("<b>Recommendation</b>", styles["Heading2"]),
                Paragraph(str(report.get("recommendation", "N/A")), styles["BodyText"]),
                Spacer(1, 12),
                Paragraph("<b>Risk Assessment</b>", styles["Heading2"]),
                Paragraph(str(report.get("risk", "N/A")), styles["BodyText"]),
                Spacer(1, 12),
                Paragraph("<b>References</b>", styles["Heading2"]),
                Paragraph(
                    str(report.get("references", []) or "No references available."),
                    styles["BodyText"]
                )
            ]
            doc.build(story)
            pdf = buffer.getvalue()
            buffer.close()
            return pdf
        except Exception as error:
            raise ExportError("Unable to export engineering report.") from error