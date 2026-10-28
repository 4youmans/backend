"""Форматирование текущей даты."""

from datetime import date


def today_label() -> str:
    """Возвращает текущую дату в формате ДД.ММ.ГГГГ."""
    return date.today().strftime("%d.%m.%Y")
