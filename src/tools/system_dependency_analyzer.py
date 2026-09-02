class SystemDependencyAnalyzer:

    # =========================================================
    # INITIALIZATION
    # =========================================================

    def __init__(self):

        self.dependencies = {

            "Hydraulic System": [

                "Hydraulic Pump",
                "Hydraulic Reservoir",
                "Hydraulic Pressure",
                "Flight Control Actuators",
                "Ailerons",
                "Elevator",
                "Rudder",
                "Aircraft Controllability"

            ],

            "Engine System": [

                "Fuel System",
                "Compressor",
                "Combustion Chamber",
                "Turbine",
                "Engine Thrust",
                "Aircraft Performance"

            ],

            "Fuel System": [

                "Fuel Tank",
                "Fuel Pump",
                "Fuel Lines",
                "Engine",
                "Aircraft Thrust"

            ],

            "Electrical System": [

                "Battery",
                "Generator",
                "Electrical Bus",
                "Avionics",
                "Flight Instruments"

            ]

        }

    # =========================================================
    # ANALYZE
    # =========================================================

    def analyze(
        self,
        classification
    ):

        return self.dependencies.get(

            classification["system"],

            []

        )