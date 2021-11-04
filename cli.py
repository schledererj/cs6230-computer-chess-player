import argparse
from termcolor import cprint
from chess_game import ChessGame
from time import perf_counter

class Main:
    def __init__(self):
        parser = argparse.ArgumentParser(description="The JustLongEnough chess simulator, powered by AI (tm)")
        parser.add_argument("depth", help="The max depth of the search tree", type=int)
        parser.add_argument("max_children", help="The max number of random legal moves to pick to generate next level of the search tree", type=int)
        parser.add_argument("--play-until", help="The maximum number of _move pairs_ to play up to", required=False, default=999, type=int)

        args = parser.parse_args()

        depth = args.depth
        max_children = args.max_children
        play_until_moves = args.play_until

        cprint(f"""
INITIATING JUSTLONGENOUGH CHESS ENGINE, POWERED BY AI (TM)...
THE WHITE PLAYER WILL USE A SEARCH TREE OF DEPTH {depth} AND MAXIMUM CHILDREN {max_children}.
THE BLACK PLAYER WILL MAKE RANDOM MOVES.
THE GAME STARTS NOW...
        """, "magenta")

        start_time = perf_counter()
        game = ChessGame(depth, max_children)
        num_moves = game.play_until_move(play_until_moves)
        end_time = perf_counter()
        run_time = end_time - start_time
        move_time = run_time / float(num_moves)
        cprint(f"NUMBER OF MOVES\t\t\t {num_moves}", "yellow")
        cprint(f"GAME DURATION\t\t\t {run_time:0.4f} SECONDS", "yellow")
        cprint(f"EACH MOVE TOOK APPROXIMATELY\t {move_time:0.4f} SECONDS", "yellow")

if __name__ == "__main__":
    Main()
