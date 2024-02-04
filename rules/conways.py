from rules.rules import Rules


class Conways(Rules):

    def survival(self, num_neighbours, current):
        if num_neighbours < 2 and current == 1:
            # die by underpopulation
            return 0
        elif (num_neighbours == 2 or num_neighbours == 3) and current == 1:
            # survives
            return 1
        elif num_neighbours > 3 and current == 1:
            # dies by overpopulation
            return 0
        elif num_neighbours == 3 and current == 0:
            # spawn by reproduction
            return 1
        else:
            # stays dead
            return 0
