from boards.wrap_around_quad import WrapAroundQuad


class GameOfLife:

    def __init__(self, w, h, board=None):
        if board is None:
            board = WrapAroundQuad({(1, 2), (2, 3), (3, 1), (3, 2), (3, 3)}, 50, 50)

        self.w = max(w, 5)
        self.h = max(h, 5)
        self.alive = None
        self.board = board
        self.board.generate_board()
        self.board.print_board()

    def tick(self):
        self.board.tick()
        self.board.print_board()
