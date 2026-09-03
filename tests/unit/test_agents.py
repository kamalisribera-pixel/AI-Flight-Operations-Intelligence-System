from src.services.agent_service import AgentService


class FakeAgent:
    def run(self, question):
        return "analysis"


def test_agent_service_delegates_analysis():
    assert AgentService(agent=FakeAgent()).analyze("failure") == "analysis"