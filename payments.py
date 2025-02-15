from abc import ABC, abstractmethod

from order import Order


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, order: Order):
        pass


class CreditCardPaymentProcessor(PaymentProcessor):
    def process_payment(self, order: Order):
        print(f"Processing credit card payment for order {order.get_order_id()}")


class PayPalPaymentProcessor(PaymentProcessor):
    def process_payment(self, order: Order):
        print(f"Processing PayPal payment for order {order.get_order_id()}")


class PaymentProcessorFactory:
    @staticmethod
    def get_payment_processor(payment_type):
        if payment_type == "CREDIT":
            return CreditCardPaymentProcessor()
        elif payment_type == "PAYPAL":
            return PayPalPaymentProcessor()
        else:
            raise ValueError("Invalid payment type")
