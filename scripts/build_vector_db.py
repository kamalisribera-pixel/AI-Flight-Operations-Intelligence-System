from pathlib import Path
import json
import numpy as np

from src.embeddings.embedding_model import AerospaceEmbeddingModel
from src.database.vector_store import AerospaceVectorStore



INPUT_PATH = Path(
    "data/processed/chunks.json"
)



def main():


    print("="*60)
    print("AI_FOIS VECTOR DATABASE BUILD")
    print("="*60)



    with open(
        INPUT_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        chunks = json.load(file)



    texts = [

        chunk["text"]

        for chunk in chunks

    ]



    model = AerospaceEmbeddingModel()


    EMBEDDING_PATH = Path(
        "data/processed/embeddings.npy"
    )

    if EMBEDDING_PATH.exists():

        print(
            "Loading existing embeddings..."
        )

        embeddings = np.load(
            EMBEDDING_PATH
        )


    else:

        print(
            "Generating embeddings..."
        )


        embeddings = model.generate_embeddings(
            texts
        )


        np.save(
            EMBEDDING_PATH,
            embeddings
        )


        print(
            "Embeddings saved."
        )


    print(
        f"Generated embeddings: {len(embeddings)}"
    )



    database = AerospaceVectorStore()


    database.add_documents(
        chunks,
        embeddings
    )


    print(
        "Vector database created"
    )


    print("="*60)



if __name__ == "__main__":
    main()