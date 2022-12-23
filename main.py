import log.main_logger
import logging.config

from log.settings import logger_config

logging.config.dictConfig(logger_config)

logger_debug = logging.getLogger("debug_logger")
logger_info = logging.getLogger("info_logger")


def main():
    logger_info.info("Start Program - Test print MESSAGE INFO")
    log.main_logger.init()
    x = 15
    y = 13
    logger_debug.debug(f"Test message (DEBUG) the main in file x+y = {x + y}")

    logger_info.info("hello world")
    logger_debug.debug("hello DEBUG")


if __name__ == '__main__':
    main()
