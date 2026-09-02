class FailureClassifier:


    def classify(
        self,
        description
    ):

        text = description.lower()


        if "hydraulic" in text:

            return {
                "system": "Hydraulic System",
                "keywords": [
                    "hydraulic",
                    "actuator",
                    "pressure",
                    "pump",
                    "fluid"
                ]
            }


        if "engine" in text:

            return {
                "system": "Engine System",
                "keywords": [
                    "compressor",
                    "stall",
                    "fuel",
                    "turbine"
                ]
            }


        return {
            "system": "Unknown",
            "keywords": []
        }