import abc
from typing import List, Tuple
import chess
from termcolor import cprint

class Player(abc.ABC):
    def play_move(self, board: chess.Board) -> chess.Board:
        _moves = self._enumerate_moves(board)
        _move_to_make = self._choose_move(board, _moves)
        # _print_color = "green" if board.turn == chess.WHITE else "red"
        # cprint(f"MOVE: {_move_to_make}", _print_color)
        # print(".", end="", flush=True)
        board.push(_move_to_make)
        return board

    @abc.abstractmethod
    def _enumerate_moves(self, board: chess.Board) -> List[Tuple[float, chess.Move]]:
        pass

    def _choose_move(self, board: chess.Board, moves: List[Tuple[float, chess.Move]]) -> chess.Move:
        if board.turn == chess.WHITE:
            _func = max
        else:
            _func = min

        return _func(moves, key=lambda x: x[0])[1]