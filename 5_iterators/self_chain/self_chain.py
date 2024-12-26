from typing import Generator, Iterable, TypeVar, Iterator

T = TypeVar("T")

def chain(*iterables: Iterable[T]) -> Generator[T, None, None]:
    """Соединяет несколько iterable в один."""
    for iterable in iterables:
        for item in iterable:
            yield item

class Chain:
    def __init__(self, *iterables: Iterable[T]):
        self.iterables = iterables
        self.current_iter = iter(iterables)
        self.current_iter_instance = iter(next(self.current_iter))

    def __iter__(self) -> 'Chain':
        return self

    def __next__(self) -> T:
        while True:
            try:
                return next(self.current_iter_instance)
            except StopIteration:
                self.current_iter_instance = iter(next(self.current_iter))
