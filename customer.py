class Customer:
    def __init__(self, member_id, first_name, last_name):
        self.member_id = member_id
        self.first_name = first_name
        self.last_name = last_name
        self.purchase_dict = {}
        self.visits = 0
        self.total_servings = 0
    
    def total_price(self):
        sum = 0
        for key in self.purchase_dict:
            sum += self.purchase_dict[key].price #key is a produce name; value corresponding to key is a purchase obj
        return sum
        
    def color(self):
        pie_dict = {
            "red": 0,
            "blue": 0,
            "green": 0,
            "light_green": 0,
            "yellow": 0,
            "brown": 0,
        }
        
        for key in self.purchase_dict:
            pie_dict[self.purchase_dict[key].color] += self.purchase_dict[key].servings #modified later depending on how servings is added to csv file
        return pie_dict