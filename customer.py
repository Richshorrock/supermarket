import pandas as pd
import numpy as np
    
class Customer:

    def __init__(self, customer_id, location = 'entry',):
        self.customer_id = customer_id
        self.location = location
        self.basket = []
        self.aisles = self.TM.columns #['dairy', 'spices', 'fruit', 'drinks', 'checkout']
        self.stock = {
        "dairy_retail_price": [2, 3, 5],
        "spice_retail_price": [1, 2, 3],
        "fruit_retail_price": [1, 3, 6],
        "drink_retail_price": [2, 5, 10]
}
        
    def move(self):
        if self.location == 'checkout':
            return None
        elif self.location == 'entry':
            self.location = 'checkout'
        self.location = np.random.choice(self.aisles, p=self.TM.loc[self.location])
        if self.location == 'checkout':
            pass
        else:
            self.fill_basket()
        
    def fill_basket(self):
    
        if self.location == 'dairy':
            item = np.random.choice(self.stock["dairy_retail_price"])
              
        elif self.location == 'spice':
            item = np.random.choice(self.stock["spice_retail_price"])
            
        elif self.location == 'fruit':
            item = np.random.choice(self.stock["fruit_retail_price"])
            
        else:
            item = np.random.choice(self.stock["drink_retail_price"])
        self.basket.append(item)
        

customer = Customer(1, 'dairy', [])
customer.move()
print(customer.basket)
print(customer.location)
        