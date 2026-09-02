class FailureReportGenerator:

    # =========================================================
    # GENERATE REPORT
    # =========================================================

    def generate(
        self,
        failure,
        classification,
        risk,
        maintenance,
        analysis
    ):

        maintenance_text = "\n".join(
            f"• {item}"
            for item in maintenance
        )

        report = f"""
============================================================
AI_FOIS FAILURE ANALYSIS REPORT
============================================================

Failure Scenario
----------------
{failure}

Detected System
---------------
{classification["system"]}

Risk Assessment
---------------
Severity : {risk["severity"]}

Operational Impact
------------------
{risk["impact"]}

Recommended Action
------------------
{risk["priority"]}

Maintenance Recommendations
---------------------------
{maintenance_text}

Engineering Analysis
--------------------
{analysis}

============================================================
END OF REPORT
============================================================
"""

        return report