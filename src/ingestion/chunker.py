class AerospaceDocumentChunker:

    def __init__(
        self,
        documents,
        chunk_size=1000,
        overlap=200
    ):

        self.documents = documents

        self.chunk_size = chunk_size

        self.overlap = overlap



    # =====================================================
    # CREATE CHUNKS
    # =====================================================

    def create_chunks(self):

        chunks = []


        chunk_id = 0


        for document in self.documents:


            text = document["text"]


            metadata = document["metadata"]


            start = 0


            while start < len(text):


                end = start + self.chunk_size


                chunk_text = text[start:end]


                chunks.append(

                    {
                        "chunk_id": chunk_id,

                        "text": chunk_text,

                        "metadata": {

                            **metadata,

                            "chunk_size": len(chunk_text)

                        }

                    }

                )


                chunk_id += 1


                start += (
                    self.chunk_size
                    -
                    self.overlap
                )


        return chunks