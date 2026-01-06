from domain.order_status import OrderStatus
from domain.money import Money

class Order:
    def __init__(self, order_id: str):
        self.id = order_id
        self.lines = []
        self.status = OrderStatus.NEW

    def add_line(self, line):
        if self.status == OrderStatus.PAID:
            raise ValueError("Cannot modify paid order")
        self.lines.append(line)

    def total_amount(self) -> Money:
        total = Money(0)
        for line in self.lines:
            total += line.price
        return total

    def pay(self):
        if not self.lines:
            raise ValueError("Cannot pay empty order")
        if self.status == OrderStatus.PAID:
            raise ValueError("Order already paid")
        self.status = OrderStatus.PAID
