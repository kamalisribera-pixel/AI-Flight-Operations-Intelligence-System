class RiskAssessor:


    def assess(
        self,
        classification
    ):

        system = classification["system"]


        risks = {

            "Hydraulic System": {
                "severity": "Critical",
                "impact":
                    "Possible loss of flight control.",
                "priority":
                    "Immediate inspection required."
            },

            "Engine System": {
                "severity": "Critical",
                "impact":
                    "Possible thrust loss.",
                "priority":
                    "Land as soon as practical."
            },

            "Fuel System": {
                "severity": "High",
                "impact":
                    "Fuel starvation possible.",
                "priority":
                    "Inspect fuel delivery."
            },

            "Electrical System": {
                "severity": "Medium",
                "impact":
                    "Loss of avionics possible.",
                "priority":
                    "Inspect electrical buses."
            }

        }


        return risks.get(

            system,

            {

                "severity": "Unknown",
                "impact": "Unknown",
                "priority": "Further analysis required."

            }

        )