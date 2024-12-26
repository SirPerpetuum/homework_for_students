from typing import Generator, Iterable, TypeVar, Iterator

T = TypeVar("T")

def cycle(iterable: Iterable[T]) -> Generator[T, None, None]:
    """Бесконечный цикл по элементам iterable."""
    while True:
        for item in iterable:
            yield item
class Cycle:
    def __init__(self, iterable: Iterable[T]):
        self.iterable = iterable
        self.iterator = iter(iterable)

    def __iter__(self) -> 'Cycle':
        return self

    def __next__(self) -> T:
        while True:
            try:
                return next(self.iterator)
            except StopIteration:
                self.iterator = iter(self.iterable)
