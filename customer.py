import pandas as pd
import numpy as np
    
class Customer:
    
    asiles = ['dairy', 'spices', 'fruit', 'drinks', 'checkout']

    stock = {
        "dairy_retail_price": [2, 3, 5],
        "spice_retail_price": [1, 2, 3],
        "fruit_retail_price": [1, 3, 6],
        "drink_retail_price": [2, 5, 10]
}
    
    def __init__(self, customer_id, location, basket):
        self.customer_id = customer_id
        self.location = None
        self.basket = []

    def move(self):
        self.location = np.random.choice(self.asiles)
        self.fill_basket()
        
    def fill_basket(self):
    
        if self.location == 'dairy':
            item = np.random.choice(self.stock["dairy_retail_price"])
            self.basket.append(item)
            
        elif self.location == 'spice':
            item = np.random.choice(self.stock["spice_retail_price"])
            self.basket.append(item)
        
        elif self.location == 'fruit':
            item = np.random.choice(self.stock["fruit_retail_price"])
            self.basket.append(item)
        
        elif self.location == 'drinks':
            item = np.random.choice(self.stock["drink_retail_price"])
            self.basket.append(item)
        

customer = Customer(1, 'dairy', [])
customer.move()
print(customer.basket)
print(customer.location)
        