"""Расчёт среднего значения и границ оценок."""


def calculate_average(grades: list[int]) -> float:
    """Считает среднюю оценку с округлением до сотых.

    Args:
        grades: Непустой список целых оценок.

    Returns:
        Средняя оценка.

    Raises:
        ValueError: Если список оценок пуст.
    """
    if not grades:
        raise ValueError("Список оценок пуст")
    return round(sum(grades) / len(grades), 2)


def grade_bounds(grades: list[int]) -> tuple[int, int]:
    """Находит минимальную и максимальную оценки.

    Args:
        grades: Непустой список оценок.

    Returns:
        Пара из минимальной и максимальной оценок.

    Raises:
        ValueError: Если список оценок пуст.
    """
    if not grades:
        raise ValueError("Список оценок пуст")
    return (min(grades), max(grades))
