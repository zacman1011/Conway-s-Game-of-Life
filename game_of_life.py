from boards.wrap_around_quad import WrapAroundQuad


class GameOfLife:

    def __init__(self, board=None, max_ticks=50):
        if board is None:
            board = WrapAroundQuad({(1, 2), (2, 3), (3, 1), (3, 2), (3, 3)}, 50, 50)

        self.board = board
        self.board.generate_board()
        self.start_board = self.board.board.copy()
        self.alive = self.board.is_alive()
        self.full_circle = False
        self.max_ticks = max_ticks

    def tick(self, frame_num, img=None):
        if frame_num >= self.max_ticks:
            return img

        print(f"Frame number {frame_num}")
        self.board.tick()
        self.alive = self.board.is_alive()
        self.full_circle = self.full_circle or self.board.board == self.start_board

        if img is not None:
            img.set_data(self.board.to_np())
            return img
