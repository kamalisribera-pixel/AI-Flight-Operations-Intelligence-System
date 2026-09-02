from src.retrieval.retriever import AerospaceRetriever



def main():


    print("="*60)
    print("AI_FOIS RETRIEVAL TEST")
    print("="*60)


    retriever = AerospaceRetriever()



    query = (
        "What happens when an aircraft "
        "loses hydraulic pressure?"
    )


    results = retriever.retrieve(
        query,
        top_k=5
    )


    for i, document in enumerate(
        results["documents"][0]
    ):

        print("\nRESULT", i+1)

        print(
            document[:500]
        )


        print(
            results["metadatas"][0][i]
        )


    print("="*60)



if __name__ == "__main__":
    main()