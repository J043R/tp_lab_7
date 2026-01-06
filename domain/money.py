class Money:
    def __init__(self, amount: float):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __eq__(self, other):
        return self.amount == other.amount
