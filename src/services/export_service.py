from src.exports.markdown_exporter import MarkdownExporter
from src.exports.json_exporter import JSONExporter
from src.exports.pdf_exporter import PDFExporter


class ExportService:
    """Coordinates engineering report exports."""

    def __init__(self):
        self._markdown = MarkdownExporter()
        self._json = JSONExporter()
        self._pdf = PDFExporter()

    def export(self, report: dict, export_format: str):
        export_format = export_format.lower()

        if export_format == "markdown":
            return self._markdown.export(report)

        if export_format == "json":
            return self._json.export(report)

        if export_format == "pdf":
            return self._pdf.export(report)

        raise ValueError(f"Unsupported export format: {export_format}")