# This is a sample Python script.
from boards.infinite_board import InfiniteBoard
from boards.padded_quad import PaddedQuad
from boards.wrap_around_quad import WrapAroundQuad
from game_of_life import GameOfLife


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    max_ticks = 25
    ticks = 0

    r_pentomino = {(22, 22), (23, 22), (21, 23), (22, 23), (22, 24)}
    glider = {(21, 22), (22, 23), (23, 21), (23, 22), (23, 23)}

    infinite_board = InfiniteBoard(r_pentomino)
    padded_board = PaddedQuad(glider, 50, 50)
    wrapped_board = WrapAroundQuad(glider, 50, 50)

    gol = GameOfLife(infinite_board)

    while gol.alive and ticks < max_ticks:
        ticks += 1
        gol.tick()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
