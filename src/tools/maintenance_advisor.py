class MaintenanceAdvisor:

    # =========================================================
    # INITIALIZATION
    # =========================================================

    def __init__(self):

        self.recommendations = {

            "Hydraulic System": [

                "Inspect hydraulic fluid level.",
                "Inspect hydraulic pumps.",
                "Inspect hydraulic reservoir.",
                "Inspect hydraulic lines for leakage.",
                "Inspect control actuators.",
                "Verify hydraulic pressure.",
                "Check hydraulic filters."

            ],

            "Engine System": [

                "Inspect compressor blades.",
                "Inspect turbine section.",
                "Check engine oil level.",
                "Inspect fuel delivery system.",
                "Verify engine sensors."

            ],

            "Fuel System": [

                "Inspect fuel pumps.",
                "Inspect fuel tanks.",
                "Inspect filters.",
                "Verify fuel pressure.",
                "Inspect fuel valves."

            ],

            "Electrical System": [

                "Inspect generators.",
                "Inspect battery health.",
                "Inspect wiring harnesses.",
                "Verify electrical buses.",
                "Inspect circuit breakers."

            ]

        }

    # =========================================================
    # GET RECOMMENDATIONS
    # =========================================================

    def recommend(
        self,
        classification
    ):

        system = classification["system"]

        return self.recommendations.get(

            system,

            [

                "Perform general aircraft inspection."

            ]

        )