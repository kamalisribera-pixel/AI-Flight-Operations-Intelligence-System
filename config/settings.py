from pathlib import Path
import os


PROJECT_NAME = "AI_FOIS"
VERSION = "0.1.0"

ROOT_DIR = Path(__file__).resolve().parent.parent


def _load_dotenv():
	"""Load simple KEY=VALUE pairs without overriding the process environment."""
	env_file = ROOT_DIR / ".env"
	if not env_file.exists():
		return
	for line in env_file.read_text(encoding="utf-8").splitlines():
		line = line.strip()
		if line and not line.startswith("#") and "=" in line:
			key, value = line.split("=", 1)
			os.environ.setdefault(key.strip(), value.strip().strip('"\''))


_load_dotenv()
ENVIRONMENT = os.getenv("APP_ENV", "development").lower()

DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
DOCUMENTS_DIR = DATA_DIR / "documents"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

MODELS_DIR = ROOT_DIR / "models"
REPORTS_DIR = ROOT_DIR / "reports"
DATABASE_DIR = ROOT_DIR / "vector_db"
APP_DATABASE_DIR = ROOT_DIR / "database"
APP_DATABASE_FILE = APP_DATABASE_DIR / "fois.db"
DATABASE_SCHEMA_FILE = APP_DATABASE_DIR / "schema.sql"
HISTORY_DATABASE_FILE = DATA_DIR / "history.sqlite3"
LOGS_DIR = ROOT_DIR / "logs"

APP_LOG_FILE = LOGS_DIR / "app.log"

PROCESSED_DOCUMENTS_FILE = PROCESSED_DATA_DIR / "documents.json"
CHUNKS_FILE = PROCESSED_DATA_DIR / "chunks.json"
EMBEDDINGS_FILE = PROCESSED_DATA_DIR / "embeddings.npy"
