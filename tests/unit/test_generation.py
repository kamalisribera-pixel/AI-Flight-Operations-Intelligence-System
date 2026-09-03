from src.services.generation_service import GenerationService


class FakeEngine:
    def generate(self, question, context):
        return f"Answer: {question}"


def test_generation_service_returns_engine_response():
    assert GenerationService(FakeEngine()).generate("lift", "context") == "Answer: lift"