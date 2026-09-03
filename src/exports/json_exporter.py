import json
from datetime import datetime
from src.exceptions import ExportError


class JSONExporter:
    """Exports engineering reports as JSON."""

    def export(self, report: dict) -> str:
        try:
            payload = {
                "title": report.get("title", "Engineering Report"),
                "created_at": report.get(
                    "created_at",
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ),
                "summary": report.get("summary", "N/A"),
                "recommendation": report.get("recommendation", "N/A"),
                "risk": report.get("risk", "N/A"),
                "references": report.get("references", []),
                "generated_by": "FOIS",
                "system": report.get("system", "Not specified"),
            }

            return json.dumps(payload, indent=4, ensure_ascii=False, default=str)
        except Exception as error:
            raise ExportError("Unable to export engineering report.") from error
