from boards.infinite_board import InfiniteBoard
from boards.padded_quad import PaddedQuad
from boards.wrap_around_quad import WrapAroundQuad
from display.console import display
from game_of_life import GameOfLife
from rules.conways import Conways
from rules.herd import Herd
from rules.lone_wolf import LoneWolf
from rules.roulette import Roulette
from state_loader import load_state

import argparse


def get_board_size(board_args):
    return board_args.height, board_args.width


def get_rules(args):
    if args.rules == "conways":
        return Conways()
    elif args.rules == "herd":
        return Herd()
    elif args.rules == "lone_wolf":
        return LoneWolf()
    elif args.rules == "roulette":
        return Roulette()
    else:
        raise f"Unknown rules: {args.rules}"


def get_board(args, initial_coords, rules):
    if args.board == "infinite":
        return InfiniteBoard(initial_coords, rules=rules)
    elif args.board == "padded_quad":
        return PaddedQuad(initial_coords, rules=rules)
    elif args.board == "wrap_around":
        return WrapAroundQuad(initial_coords, rules=rules)
    else:
        raise f"Unknown board: {args.board}"


def main():
    parser = argparse.ArgumentParser(description="Run Conway's Game of Life with some given parameters")

    parser.add_argument(
        "--file_name",
        type=str,
        help="Specify the file containing the initial state in CSV format"
    )
    parser.add_argument(
        "--rules",
        default="conways",
        choices=["conways", "herd", "lone_wolf", "roulette"],
        help="Specify the rules for the simulation"
    )
    parser.add_argument(
        "--board",
        default="infinite",
        choices=["infinite", "padded_quad", "wrap_around"],
        help="Specify the board for the simulation"
    )
    parser.add_argument(
        "--height",
        default=50,
        type=int,
        help="Specify the height of the board (unless board is infinite)"
    )
    parser.add_argument(
        "--width",
        default=50,
        type=int,
        help="Specify the width of the board (unless board is infinite)"
    )
    parser.add_argument(
        "--max_iterations",
        default=100,
        type=int,
        help="Specify the maximum iterations for the simulation"
    )
    args = parser.parse_args()

    # Load the initial coordinates from the specified CSV
    initial_coords = load_state(args.file_name)
    print(f"Initial coordinates: {initial_coords}")

    # Create rules specified in parameter
    rules = get_rules(args)

    # Create board specified in parameter
    board = get_board(args, initial_coords, rules)

    # Create the game itself to run
    gol = GameOfLife(board, max_ticks=args.max_iterations)

    # Give the game to the display to run it
    display(gol, interval=100)


if __name__ == '__main__':
    main()
