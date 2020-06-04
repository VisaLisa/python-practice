class Pant:
    def __init__(self, pant_color, waist_size, pant_length, pant_price):
        self.color = pant_color
        self.size = waist_size
        self.length = pant_length
        self.price = pant_price
        
    def change_price(self, new_price):
        self.price = new_price
    
    def discount(self, discount):
        return self.price - (1 - discount)