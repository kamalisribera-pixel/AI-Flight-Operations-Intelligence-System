from src.retrieval.retriever import AerospaceRetriever
from src.generation.llm_engine import AerospaceLLMEngine
from src.agents.aerospace_agent import AerospaceAgent



def main():

    print("="*60)
    print("AI_FOIS ASSISTANT")
    print("="*60)


    question = input(
        "\nAsk aerospace question: "
    )


    retriever = AerospaceRetriever()


    llm = AerospaceLLMEngine()


    agent = AerospaceAgent(
        retriever,
        llm
    )


    answer = agent.run(
        question
    )


    print("\nAI_FOIS:")
    print(answer)



if __name__ == "__main__":
    main()