from src.services.agent_service import AgentService


class TestAgentPipeline:

    def test_failure_analysis(self):

        service = AgentService()

        result = service.analyze(
            "Hydraulic pressure drops during landing gear extension."
        )

        assert result is not None

        assert len(result) > 0