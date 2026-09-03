from src.generation.llm_engine import AerospaceLLMEngine
from src.exceptions import GenerationError
from config.logging_config import logger


class GenerationService:

	def __init__(self, engine=None):
		self.engine = engine or AerospaceLLMEngine()

	def generate(self, question, context):
		try:
			return self.engine.generate(question, context)
		except Exception as error:
			logger.exception("LLM generation failed")
			raise GenerationError(
				"The language model is unavailable. Check that Ollama is running."
			) from error
