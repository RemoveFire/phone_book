import logging

logger = logging.getLogger(__name__)
handler = logging.FileHandler(filename='%slog' % __file__[:-2])
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)


logger.addHandler(handler)

logger.info("Test the custom logger")

