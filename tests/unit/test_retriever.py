import pytest

from src.exceptions import RetrievalError
from src.services.retrieval_service import RetrievalService


class FakeRetriever:
    def retrieve(self, query, top_k):
        return {"documents": [["lift explanation"]], "metadatas": [[{"source": "manual.pdf", "page_number": 2}]]}


def test_retrieval_builds_context():
    context, results = RetrievalService(FakeRetriever()).build_context("lift")
    assert "manual.pdf" in context
    assert results["documents"][0][0] == "lift explanation"


def test_empty_retrieval_is_reported():
    class EmptyRetriever:
        def retrieve(self, query, top_k):
            return {"documents": [[]], "metadatas": [[]]}
    with pytest.raises(RetrievalError):
        RetrievalService(EmptyRetriever()).retrieve("unknown")