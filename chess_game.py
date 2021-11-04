import chess
import argparse
from numpy import number
from random_player import RandomPlayer
from termcolor import cprint

from search_player import SearchPlayer


class ChessGame:
    def __init__(self, depth: int, max_children: int) -> None:
        self._board = chess.Board()
        self._white_player = SearchPlayer(depth, max_children)
        self._black_player = RandomPlayer()

    def reset(self) -> None:
        self._board = chess.Board()

    def play_turn(self) -> None:
        if self._board.turn == chess.WHITE:
            self._board = self._white_player.play_move(self._board)
        else:
            self._board = self._black_player.play_move(self._board)

        if self._board.is_game_over():
            self.print_game_stats(True)

    def print_game_stats(self, game_over_hint: bool = None, do_print: bool = False) -> None:
        if game_over_hint or self._board.is_game_over():
            if do_print:
                cprint(f"""
    THE GAME IS OVER.
    THE OUTCOME IS: {self._board.outcome().termination}.
    THE WINNER IS: {"DRAW" if self._board.outcome().winner is None else ("WHITE" if self._board.outcome().winner else "BLACK")}
    THE FINAL BOARD STATE IS:
    {self._board}
                """, "green")
        else:
            if do_print:
                cprint(f"""
    THE GAME IS NOT OVER.
    THE CURRENT TURN IS: {"WHITE" if bool(self._board.turn) else "BLACK"}.
    THERE HAVE BEEN {self._board.fullmove_number} FULL MOVES THIS GAME.
                """, "red")

    def play_until_move(self, number_of_moves: int) -> int:
        i = 0
        while not self._board.is_game_over() and i < number_of_moves * 2:
            self.play_turn()

        return (self._board.fullmove_number, "DRAW" if self._board.outcome().winner is None else ("WHITE" if self._board.outcome().winner else "BLACK"), self._board.outcome().termination)
