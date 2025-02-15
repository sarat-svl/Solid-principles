class Order:

    def __init__(self, order_id, amount):
        self.order_id = order_id
        self.amount = amount

    def get_order_id(self):
        return self.order_id

    def get_amount(self):
        return self.amount
