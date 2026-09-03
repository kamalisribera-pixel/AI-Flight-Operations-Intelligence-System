from src.services.query_service import QueryService


class TestQueryPipeline:

    def test_query_pipeline(self):

        service = QueryService()

        result = service.ask(
            "Explain hydraulic pressure."
        )

        assert result is not None

        assert "answer" in result

        assert len(result["answer"]) > 0

        assert "report_id" in result