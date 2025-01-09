import logging

# 1. Logger - основной объект для логирования
logger = logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)

# 2. Handler - куда отправляем логи
console_handler = logging.StreamHandler()  # В консоль
file_handler = logging.FileHandler("app.log")  # В файл

# 3. Formatter - как форматируем сообщение
formatter = logging.Formatter(
    fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# 4. Filter - что фильтруем (опционально)
class SensitiveDataFilter(logging.Filter):
    def filter(self, record):
        return not any(word in record.getMessage().lower()
                      for word in ['password', 'token', 'secret'])

# Соединяем всё вместе
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.addFilter(SensitiveDataFilter())

logger.debug('debug message')
logger.info(' 12345')