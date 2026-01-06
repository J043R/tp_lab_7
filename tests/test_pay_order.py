import pytest
from domain.order import Order
from domain.order_line import OrderLine
from domain.money import Money
from infrastructure.in_memory_order_repository import InMemoryOrderRepository
from infrastructure.fake_payment_gateway import FakePaymentGateway
from application.pay_order_use_case import PayOrderUseCase

def test_success_payment():
    repo = InMemoryOrderRepository()
    gateway = FakePaymentGateway()

    order = Order("1")
    order.add_line(OrderLine(Money(100)))
    repo.save(order)

    use_case = PayOrderUseCase(repo, gateway)
    status = use_case.execute("1")

    assert status.value == "PAID"

def test_empty_order_payment_error():
    repo = InMemoryOrderRepository()
    gateway = FakePaymentGateway()

    order = Order("2")
    repo.save(order)

    use_case = PayOrderUseCase(repo, gateway)
    with pytest.raises(ValueError):
        use_case.execute("2")

def test_double_payment_error():
    repo = InMemoryOrderRepository()
    gateway = FakePaymentGateway()

    order = Order("3")
    order.add_line(OrderLine(Money(50)))
    repo.save(order)

    use_case = PayOrderUseCase(repo, gateway)
    use_case.execute("3")

    with pytest.raises(ValueError):
        use_case.execute("3")

def test_modify_after_payment_error():
    order = Order("4")
    order.add_line(OrderLine(Money(30)))
    order.pay()

    with pytest.raises(ValueError):
        order.add_line(OrderLine(Money(10)))

def test_total_amount():
    order = Order("5")
    order.add_line(OrderLine(Money(40)))
    order.add_line(OrderLine(Money(60)))

    assert order.total_amount().amount == 100
