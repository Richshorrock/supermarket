from racer import Snail, Turtle, Rabbit

class Race:
    '''
    this is the race class to.....
    '''
    def __init__(self, rabbits=2, turtles=3, snails=4, rounds=10):

        self.rounds = rounds
        self.racer_list = []
        self.number_rabbits = rabbits
        self.number_turtles = turtles
        self.number_snails = snails

    def load_racers(self):

        for snail_id in range(self.number_snails):
            self.racer_list.append(Snail(f'snail_{snail_id}'))
        for turtle_id in range(self.number_turtles):
            self.racer_list.append(Turtle(f'turtle_{turtle_id}'))
        for rabbit_id in range(self.number_rabbits):
            self.racer_list.append(Rabbit(f'rabbit_{rabbit_id}'))

    def start_race(self):
        for round in range(self.rounds):
            for racer in self.racer_list:
                racer.move()

    def evaluate_race(self):
        for racer in self.racer_list:
            print(racer.name, racer.location, racer.animal_type)
            


if __name__ == '__main__':

    race = Race()
    race.load_racers()
    race.start_race()
    race.evaluate_race()