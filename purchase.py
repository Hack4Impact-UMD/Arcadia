class Purchase:
    def __init__(self, date, location, product, quantity, price):
        self.date = date
        self.location = location
        self.produce = product #product is a produce obj
        self.color = self.produce.color
        self.quantity = quantity
        self.price = price
        