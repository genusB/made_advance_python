import logging
import logging.config

log_conf = {
    "version": 1,
    "formatters": {
        "basic": {
            "format": "%(asctime)s\t%(levelname)s\t%(message)s",
        },
        "extended": {
            "format": "%(asctime)s\t%(levelname)s\t%(name)s\t%(message)s",
        },
    },
    "handlers": {
        "file_handler": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "filename": "cache.log",
            "formatter": "basic",
        },
        "stream_handler": {
            "level": "DEBUG",
            "formatter": "extended",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "": {
            "level": "DEBUG",
            "handlers": ["file_handler"],
        },
        "total": {
            "level": "DEBUG",
            "handlers": ["file_handler", "stream_handler"],
        },
    },
}


def create_root_loger() -> logging.Logger:
    logging.config.dictConfig(log_conf)
    root_logger = logging.getLogger()
    return root_logger


def create_total_loger() -> logging.Logger:
    logging.config.dictConfig(log_conf)
    total_logger = logging.getLogger("total")
    return total_logger
