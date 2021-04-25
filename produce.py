class Produce:
    def __init__(self, name, color, serving_size, unit_weight, correction):
        self.name = name
        self.color = color
        self.serving_size = serving_size
        self.unit_weight = unit_weight
        self.correction = correction
        # self.unit_price = unit_price
        
        # unit price is from the csv they gave us a while back
        # serving_size, unit_weight, correction, and color are from the product list