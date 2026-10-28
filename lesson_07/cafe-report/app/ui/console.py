"""Печать отчёта в консоль."""


def print_report(lines: list[str]) -> None:
    """Печатает строки отчёта по одной.

    Args:
        lines: Строки для вывода в стандартный поток.
    """
    for line in lines:
        print(line)
