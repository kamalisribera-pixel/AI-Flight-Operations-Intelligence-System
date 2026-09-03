from src.agents.aerospace_agent import AerospaceAgent
from src.generation.llm_engine import AerospaceLLMEngine
from src.retrieval.retriever import AerospaceRetriever


class AgentService:

	def __init__(self, agent=None, retriever=None, llm=None):
		if agent is not None:
			self.agent = agent
			return
		retriever = retriever or AerospaceRetriever()
		llm = llm or AerospaceLLMEngine()
		self.agent = AerospaceAgent(retriever, llm)

	def analyze(self, question):
		return self.agent.run(question)
