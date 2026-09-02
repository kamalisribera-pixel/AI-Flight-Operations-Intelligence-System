class FlightImpactAnalyzer:

    # =========================================================
    # INITIALIZATION
    # =========================================================

    def __init__(self):

        self.impacts = {

            "Hydraulic System": [

                "Reduced hydraulic pressure.",
                "Reduced actuator effectiveness.",
                "Reduced control surface authority.",
                "Reduced aircraft maneuverability.",
                "Possible emergency landing."

            ],

            "Engine System": [

                "Reduced engine thrust.",
                "Decreased aircraft performance.",
                "Possible engine shutdown.",
                "Possible forced landing."

            ],

            "Fuel System": [

                "Interrupted fuel supply.",
                "Engine power loss.",
                "Possible engine flameout.",
                "Reduced aircraft endurance."

            ],

            "Electrical System": [

                "Loss of avionics.",
                "Reduced cockpit instrumentation.",
                "Navigation degradation.",
                "Communication degradation."

            ]

        }

    # =========================================================
    # ANALYZE
    # =========================================================

    def analyze(
        self,
        classification
    ):

        return self.impacts.get(

            classification["system"],

            [

                "Unknown operational impact."

            ]

        )