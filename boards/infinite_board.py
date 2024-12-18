from boards.board import Board
import numpy as np


class InfiniteBoard(Board):

    def __init__(self, seed_coords, rules=None):
        super().__init__(seed_coords, rules)

    def generate_board(self):
        self.board = self.seed_coords
        self.check_for_life()

    def tick(self):
        new_board = set()
        dead_neighbours = {}
        # Check if alive cells survive and populate the dead_neighbours dict
        self.__check_live_cells(dead_neighbours, new_board)
        # Check to see if any cells spawn from the neighbours of the alive cells in the last iteration
        self.__check_dead_cells(dead_neighbours, new_board)
        # Set new board and check it has life
        self.board = new_board
        self.check_for_life()

    def __check_live_cells(self, dead_neighbours, new_board):
        for (x, y) in self.board:
            # For each alive cell in the board check its neighbours
            num_neighbours = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    # Use i and j to iterate through 8 neighbours + itself
                    neighbour = (x + i, y + j)

                    # Ignore if referring to itself
                    if not (i == 0 and j == 0):
                        if neighbour in self.board:
                            # If neighbour is alive then count can increment
                            num_neighbours += 1
                        else:
                            # If neighbour is dead then we keep track of the amount of alive neighbours it has
                            # If it has not been tracked so far then we are adding it to dead_neighbours
                            # If it has been tracked then we are incrementing the count of alive neighbours
                            dead_neighbours[neighbour] = dead_neighbours.get(neighbour, 0) + 1

            # Use the rules class object given to the board to work out if this cell survives
            if self.rules.survival(num_neighbours, 1) == 1:
                new_board.add((x, y))

    def __check_dead_cells(self, dead_neighbours, new_board):
        for coord in dead_neighbours:
            if self.rules.survival(dead_neighbours[coord], 0) == 1:
                new_board.add(coord)

    def check_for_life(self):
        self.alive = len(self.board) != 0

    def print_board(self):
        if not self.alive:
            print("Board has died")
            return

        min_x, max_x, min_y, max_y = None, None, None, None
        for (x, y) in self.board:
            if min_x is None:
                min_x, max_x, min_y, max_y = x, x, y, y
            else:
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                min_y = min(min_y, y)
                max_y = max(max_y, y)

        output = ""
        for y in range(min_y - 1, max_y + 2):
            for x in range(min_x - 1, max_x + 2):
                output += ("♥" if (x, y) in self.board else "•")
                output += " "
            output += "\n"
        print(output)

    def to_np(self):
        if not self.alive:
            print("Board has died")
            return

        min_x, max_x, min_y, max_y = None, None, None, None
        for (x, y) in self.board:
            if min_x is None:
                min_x, max_x, min_y, max_y = x, x, y, y
            else:
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                min_y = min(min_y, y)
                max_y = max(max_y, y)

        size = max((max_x - min_x), (max_y - min_y)) + 3

        grid = np.zeros(size * size).reshape(size, size)

        for (x, y) in self.board:
            grid[y - min_y + 1][x - min_x + 1] = 255

        return grid
