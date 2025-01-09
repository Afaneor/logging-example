import logging
from elasticsearch import Elasticsearch
from datetime import datetime


class ElasticsearchHandler(logging.Handler):
    def __init__(self, host='localhost', index_name='app-logs'):
        super().__init__()
        self.es = Elasticsearch([host])
        self.index_name = index_name

    def emit(self, record):
        try:
            # Форматируем лог для Elasticsearch
            log_entry = {
                'timestamp': datetime.utcnow(),
                'level': record.levelname,
                'message': record.getMessage(),
                'module': record.module,
                'function': record.funcName,
                'line': record.lineno,
                'trace': None
            }

            # Добавляем stacktrace если есть
            if record.exc_info:
                log_entry['trace'] = self.formatter.formatException(
                    record.exc_info
                )

            # Отправляем в Elasticsearch
            self.es.index(
                index=self.index_name,
                document=log_entry
            )
        except Exception as e:
            print(f"Failed to send log to Elasticsearch: {e}")


# Использование
es_handler = ElasticsearchHandler(
    host='http://elasticsearch:9200',
    index_name='my-app-logs'
)
es_handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
))
logger = logging.getLogger('my_app')
logger.addHandler(es_handler)
