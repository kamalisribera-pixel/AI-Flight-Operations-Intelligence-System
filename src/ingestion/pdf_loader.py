from pathlib import Path

import pymupdf


class AerospacePDFLoader:

    def __init__(
        self,
        file_path: str
    ):

        self.file_path = Path(file_path)


    # =====================================================
    # LOAD PDF
    # =====================================================

    def load(self):

        if not self.file_path.exists():

            raise FileNotFoundError(
                f"Document not found: {self.file_path}"
            )


        document = pymupdf.open(
            self.file_path
        )


        pages = []


        for page_number, page in enumerate(document):

            text = page.get_text()


            pages.append(
                {
                    "text": text,

                    "metadata": {

                        "source": self.file_path.name,

                        "page_number": page_number + 1

                    }
                }
            )


        document.close()


        return pages