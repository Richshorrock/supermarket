import numpy as np

class Racer:
    
    def __init__(self, name):
        
        self.name = name
        self.location = 0
        self.animal_type = 'racer animal'
    
    def move(self):
        self.location += 0.1

class Snail(Racer):
    
    def __init__(self, name):
        super().__init__(name)
        self.animal_type = 'snail'
        
    def move(self):
        self.location += np.random.normal()
        
    def slime_trail(self):
        print('there is slime behind me!')

class Turtle(Racer):
    def __init__(self, name):
        super().__init__(name)
        self.animal_type = 'turtle'
    def move(self):
        self.location += np.random.choice([0,1], p = [0.65, 0.35])
    def slow(self):
        print('there is noone behind me!')

class Rabbit(Racer):
    def __init__(self, name):
        super().__init__(name)
        self.animal_type = 'rabbit'
    def move(self):
        self.location += np.random.random()
    def rabbit_stew(self):
        print('I taste good!')

if __name__ == '__main__':

    shelly = Snail('shelly')
    murtle = Turtle('murtle')
    roger = Rabbit('roger')

    print(f'please welcome {shelly.name}, {murtle.name} and {roger.name} to the staring line!')

    racers = [shelly, murtle, roger]

    for racer in racers:
        for _ in range(10):
            print(f'{racer.name} is at {racer.location}')
            racer.move()
            print(f'{racer.name} moves to {racer.location}')


