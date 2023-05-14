import logging


class CustomFormatter(logging.Formatter):
    green = "\033[92m"
    grey = "\033[90m"
    yellow = "\033[93m"
    red = "\033[91m"
    bold_red = "\033[31m"
    reset = "\x1b[0m"
    format = (
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
    )

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: green + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def get_file_handler() -> logging.FileHandler:
    handler = logging.FileHandler("./logs/logs.log")
    handler.setFormatter(CustomFormatter())
    return handler


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(get_file_handler())
    logger.propagate = False
    return logger
