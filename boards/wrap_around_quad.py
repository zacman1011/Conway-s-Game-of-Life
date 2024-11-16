import numpy as np

from boards.board import Board


class WrapAroundQuad(Board):

    def __init__(self, seed_coords, h=50, w=50, rules=None):
        super().__init__(seed_coords, rules)
        self.h = h
        self.w = w
        self.board = None

    def generate_board(self):
        self.board = [[1 if (x, y) in self.seed_coords else 0 for x in range(self.w)] for y in range(self.h)]
        self.check_for_life()

    def tick(self):
        new_board = [[self.__is_alive(x, y, self.board[y][x]) for x in range(self.w)] for y in range(self.h)]
        self.board = new_board
        self.check_for_life()

    def __is_alive(self, x, y, current):
        num_neighbours = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 and j == 0):
                    x_neighbour = (x + i + self.w) % self.w
                    y_neighbour = (y + j + self.h) % self.h
                    num_neighbours += self.board[y_neighbour][x_neighbour]

        return self.rules.survival(num_neighbours, current)

    def check_for_life(self):
        for row in self.board:
            for elem in row:
                if elem == 1:
                    self.alive = True
                    return
        self.alive = False

    def print_board(self):
        output = ""
        for y in range(-1, self.h):
            for x in range(-1, self.w):
                if x == -1:
                    if y == -1:
                        output += " "
                    else:
                        output += str(y)
                else:
                    if y == -1:
                        output += str(x)
                    else:
                        output += (u"\u2588" if self.board[y][x] == 1 else " ")
                output += " "
            output += "\n"
        print(output)

    def to_np(self):
        return np.array(self.board)
