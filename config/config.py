import os

from config.settings import DATABASE_DIR, ENVIRONMENT


def _int_env(name, default):
	try:
		return int(os.getenv(name, str(default)))
	except ValueError as error:
		raise ValueError(f"{name} must be an integer") from error


def _float_env(name, default):
	try:
		return float(os.getenv(name, str(default)))
	except ValueError as error:
		raise ValueError(f"{name} must be a number") from error


EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL", "BAAI/bge-small-en-v1.5")
LLM_MODEL_NAME = os.getenv("LLM_MODEL", "llama3")

CHUNK_SIZE = _int_env("CHUNK_SIZE", 1000)
CHUNK_OVERLAP = _int_env("CHUNK_OVERLAP", 200)
RETRIEVAL_TOP_K = _int_env("TOP_K", 5)

LLM_TEMPERATURE = _float_env("LLM_TEMPERATURE", 0.2)
MAX_TOKENS = _int_env("MAX_TOKENS", 2048)

CHROMA_PERSIST_DIR = DATABASE_DIR
CHROMA_COLLECTION_NAME = "aerospace_knowledge"
VECTOR_INSERT_BATCH_SIZE = 5000

if ENVIRONMENT == "testing":
	LLM_TEMPERATURE = 0.0
