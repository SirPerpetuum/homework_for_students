import time
from datetime import timedelta
from functools import wraps


def retry(count=3, delay=timedelta(seconds=1), handled_exceptions=(Exception,)):
    if count < 1:
        raise ValueError("Параметр count должен быть не менее 1.")

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(count):
                try:
                    return func(*args, **kwargs)
                except handled_exceptions as e:
                    if attempt < count - 1:  # Проверяем, это ли последняя попытка
                        time.sleep(delay.total_seconds())
                    else:
                        raise e  # Повторно выбрасываем последнее исключение

        return wrapper

    return decorator
