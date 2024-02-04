from rules.conways import Conways


class Board:

    def __init__(self, seed_coords, rules=None):
        if rules is None:
            rules = Conways()

        self.seed_coords = seed_coords
        self.alive = True
        self.board = None
        self.rules = rules

    def generate_board(self):
        pass

    def print_board(self):
        pass

    def tick(self):
        pass

    def check_for_life(self):
        pass

    def is_alive(self):
        return self.alive