from config.config import RETRIEVAL_TOP_K
from config.logging_config import logger
from src.retrieval.retriever import AerospaceRetriever



def main():


    logger.info("Starting retrieval test")


    retriever = AerospaceRetriever()



    query = (
        "What happens when an aircraft "
        "loses hydraulic pressure?"
    )


    results = retriever.retrieve(
        query,
        top_k=RETRIEVAL_TOP_K
    )


    for i, document in enumerate(
        results["documents"][0]
    ):

        logger.info("Result %s: %s", i + 1, document[:500])
        logger.info("Metadata: %s", results["metadatas"][0][i])



if __name__ == "__main__":
    main()
