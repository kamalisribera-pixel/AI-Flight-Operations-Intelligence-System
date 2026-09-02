class TroubleshootingAgent:

    # =========================================================
    # INITIALIZATION
    # =========================================================

    def __init__(self):

        self.procedures = {

            "Hydraulic System": [

                "Check hydraulic fluid level.",
                "Inspect hydraulic reservoir.",
                "Inspect hydraulic pumps.",
                "Inspect hydraulic lines for leakage.",
                "Inspect hydraulic actuators.",
                "Verify hydraulic pressure.",
                "Perform operational control check."

            ],

            "Engine System": [

                "Inspect compressor section.",
                "Inspect turbine blades.",
                "Verify fuel flow.",
                "Check oil pressure.",
                "Perform engine run-up."

            ],

            "Fuel System": [

                "Inspect fuel pumps.",
                "Inspect fuel lines.",
                "Verify fuel pressure.",
                "Inspect filters.",
                "Check fuel quantity."

            ],

            "Electrical System": [

                "Inspect battery.",
                "Inspect generators.",
                "Check circuit breakers.",
                "Verify electrical buses.",
                "Test avionics."

            ]

        }

    # =========================================================
    # GENERATE PROCEDURE
    # =========================================================

    def troubleshoot(
        self,
        classification
    ):

        return self.procedures.get(

            classification["system"],

            [

                "Perform general aircraft inspection."

            ]

        )