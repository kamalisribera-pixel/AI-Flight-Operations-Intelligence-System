from config.logging_config import logger

from src.exceptions import GenerationError
from src.generation.llm_engine import AerospaceLLMEngine


class GenerationService:

    def __init__(self, engine=None):
        self.engine = engine or AerospaceLLMEngine()

    def generate(self, question, context):

        try:
            return self.engine.generate(
                question,
                context
            )

        except Exception as error:

            logger.exception(
                "LLM response generation failed."
            )

            raise GenerationError(
                "Unable to generate an engineering response. "
                "Please verify that the language model service is available."
            ) from error