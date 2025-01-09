# ❌ Плохой подход с print
def process_payment(amount, user_id):
    print(f"Processing payment for user {user_id}")  # Нет временной метки
    print(f"Amount: {amount}")  # Нет уровня важности
    try:
        # ... операции с платежом
        raise Exception("Payment failed")  # Искусственно вызываем ошибку
        print("Payment successful")  # Нельзя отключить в production
    except Exception as e:
        print(f"Error: {e}")  # Нет stacktrace

process_payment(1, 1)

# ✅ Правильный подход с logging
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


def process_payment(amount, user_id):
    logger.info(f"Processing payment for user {user_id}")  # Есть timestamp
    logger.debug(f"Amount: {amount}")  # Можно отключить в production
    try:
        # ... операции с платежом
        raise Exception("Payment failed")  # Искусственно вызываем ошибку
        logger.info("Payment successful")
    except Exception as e:
        logger.error("Payment failed", exc_info=True)  # Полный stacktrace

process_payment(1, 1)
