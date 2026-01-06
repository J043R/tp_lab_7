from interfaces.order_repository import OrderRepository

class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self.storage = {}

    def get_by_id(self, order_id):
        return self.storage.get(order_id)

    def save(self, order):
        self.storage[order.id] = order
