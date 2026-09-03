from src.services.agent_service import AgentService
from src.services.generation_service import GenerationService
from src.services.history_service import HistoryService
from src.services.report_service import ReportService
from src.services.retrieval_service import RetrievalService
from src.exceptions import AppError
from config.logging_config import logger


class QueryService:

    def __init__(
        self,
        retrieval_service=None,
        generation_service=None,
        agent_service=None,
        report_service=None,
        history_service=None
    ):
        self.retrieval_service = retrieval_service or RetrievalService()
        self.generation_service = generation_service or GenerationService()
        self.agent_service = agent_service or AgentService(
            retriever=self.retrieval_service.retriever,
            llm=self.generation_service.engine
        )
        self.report_service = report_service or ReportService()
        self.history_service = history_service or HistoryService()

    def ask(self, question):
        question = question.strip()
        if not question:
            raise ValueError("Question cannot be empty.")
        query_id = self.history_service.save_query(question)
        analysis = None

        try:
            if self.agent_service.agent.is_failure_question(question):
                analysis = self.agent_service.analyze(question)
                answer = analysis
                self.history_service.save_tool_result(
                    query_id, "AerospaceAgent", str(analysis)
                )
                context, retrieval = "", {}
            else:
                context, retrieval = self.retrieval_service.build_context(question)
                answer = self.generation_service.generate(question, context)
        except AppError:
            raise
        except Exception as error:
            logger.exception("Query processing failed")
            raise AppError("The request could not be completed.") from error
        result = self.report_service.create(
            question=question,
            answer=answer,
            context=context,
            analysis=analysis
        )
        result["retrieval"] = retrieval
        result["query_id"] = query_id
        result["report_id"] = self.history_service.save_report(query_id, str(answer))
        result["history_id"] = result["report_id"]
        return result
