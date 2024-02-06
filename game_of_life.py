from boards.wrap_around_quad import WrapAroundQuad


class GameOfLife:

    def __init__(self, board=None):
        if board is None:
            board = WrapAroundQuad({(1, 2), (2, 3), (3, 1), (3, 2), (3, 3)}, 50, 50)

        self.board = board
        self.board.generate_board()
        self.board.print_board()
        self.alive = self.board.is_alive()

    def tick(self):
        self.board.tick()
        self.alive = self.board.is_alive()
        self.board.print_board()
