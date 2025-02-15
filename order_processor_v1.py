class OrderProcessor:
    def process_order(self, payment_type, shipping_type):
        if payment_type == "CREDIT":
            print("Processing Credit Card payment...")
        elif payment_type == "PAYPAL":
            print("Processing PayPal payment...")

        if shipping_type == "STANDARD":
            print("Processing Standard Shipping...")

        elif shipping_type == "EXPRESS":
            print("Processing Express Shipping...")

        print("Sending Email Notification...")
