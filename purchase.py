from produce import Produce

class Purchase:
    def __init__(self, date, location, product, quantity, price):
        self.date = date
        self.location = location
        self.produce = product #product is a produce obj
        self.color = self.produce.color
        self.quantity = quantity
        self.price = price
        # self.servings = (self.quantity*(self.produce.unit_weight)*(self.produce.correction)*453.59231)/self.produce.serving_size

    def calculate_servings(self):
        return (self.quantity*(self.produce.unit_weight)*(self.produce.correction)*453.59231)/self.produce.serving_size