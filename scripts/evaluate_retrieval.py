from src.retrieval.retriever import AerospaceRetriever



TEST_CASES = [

    {
        "question": 
        "What happens when an aircraft loses hydraulic pressure?",

        "expected_keywords": [
            "hydraulic",
            "pressure",
            "system"
        ]
    },


    {
        "question":
        "How does an aircraft generate lift?",

        "expected_keywords": [
            "lift",
            "wing",
            "airflow"
        ]
    },


    {
        "question":
        "What causes compressor stall in aircraft engines?",

        "expected_keywords": [
            "compressor",
            "stall",
            "engine"
        ]
    },


    {
        "question":
        "Explain aircraft stability.",

        "expected_keywords": [
            "stability",
            "control",
            "aircraft"
        ]
    },


    {
        "question":
        "How does an aircraft fuel system work?",

        "expected_keywords": [
            "fuel",
            "tank",
            "engine"
        ]
    }

]



def evaluate():


    print("="*60)
    print("AI_FOIS RETRIEVAL EVALUATION")
    print("="*60)



    retriever = AerospaceRetriever()


    total_score = 0



    for index, case in enumerate(TEST_CASES):


        print(
            f"\nTEST {index+1}"
        )


        print(
            "Question:",
            case["question"]
        )



        results = retriever.retrieve(
            case["question"],
            top_k=5
        )



        retrieved_text = " ".join(

            results["documents"][0]

        ).lower()



        matched = 0


        for keyword in case["expected_keywords"]:

            if keyword.lower() in retrieved_text:

                matched += 1



        score = (

            matched /

            len(case["expected_keywords"])

        )


        total_score += score



        print(
            f"Score: {score:.2f}"
        )


        print(
            "Retrieved:",
            results["metadatas"][0][0]
        )



    final_score = (

        total_score /

        len(TEST_CASES)

    )


    print("\n")
    print("="*60)

    print(
        f"Average Retrieval Score: {final_score:.2f}"
    )

    print("="*60)




if __name__ == "__main__":

    evaluate()