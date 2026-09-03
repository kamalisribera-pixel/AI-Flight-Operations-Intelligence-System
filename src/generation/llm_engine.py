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


        prompt = f"""
You are AI_FOIS, an aerospace engineering assistant.

Answer the question using ONLY the provided aerospace documents.

If the information is not available in the context,
say that you do not have enough information.

Provide a clear technical explanation.

Always cite the document name and page number when using information from the context.

Do not use information outside the provided context.

When explaining engineering concepts:
- Separate information directly stated in the document from your own interpretation.
- Do not claim the document states something unless it explicitly does.

Context:

{context}


Question:

{question}


Answer:
"""


        return prompt



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
