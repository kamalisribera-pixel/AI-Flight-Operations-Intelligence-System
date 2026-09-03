from config.logging_config import logger

from src.agents.aerospace_agent import AerospaceAgent
from src.exceptions import AgentError, ValidationError
from src.generation.llm_engine import AerospaceLLMEngine
from src.retrieval.retriever import AerospaceRetriever


class AgentService:

    def __init__(self, agent=None, retriever=None, llm=None):

        if agent is not None:
            self.agent = agent
            return

        retriever = retriever or AerospaceRetriever()
        llm = llm or AerospaceLLMEngine()

        self.agent = AerospaceAgent(
            retriever,
            llm
        )

    def analyze(self, question):

        if not question or not question.strip():
            raise ValidationError(
                "Please provide a failure description."
            )

        try:
            return self.agent.run(question)

        except Exception as error:

            logger.exception(
                "Engineering agent analysis failed."
            )

            raise AgentError(
                "Unable to complete the engineering analysis."
            ) from error