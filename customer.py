import pandas as pd
import numpy as np

asiles = ['dairy', 'spices', 'fruit', 'drinks', 'checkout']

stock = {
    "dairy_retail_price": [2, 3, 5],
    "spice_retail_price": [1, 2, 3],
    "fruit_retail_price": [1, 3, 6],
    "drink_retail_price": [2, 5, 10]
}
    
class Customer:
    
    def __init__(self, customer_id, location, basket):
        self.customer_id = customer_id
        self.location = None
        self.basket = []

    def move(self, location):
        self.location = np.random.choice(self.asiles).self??????
        
    def fill_basket(self, item)
        self.location == 'dairy'
        item = np.choice(stock["dairy_ retail_price"])
        self.basket.append(item)
        
        self.location == 'spice'
        item = np.choice(stock["spice retail_price"])
        self.basket.append(item)
        
        self.location == 'fruit'
        item = np.choice(stock["fruit retail_price"])
        self.basket.append(item)
        
        self.location == 'drinks'
        item = np.choice(stock["drink_retail_price"])
        self.basket.append(item)
        
        
        