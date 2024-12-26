import os
import pytz
from typing import Protocol, List, Tuple
from datetime import datetime
from helpers import create_file

class Protocol_Saver(Protocol):
    def __init__(self, filepath: str):
        self.path = filepath

    def save_to_file(self, buffer: List[Tuple[str, str, int]]) -> None:
        ...

class SaverTxt:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def save_to_file(self, buffer: List[Tuple[str, str, int]]) -> None:
        with open(self.filepath, "a") as file:
            file.writelines(f"{timestamp} {name} {value}\n" for timestamp, name, value in buffer)
            buffer.clear()

class SaverCsv:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def save_to_file(self, buffer: List[Tuple[str, str, int]]) -> None:
        with open(self.filepath, "a") as file:
            file.writelines(f"{timestamp};{name};{value}\n" for timestamp, name, value in buffer)
            buffer.clear()

class Statsd:
    def __init__(self, saver: Protocol_Saver, buffer_limit: int):
        self.saver = saver
        self.buffer_limit = buffer_limit
        self.buffer: List[Tuple[str, str, int]] = []

    def incr(self, name: str) -> None:
        self._add_metric(name, 1)

    def decr(self, name: str) -> None:
        self._add_metric(name, -1)

    def _add_metric(self, name: str, value: int) -> None:
        utc_now = datetime.now(pytz.utc)
        timestamp = utc_now.strftime("%Y-%m-%dT%H:%M:%S%z")
        self.buffer.append((timestamp, name, value))

        if len(self.buffer) >= self.buffer_limit:
            self._evacuate()

    def _evacuate(self) -> None:
        self.saver.save_to_file(self.buffer)

    def __enter__(self) -> 'Statsd':
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self._evacuate()
        self.buffer.clear()

def get_txt_statsd(path: str, buffer_limit: int = 10) -> Statsd:
    if not path.endswith('.txt'):
        raise ValueError("File must be a .txt or .csv file.")
    if not os.path.isfile(path):
        create_file(path)
    return Statsd(SaverTxt(path), buffer_limit)

def get_csv_statsd(path: str, buffer_limit: int = 10) -> Statsd:
    if not path.endswith('.csv'):
        raise ValueError("File must be a .txt or .csv file.")
    if not os.path.isfile(path):
        create_file(path)
    if os.path.getsize(path) == 0:
        with open(path, "a") as file:
            file.write("Timestamp;Name;Value\n")
    return Statsd(SaverCsv(path), buffer_limit)
