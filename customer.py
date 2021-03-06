import numpy
from purchase import Purchase

class Customer:
    def __init__(self, member_id, first_name, last_name):
        self.member_id = member_id
        self.first_name = first_name
        self.last_name = last_name
        self.purchase_dict = {}
        self.visits = 0
        #self.total_servings = 0
    
    def total_price(self):
        sum = 0
        for key in self.purchase_dict:
            sum += self.purchase_dict[key].price #key is a produce name; value corresponding to key is a purchase obj
        return '{:.2f}'.format(sum)
        
    def total_servings(self):
        sum = 0
        for key in self.purchase_dict:
            if not numpy.isnan(self.purchase_dict[key].calculate_servings()):
                sum += self.purchase_dict[key].calculate_servings() #key is a produce name; value corresponding to key is a purchase obj
        return round(sum, 1)

    
    def color(self):
        # check to make sure colors will be parsed correctly
        pie_dict = {
            "red": 0,
            "blue/purple": 0,
            "green": 0,
            "light green": 0,
            "orange/yellow": 0,
            "brown/white": 0,
        }
        
        for key in self.purchase_dict:
            if self.purchase_dict[key].color != "":
                pie_dict[self.purchase_dict[key].color] += self.purchase_dict[key].calculate_servings() #modified later depending on how servings is added to csv file
        return pie_dict