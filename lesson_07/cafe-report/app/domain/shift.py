"""Объединение заказов по смене."""

from datetime import date
from app.domain.order import Order


class Shift:
    """Заказы одной рабочей смены."""

    def __init__(self, day: date) -> None:
        """Создаёт смену с пустым списком заказов.

        Args:
            day: Дата смены.
        """
        self.day = day
        self.orders: list[Order] = []

    def add(self, order: Order) -> None:
        """Добавляет заказ в смену.

        Args:
            order: Заказ для добавления.
        """
        self.orders.append(order)

    def total_kopeks(self) -> int:
        """Считает сумму заказов смены в копейках.

        Returns:
            Сумма заказов; для пустой смены — ноль.
        """
        return sum((order.kopeks for order in self.orders))
