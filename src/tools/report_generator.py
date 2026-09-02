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
        troubleshooting,
        root_causes,
        dependencies,
        flight_impact,
        procedures,
        analysis
    ):

        maintenance_text = "\n".join(
            f"• {item}"
            for item in maintenance
        )

        troubleshooting_text = "\n".join(
            f"{i}. {step}"
            for i, step in enumerate(troubleshooting, start=1)
        )

        dependency_text = "\n↓\n".join(
            dependencies
        )

        impact_text = "\n↓\n".join(
            flight_impact
        )

        procedure_text = "\n".join(
            f"• {step}"
            for step in procedures
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

Troubleshooting Procedures
---------------------------
{troubleshooting_text}

Root Cause Analysis
-------------------
{root_causes}

Engineering Analysis
--------------------
{analysis}

Flight Impact Assessment
-------------------------
{impact_text}

System Dependencies
-------------------
{dependency_text}

Procedures
----------
{procedure_text}

============================================================
END OF REPORT
============================================================
"""

        return report