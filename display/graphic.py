import matplotlib.pyplot as plt
import matplotlib.animation as animation


def display(gol, interval=500):
    grid = gol.board.to_np()

    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')

    _ani = animation.FuncAnimation(fig, gol.tick, fargs=(img,), frames=None, interval=interval)

    plt.axis('off')
    plt.show()
