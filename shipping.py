from abc import ABC, abstractmethod


class ShippingProcessor(ABC):
    @abstractmethod
    def process_shipping(self, order):
        pass


class StandardShippingProcessor(ShippingProcessor):
    def process_shipping(self, order):
        print(f"Processing standard shipping for order {order.get_order_id()}")


class ExpressShippingProcessor(ShippingProcessor):
    def process_shipping(self, order):
        print(f"Processing express shipping for order {order.get_order_id()}")


class ShippingProcessorFactory:
    @staticmethod
    def get_shipping_processor(shipping_type):
        if shipping_type == "STANDARD":
            return StandardShippingProcessor()
        elif shipping_type == "EXPRESS":
            return ExpressShippingProcessor()
        else:
            raise ValueError("Invalid shipping type")
