from pathlib import Path

from config.logging_config import logger
from src.ingestion.pdf_loader import AerospacePDFLoader


class AerospaceDocumentLoader:


    def __init__(
        self,
        directory
    ):

        self.directory = Path(directory)

        self.statistics = {

            "documents_found": 0,

            "documents_processed": 0,

            "total_pages": 0,

            "documents": []

        }


        if not self.directory.exists():

            raise FileNotFoundError(
                f"Document directory not found: {self.directory}"
            )


    # =====================================================
    # FIND PDF FILES
    # =====================================================

    def get_pdf_files(self):

        return list(
            self.directory.glob("*.pdf")
        )


    # =====================================================
    # LOAD DOCUMENTS
    # =====================================================

    def load_documents(self):

        documents = []


        pdf_files = self.get_pdf_files()


        self.statistics["documents_found"] = len(
            pdf_files
        )


        if not pdf_files:

            raise ValueError(
                "No PDF documents found."
            )


        for pdf_file in pdf_files:


            logger.info(
                f"Loading document: {pdf_file.name}"
            )


            loader = AerospacePDFLoader(
                pdf_file
            )


            pages = loader.load()


            documents.extend(
                pages
            )


            self.statistics["documents_processed"] += 1

            self.statistics["total_pages"] += len(
                pages
            )


            self.statistics["documents"].append(
                {
                    "filename": pdf_file.name,
                    "pages": len(pages)
                }
            )


        return documents


    # =====================================================
    # GET STATISTICS
    # =====================================================

    def get_statistics(self):

        return self.statistics
