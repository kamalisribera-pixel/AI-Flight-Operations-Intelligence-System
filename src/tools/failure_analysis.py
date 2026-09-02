class FailureAnalysisTool:


    def __init__(
        self,
        retriever
    ):

        self.retriever = retriever



    def analyze(
        self,
        failure_description,
        classification
    ):


        query = f"""
        Aircraft failure scenario:

        {failure_description}

        Find:
        - Aircraft system involved
        - Possible causes
        - Effects
        - Relevant procedures
        """


        results = self.retriever.retrieve(
            query,
            top_k=5
        )


        return {
            "failure": failure_description,
            "classification": classification,
            "documents": results["documents"][0],
            "metadata": results["metadatas"][0]
        }