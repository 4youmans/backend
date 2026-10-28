"""Сохранение текстовых отчётов."""

from pathlib import Path


def save_report(path: Path, lines: list[str]) -> int:
    """Сохраняет строки отчёта в файл UTF-8.

    Args:
        path: Путь к выходному файлу.
        lines: Строки отчёта без завершающего перевода строки.

    Returns:
        Количество записанных строк.
    """
    with open(path, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))
    return len(lines)
