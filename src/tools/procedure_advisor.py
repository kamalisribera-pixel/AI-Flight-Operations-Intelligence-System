class ProcedureAdvisor:

    # =========================================================
    # INITIALIZATION
    # =========================================================

    def __init__(self):

        self.procedures = {

            "Hydraulic System": [

                "Verify hydraulic pressure.",
                "Inspect hydraulic fluid level.",
                "Inspect hydraulic reservoir.",
                "Inspect hydraulic pumps.",
                "Inspect hydraulic lines.",
                "Inspect flight control actuators.",
                "Perform operational control check.",
                "Follow emergency hydraulic checklist if required."

            ],

            "Engine System": [

                "Verify engine indications.",
                "Inspect fuel supply.",
                "Inspect compressor section.",
                "Inspect turbine section.",
                "Perform engine run-up.",
                "Follow engine abnormal procedures."

            ],

            "Fuel System": [

                "Verify fuel quantity.",
                "Inspect fuel pumps.",
                "Inspect fuel filters.",
                "Inspect fuel lines.",
                "Perform fuel pressure test."

            ],

            "Electrical System": [

                "Verify battery voltage.",
                "Inspect generators.",
                "Inspect electrical buses.",
                "Inspect wiring.",
                "Perform avionics functional test."

            ]

        }

    # =========================================================
    # GET PROCEDURE
    # =========================================================

    def advise(
        self,
        classification
    ):

        return self.procedures.get(

            classification["system"],

            [

                "Follow standard aircraft inspection procedure."

            ]

        )