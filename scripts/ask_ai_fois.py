from src.retrieval.retriever import AerospaceRetriever
from src.generation.llm_engine import AerospaceLLMEngine



def main():

    print("="*60)
    print("AI_FOIS ASSISTANT")
    print("="*60)


    question = input(
        "\nAsk aerospace question: "
    )


    retriever = AerospaceRetriever()


    results = retriever.retrieve(
        question,
        top_k=5
    )


    context_parts = []


    for i, document in enumerate(
        results["documents"][0]
    ):

        metadata = results["metadatas"][0][i]


        context_parts.append(
            f"""
    Document:
    {metadata.get('source')}

    Page:
    {metadata.get('page_number')}

    Content:
    {document}
    """
        )


    context = "\n\n".join(
        context_parts
    )


    llm = AerospaceLLMEngine()


    answer = llm.generate(
        question,
        context
    )


    print("\nAI_FOIS:")
    print(answer)



if __name__ == "__main__":
    main()