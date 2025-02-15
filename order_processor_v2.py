from notifications import NotificationService
from payments import PaymentProcessor
from shipping import ShippingProcessor


class order_processor_v2:
    def __init__(
        self,
        payment_processor: PaymentProcessor,
        shipping_processor: ShippingProcessor,
        notification_service: NotificationService,
    ):
        self.payment_processor = payment_processor
        self.shipping_processor = shipping_processor
        self.notification_service = notification_service

    def process(self, order):
        self.payment_processor.process_payment(order)
        self.shipping_processor.process_shipping(order)
        self.notification_service.send("Order processed successfully")
