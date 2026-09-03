from src.services.query_service import QueryService



def main():

    print("="*60)
    print("AI_FOIS ASSISTANT")
    print("="*60)


    question = input(
        "\nAsk aerospace question: "
    )


    result = QueryService().ask(question)


    print("\nAI_FOIS:")
    print(result["answer"])



if __name__ == "__main__":
    main()