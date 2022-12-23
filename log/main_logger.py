import logging

#
# def find_logger():
#     # создание логгера с именем "main" (может быть любым)
#     logger = logging.getLogger('main')
#     # установка уровня логирования
#     logger.setLevel(logging.INFO)
#
#     # создание обработчика с логированием в консоль
#     cons_handler = logging.StreamHandler()
#     # установка уровня логирования конкретно этого обработчика
#     cons_handler.setLevel(logging.INFO)
#
#     # создание обработчика с логированием в файл ".log"
#     file_handler = logging.FileHandler(filename='warning_%slog' % __file__[:-2], mode="a")
#     file_handler.setLevel(logging.WARNING)
#
#     # создание шаблона отображения
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
#     # связвание обработчиков с шаблоном форматирования
#     cons_handler.setFormatter(formatter)
#     file_handler.setFormatter(formatter)
#
#     # добавление обработчиков логгеру
#     logger.addHandler(cons_handler)
#     logger.addHandler(file_handler)
#
#     # использование логгера
#     logger.debug('debug message')
#     logger.info('info message')
#     logger.warn('warn message')
#     logger.error('error message')
#     logger.critical('critical message')


# def info_logger():
#     logger = logging.getLogger(__name__)
#     handler = logging.FileHandler(filename='%slog' % __file__[:-2])
#     formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
#     handler.setFormatter(formatter)
#
#     logger.addHandler(handler)
#
#     logger.info("Test the custom logger")
#
#
# def variable_logger():
#     logging.debug(f'Enter in to the {__name__}')


def init():
    import log.lowermodule as low
    import log.uppermodule as upp

    my_file = f'{__name__}'

    low.word_count(my_file)
    upp.record_word_count(my_file)
