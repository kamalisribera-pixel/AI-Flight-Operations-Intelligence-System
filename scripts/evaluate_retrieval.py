from config.config import RETRIEVAL_TOP_K
from config.logging_config import logger
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


    logger.info("Starting retrieval evaluation")



    retriever = AerospaceRetriever()


    total_score = 0



    for index, case in enumerate(TEST_CASES):


        logger.info("Test %s: %s", index + 1, case["question"])



        results = retriever.retrieve(
            case["question"],
            top_k=RETRIEVAL_TOP_K
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



        logger.info("Score: %.2f", score)
        logger.info("Retrieved: %s", results["metadatas"][0][0])



    final_score = (

        total_score /

        len(TEST_CASES)

    )


    logger.info("Average retrieval score: %.2f", final_score)




if __name__ == "__main__":

    evaluate()
