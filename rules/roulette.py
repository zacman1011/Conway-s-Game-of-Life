import random

from rules.rules import Rules


class Roulette(Rules):

    def survival(self, num_neighbours, current):
        if current == 1:
            # Alive has a 4/5 chance of surviving
            return 1 if random.randint(1, 5) <= 4 else 0
        else:
            # Dead has a num_neighbours/10 chance of surviving
            return 1 if random.randint(1, 10) <= num_neighbours else 0
