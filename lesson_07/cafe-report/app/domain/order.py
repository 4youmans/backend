"""Заказ кафе с проверкой суммы."""

from dataclasses import dataclass
from app.utils.text import normalize_name


@dataclass(frozen=True)
class Order:
    """Заказ кафе."""

    waiter: str
    kopeks: int

    def __post_init__(self) -> None:
        """Проверяет сумму заказа и нормализует имя официанта.

        Raises:
            ValueError: Если сумма заказа отрицательная.
        """
        if self.kopeks < 0:
            raise ValueError("Сумма заказа не может быть отрицательной")
        object.__setattr__(self, "waiter", normalize_name(self.waiter))
