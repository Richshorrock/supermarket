import pandas as pd

### importing customer no's from data

df=pd.read_csv=('data/monday.csv')

def get_customer_id(customer_id):
    customer_row = df[df['customer_no'] == customer_id]
  

class Customer:
    
    def __init__(self, customer_id, basket):
        self.customer_id = customer_id
        self.supermarket = supermarket
        self.name = get_customer_id(customer_id)
        self.location = None
        self.basket = []

    #def move(self):
        #self.location += 0.1
        
customer1 = Customer()

print(customer1.customer_id)