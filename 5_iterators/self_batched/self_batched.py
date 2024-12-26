from typing import Generator, Iterable, TypeVar, Iterator

T = TypeVar("T")

def batched(obj: Iterable[T], n: int) -> Generator[tuple[T, ...], None, None]:
    """Группирует элементы в батчи заданного размера."""
    batch: list[T] = []
    for item in obj:
        batch.append(item)
        if len(batch) == n:
            yield tuple(batch)
            batch = []
    if batch:  # Отдает оставшиеся элементы, если они есть
        yield tuple(batch)

class Batched:
    def __init__(self, obj: Iterable[T], n: int):
        self.obj = iter(obj)  # Преобразуем в итератор
        self.n = n
        self.batch = []  # Список для хранения текущего батча

    def __iter__(self) -> 'Batched':
        return self

    def __next__(self) -> tuple[T, ...]:
        while len(self.batch) < self.n:
            try:
                self.batch.append(next(self.obj))
            except StopIteration:
                if not self.batch:  # Если на этом этапе пусто
                    raise StopIteration
                else:
                    break

        if self.batch:
            batch_to_return = tuple(self.batch)
            self.batch = []  # Сбрасываем текущий батч
            return batch_to_return

        raise StopIteration  # Если ничего нет, поднять ошибку
