"""Нормализация пробелов и имён."""


def _squash_spaces(value: str) -> str:
    """Удаляет лишние пробелы между словами.

    Args:
        value: Исходный текст.

    Returns:
        Текст с одиночными пробелами.
    """
    return " ".join(value.split())


def normalize_name(name: str) -> str:
    """Нормализует пробелы и регистр имени.

    Args:
        name: Имя в произвольном регистре.

    Returns:
        Имя с заглавной буквы в каждом слове.
    """
    return _squash_spaces(name).title()
