from domain.money import Money

class OrderLine:
    def __init__(self, price: Money):
        self.price = price
