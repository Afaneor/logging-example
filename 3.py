import logging
from colorama import Fore, Style

class ColoredFormatter(logging.Formatter):
    COLORS = {
        logging.DEBUG: Fore.BLUE,
        logging.INFO: Fore.GREEN,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.RED,
        logging.CRITICAL: Fore.RED + Style.BRIGHT
    }

    def format(self, record):
        if record.levelno in self.COLORS:
            record.levelname = (f"{self.COLORS[record.levelno]}"
                              f"{record.levelname}{Style.RESET_ALL}")
            record.msg = (f"{self.COLORS[record.levelno]}"
                         f"{record.msg}{Style.RESET_ALL}")
        return super().format(record)

# Настраиваем цветной вывод в консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(ColoredFormatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
))

# Настраиваем детальный вывод в файл
file_handler = logging.FileHandler('app.log')
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s - '
    '%(pathname)s:%(lineno)d'
))

# Создаем логгер
logger = logging.getLogger('my_app')
logger.setLevel(logging.DEBUG)

# Добавляем обработчики
logger.addHandler(console_handler)

# Добавляем обработчик для файлов
logger.addHandler(file_handler)

# Выводим сообщения
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
