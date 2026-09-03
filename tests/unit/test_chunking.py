from src.ingestion.chunker import AerospaceDocumentChunker


def test_chunking_preserves_metadata_and_overlap():
    documents = [{"text": "abcdefghij", "metadata": {"source": "manual.pdf"}}]
    chunks = AerospaceDocumentChunker(documents, chunk_size=6, overlap=2).create_chunks()
    assert [chunk["text"] for chunk in chunks] == ["abcdef", "efghij", "ij"]
    assert chunks[0]["metadata"]["source"] == "manual.pdf"