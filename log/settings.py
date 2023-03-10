import logging


class MegaHandler(logging.Handler):
    def __init__(self, filename):
        logging.Handler.__init__(self)
        self.filename = filename

    def emit(self, record):
        message = self.format(record)
        with open(self.filename, "a") as file:
            file.write(message + "\n")


logger_config = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "briefFormat": {
            "format": "%(levelname)-8s %(asctime)s %(name)-16s %(message)s",
        },
        "verbose_format": {
            "format": "{asctime} - {levelname} - {name} - {message}",
            "style": "{"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "briefFormat"
        },
        "file": {
            "()": MegaHandler,
            "level": "DEBUG",
            "formatter": "verbose_format",
            "filename": "debug.log"
        },
        "fileHandler": {
            "class": "logging.FileHandler",
            "level": "INFO",
            "formatter": "verbose_format",
            "filename": "info.log"
        }
    },
    "loggers": {
        "debug_logger": {
            "level": "DEBUG",
            "handlers": ["file"]
        },
        "info_logger": {
            "level": "INFO",
            "handlers": ["console", "fileHandler"],
        }
    }
}
