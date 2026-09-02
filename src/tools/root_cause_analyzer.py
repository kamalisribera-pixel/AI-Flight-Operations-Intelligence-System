class RootCauseAnalyzer:

    def __init__(self):

        self.causes = {

            "Hydraulic System":[

                {
                    "cause":"Hydraulic fluid leakage",
                    "probability":"Very High"
                },

                {
                    "cause":"Hydraulic pump failure",
                    "probability":"High"
                },

                {
                    "cause":"Reservoir pressure loss",
                    "probability":"High"
                },

                {
                    "cause":"Actuator malfunction",
                    "probability":"Medium"
                },

                {
                    "cause":"Servo valve blockage",
                    "probability":"Medium"
                }

            ],

            "Engine System":[

                {
                    "cause":"Compressor stall",
                    "probability":"Very High"
                },

                {
                    "cause":"Fuel starvation",
                    "probability":"High"
                },

                {
                    "cause":"Turbine damage",
                    "probability":"Medium"
                }

            ]

        }


    def analyze(
        self,
        classification
    ):

        return self.causes.get(

            classification["system"],

            [

                {

                    "cause":"Unknown",

                    "probability":"Unknown"

                }

            ]

        )