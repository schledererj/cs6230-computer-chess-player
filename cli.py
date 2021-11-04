import argparse
import json
from termcolor import cprint
from chess_game import ChessGame
from time import perf_counter
import sys
import multiprocessing
import itertools

class Main:
    def __init__(self):
        parser = argparse.ArgumentParser(description="The JustLongEnough Chess Simulator, powered by AI (tm)")
        parser.add_argument("depth", help="The max depth of the search tree", type=int)
        parser.add_argument("max_children", help="The max number of random legal moves to pick to generate next level of the search tree", type=int)
        parser.add_argument("--play-until", help="The maximum number of _move pairs_ to play up to", required=False, default=999, type=int)

        args = parser.parse_args()

        depth = args.depth
        max_children = args.max_children
        play_until_moves = args.play_until

        cprint(f"""
INITIATING JUSTLONGENOUGH CHESS SIMULATOR, POWERED BY AI (TM)...
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

def init(args):
    _stats = args

class MultiRunner():
    def __init__(self):
        parser = argparse.ArgumentParser(description="Runs multi-threaded Chess simulations with the JustLongEnough Chess Simulator, powered by AI (tm)")
        parser.add_argument("up_to_depth", help="The max depth of the search tree. Will run depths of 1 up to this parameter", type=int)
        parser.add_argument("up_to_max_children", help="The max number of random legal moves to pick to generate next level of the search tree. Will run max children of 1 up to this parameter", type=int)
        parser.add_argument("num_games", help="The number of games to run for each variation", type=int)

        args = parser.parse_args()

        up_to_depth = args.up_to_depth
        up_to_max_children = args.up_to_max_children
        num_games = args.num_games

        cprint(f"""
INITIATING JUSTLONGENOUGH CHESS SIMULATOR, POWERED BY AI (TM)...
THIS IS THE MULTITHREADED VERSION OF THE APPLICATION.
IT WILL RUN {num_games} OF EACH VARIATION USING:
- SEARCH DEPTHS FROM 1 THROUGH {up_to_depth}
- MAX CHILDREN FROM 1 THROUGH {up_to_max_children}

IT WILL USE EVERY AVAILABLE CPU CORE AND LIKELY RUN FOR A WHILE, 
SO MAKE SURE YOUR LAPTOP IS PLUGGED IN.

THE GAMES START NOW...
        """, "magenta", file=sys.stderr)

        cpu_count = multiprocessing.cpu_count()
        depth_range = range(1, up_to_depth + 1)
        children_range = range(1, up_to_max_children + 1)
        arg_permutations = [(x[0], x[1]) for x in itertools.product(depth_range, children_range)] * num_games

        manager = multiprocessing.Manager()
        self.stats = manager.list()
        with multiprocessing.Pool(cpu_count - 1) as thread_pool:
            thread_pool.starmap(self._run_game, arg_permutations)

        print(json.dumps(list(self.stats)))

    def _run_game(self, depth, max_children):
        start_time = perf_counter()
        game = ChessGame(depth, max_children)
        num_moves, winner, termination = game.play_until_move(999)
        end_time = perf_counter()
        run_time = end_time - start_time
        move_time = run_time / float(num_moves)
        self._put_stats(depth, max_children, run_time, move_time, num_moves, winner, termination)

    def _put_stats(self, depth, max_children, run_time, move_time, num_moves, winner, termination):
        self.stats.append({
            "depth": depth,
            "max_children": max_children,
            "run_time": run_time,
            "move_time": move_time,
            "num_moves": num_moves,
            "winner": winner,
            "termination": str(termination)
        })

if __name__ == "__main__":
    # Main()
    MultiRunner()