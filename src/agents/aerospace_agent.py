from src.tools.failure_analysis import FailureAnalysisTool
from src.tools.report_generator import FailureReportGenerator
from src.tools.failure_classifier import FailureClassifier
from src.tools.risk_assessor import RiskAssessor
from src.tools.maintenance_advisor import MaintenanceAdvisor
from src.tools.troubleshooting_agent import TroubleshootingAgent
from tools.root_cause_analyzer import RootCauseAnalyzer
from src.tools.system_dependency_analyzer import SystemDependencyAnalyzer
from src.tools.flight_impact_analyzer import FlightImpactAnalyzer
from src.tools.procedure_advisor import ProcedureAdvisor


class AerospaceAgent:

    # =========================================================
    # INITIALIZATION
    # =========================================================

    def __init__(
        self,
        retriever,
        llm
    ):

        self.retriever = retriever
        self.llm = llm

        self.failure_tool = FailureAnalysisTool(
            retriever
        )

        self.report_generator = FailureReportGenerator()

        self.failure_classifier = FailureClassifier()

        self.risk_assessor = RiskAssessor()     

        self.maintenance_advisor = MaintenanceAdvisor() 

        self.troubleshooter = TroubleshootingAgent()  

        self.root_cause = RootCauseAnalyzer()

        self.system_dependency_analyzer = SystemDependencyAnalyzer()

        self.flight_impact_analyzer = FlightImpactAnalyzer()

        self.procedure_advisor = ProcedureAdvisor()
    # =========================================================
    # RUN AGENT
    # =========================================================

    def run(
        self,
        question
    ):

        # -----------------------------------------------------
        # FAILURE ANALYSIS WORKFLOW
        # -----------------------------------------------------

        if self.is_failure_question(question):

            classification = self.failure_classifier.classify(
                question
            )

            risk = self.risk_assessor.assess(
                classification
            )

            analysis = self.failure_tool.analyze(
                question,
                classification
            )

            maintenance = self.maintenance_advisor.recommend(
                classification
            )

            troubleshooting = self.troubleshooter.troubleshoot(
                classification
            )

            root_causes = self.root_cause.analyze(
                classification
            )

            system_dependencies = self.system_dependency_analyzer.analyze(
                classification
            )

            flight_impact = self.flight_impact_analyzer.analyze(
                classification
            )

            procedures = self.procedure_advisor.advise(
                classification
            )

            context = self.build_failure_context(
                analysis
            )

            answer = self.llm.generate(
                question,
                context
            )

            return self.report_generator.generate(
                failure=question,
                classification=classification,
                risk=risk,
                maintenance=maintenance,
                troubleshooting=troubleshooting,
                root_causes=root_causes,
                analysis=answer,
                system_dependencies=system_dependencies,
                flight_impact=flight_impact,
                procedures=procedures
            )

        # -----------------------------------------------------
        # NORMAL RAG WORKFLOW
        # -----------------------------------------------------

        context = self.retrieve(
            question
        )

        answer = self.llm.generate(
            question,
            context
        )

        return answer

    # =========================================================
    # FAILURE DETECTION
    # =========================================================

    def is_failure_question(
        self,
        question
    ):

        keywords = [

            "failure",
            "fail",
            "fails",
            "fault",
            "problem",
            "damage",
            "loss",
            "drop",
            "malfunction",
            "leak",
            "stall",
            "overheat",
            "shutdown"

        ]

        return any(
            word in question.lower()
            for word in keywords
        )

    # =========================================================
    # BUILD FAILURE CONTEXT
    # =========================================================

    def build_failure_context(
        self,
        analysis
    ):

        context = []

        context.append(
            f"""
System:
{analysis['classification']['system']}

Failure:
{analysis['failure']}
"""
        )

        for doc, meta in zip(

            analysis["documents"],
            analysis["metadata"]

        ):

            context.append(

                f"""
Source:
{meta.get('source')}

Page:
{meta.get('page_number')}

Information:
{doc}
"""

            )

        return "\n\n".join(context)

    # =========================================================
    # NORMAL DOCUMENT RETRIEVAL
    # =========================================================

    def retrieve(
        self,
        question
    ):

        results = self.retriever.retrieve(

            question,
            top_k=5

        )

        documents = results["documents"][0]
        metadata = results["metadatas"][0]

        context_parts = []

        for doc, meta in zip(
            documents,
            metadata
        ):

            context_parts.append(

                f"""
Document:
{meta.get('source')}

Page:
{meta.get('page_number')}

Content:
{doc}
"""

            )

        return "\n\n".join(
            context_parts
        )