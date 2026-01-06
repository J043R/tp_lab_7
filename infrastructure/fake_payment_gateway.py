from interfaces.payment_gateway import PaymentGateway

class FakePaymentGateway(PaymentGateway):
    def charge(self, order_id, money):
        return True
