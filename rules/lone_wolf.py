from rules.rules import Rules


class LoneWolf(Rules):

    def survival(self, num_neighbours, current):
        if num_neighbours == 2:
            # survives or spawns by reproduction
            return 1
        elif num_neighbours > 3 and current == 1:
            # dies by overpopulation
            return 0
        else:
            # stays dead
            return 0
