"""Построчное чтение данных из CSV."""

import csv
from collections.abc import Iterator
from pathlib import Path


def read_rows(path: Path) -> Iterator[dict[str, str]]:
    """Читает строки CSV с заголовком в кодировке UTF-8.

    Args:
        path: Путь к CSV-файлу.

    Yields:
        Словарь с именами столбцов и строковыми значениями.
    """
    with open(path, encoding="utf-8", newline="") as file:
        yield from csv.DictReader(file)
