import random
import numpy as np

from customer import Customer


class Supermarket:
    def __init__(self): # customer_id is still fuzzy, 0 or do we just make a variable based on the mc?
        self.customer_id = 0
        self.customer_list = []
        self.revenue = 0
        
    def start_supermarket(self):
        for timestep in range(900):
            for _ in range(random.randint(0,3)): # this should be 5 right? 5 aisles counting checkout
                customer = Customer(self.customer_id) 
                self.customer_list.append(customer) #I swear ong I will figure out how complete this function
                self.customer_id += 1
    
            for customer in self.customer_list:
                customer.move()
        
        for customer in self.customer_list:
            self.revenue += sum(customer.basket)
            
if __name__ == '__main__':
    supermarket = Supermarket()
    supermarket.start_supermarket()
    print(supermarket.revenue)
        