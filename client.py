from notifications import EmailNotification, NotificationFactory
from order import Order
from order_processor_v2 import order_processor_v2
from payments import PaymentProcessorFactory
from shipping import ShippingProcessorFactory


class client:
    def run(self):
        print("Processing order...")
        order = Order(1, 100)
        payment_processor = PaymentProcessorFactory.get_payment_processor("CREDIT")
        shipping_processor = ShippingProcessorFactory.get_shipping_processor("STANDARD")
        notification_service = NotificationFactory.create_notification("EMAIL")
        order_processor = order_processor_v2(
            payment_processor, shipping_processor, notification_service
        )
        order_processor.process(order)


if __name__ == "__main__":
    client = client()
    client.run()
