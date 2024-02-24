from boards.infinite_board import InfiniteBoard
from boards.padded_quad import PaddedQuad
from boards.wrap_around_quad import WrapAroundQuad
from display.graphic import display
from game_of_life import GameOfLife


if __name__ == '__main__':
    r_pentomino = {(22, 22), (23, 22), (21, 23), (22, 23), (22, 24)}
    glider = {(21, 22), (22, 23), (23, 21), (23, 22), (23, 23)}
    blinker = {(2, 1), (2, 2), (2, 3)}

    infinite_board = InfiniteBoard(r_pentomino)
    # padded_board = PaddedQuad(glider, 50, 50)
    # wrapped_board = WrapAroundQuad(r_pentomino, 30, 30)

    gol = GameOfLife(infinite_board, max_ticks=500)

    display(gol, interval=100)


