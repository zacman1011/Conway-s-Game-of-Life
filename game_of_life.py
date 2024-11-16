from boards.wrap_around_quad import WrapAroundQuad


class GameOfLife:

    def __init__(self, board, max_ticks=50):
        self.board = board
        self.board.generate_board()
        self.start_board = self.board.board.copy()
        self.alive = self.board.is_alive()
        self.full_circle = False
        self.max_ticks = max_ticks

    def tick(self, frame_num, img=None):
        if frame_num >= self.max_ticks:
            return img

        self.board.tick()
        self.alive = self.board.is_alive()
        self.full_circle = self.full_circle or self.board.board == self.start_board

        if img is not None:
            img.set_data(self.board.to_np())
        return img
