import time

barrier = "----------------------------------\n"


def display(gol, max_ticks=10, interval=500):
    sleep = interval / 1000
    ticks = 0

    print("Initial Board")
    gol.board.print_board()
    print(barrier)

    while gol.alive and ticks < max_ticks:
        ticks += 1

        gol.tick(ticks)
        gol.board.print_board()

        if sleep > 0:
            time.sleep(sleep)

        print(barrier)
