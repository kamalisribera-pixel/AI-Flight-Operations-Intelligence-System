import logging

from config.settings import APP_LOG_FILE, LOGS_DIR, PROJECT_NAME


LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def setup_logging(level=logging.INFO):
    LOGS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    logger = logging.getLogger(PROJECT_NAME)
    logger.setLevel(level)
    logger.propagate = False

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        fmt=LOG_FORMAT,
        datefmt=DATE_FORMAT
    )

    file_handler = logging.FileHandler(
        APP_LOG_FILE,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger


logger = setup_logging()
