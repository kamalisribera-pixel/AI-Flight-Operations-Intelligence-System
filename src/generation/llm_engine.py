from config.config import LLM_MODEL_NAME, LLM_TEMPERATURE, MAX_TOKENS
from langchain_ollama import OllamaLLM



class AerospaceLLMEngine:


    def __init__(self):

        self.llm = OllamaLLM(
            model=LLM_MODEL_NAME,
            temperature=LLM_TEMPERATURE,
            num_predict=MAX_TOKENS
        )


    def build_prompt(
        self,
        question,
        context
    ):

        return f"""
    You are AI_FOIS, an aerospace engineering assistant.

    Use ONLY the provided aerospace documentation.

    If the answer cannot be found in the documents, reply:

    "Insufficient information is available in the provided documents."

    Requirements:

    - Answer in plain text.
    - DO NOT use Markdown headings (#, ##, ###).
    - DO NOT create a report.
    - DO NOT write titles.
    - DO NOT use separator lines (==== or ----).
    - Keep the response concise and technical.
    - Separate documented facts from engineering reasoning.
    - Cite the source document and page number whenever possible.

    Context:
    ----------------
    {context}

    Question:
    ----------------
    {question}

    Technical Response:
    ----------------
    """
    





    def generate(
        self,
        question,
        context
    ):

        prompt = self.build_prompt(
            question,
            context
        )


        response = self.llm.invoke(
            prompt
        )


        return response.strip()
