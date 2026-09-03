class FailureReportGenerator:

    @staticmethod
    def _value(value, fallback):
        if value is None or str(value).strip().lower() in {"", "unknown", "none", "n/a"}:
            return fallback
        return str(value).strip()

    @classmethod
    def _root_cause_rows(cls, root_causes):
        if not isinstance(root_causes, (list, tuple)):
            root_causes = []

        rows = []
        for cause in root_causes:
            if isinstance(cause, dict):
                name = cls._value(cause.get("cause"), "Cause not identified")
                confidence = cls._value(
                    cause.get("probability") or cause.get("confidence"),
                    "Unavailable"
                )
            else:
                name = cls._value(cause, "Cause not identified")
                confidence = "Unavailable"
            rows.append(f"| {name} | {confidence} |")

        return rows or ["| Cause not identified from the available evidence. | Unavailable |"]

    def generate(
        self,
        failure,
        classification,
        risk,
        maintenance,
        troubleshooting,
        root_causes,
        dependencies,
        flight_impact,
        procedures,
        analysis
    ):

        system = self._value(
            (classification or {}).get("system"),
            "System could not be identified from the available evidence."
        )
        severity = self._value(
            (risk or {}).get("severity"),
            "Unable to determine."
        )
        impact = self._value(
            (risk or {}).get("impact"),
            "Operational impact could not be determined."
        )
        priority = self._value(
            (risk or {}).get("priority"),
            "No priority action identified."
        )
        return {
            "title": "Failure Analysis Report",
            "system": system,
            "failure": failure,
            "summary": self._value(analysis, "Analysis was not available."),
            "recommendation": priority,
            "risk": severity,
            "references": [],
            "operational_impact": impact,
            "maintenance": [
                self._value(item, "Review the applicable maintenance procedure.")
                for item in (maintenance or [])
            ],
            "troubleshooting": [
                self._value(step, "Follow the approved troubleshooting procedure.")
                for step in (troubleshooting or [])
            ],
            "root_causes": root_causes if isinstance(root_causes, list) else [],
            "flight_impact": [
                self._value(item, "No flight impact identified.")
                for item in (flight_impact or [])
            ],
            "dependencies": [
                self._value(item, "No dependency identified.")
                for item in (dependencies or [])
            ],
            "procedures": [
                self._value(item, "No additional procedure identified.")
                for item in (procedures or [])
            ],
        }