import logging


def configure_logging(level: str | None = None) -> logging.Logger:
    log_level = (level or "INFO").upper()
    resolved_level = getattr(logging, log_level, logging.INFO)

    logger = logging.getLogger("knowledgeos")
    logger.setLevel(resolved_level)

    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter(
                "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )
        )
        logger.addHandler(handler)

    logger.propagate = False
    return logger
