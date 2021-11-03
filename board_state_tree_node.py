from typing import List
import chess
import random

from scorer import Scorer


class BoardStateTreeNode:
    def __init__(self, board: chess.Board, move: chess.Move = None, max_children: int = None) -> None:
        self._board = board
        self._move = move
        self._max_children = max_children
        self._children = list()

    def populate_tree(self, depth: int) -> None:
        if depth <= 0:
            pass

        _legal_moves = list(self._board.legal_moves)
        _random_moves = [random.choice(_legal_moves)
                         for x in range(self._max_children)]
        for _move in _random_moves:
            if self._move:
                self._board.push(_move)
            _node = BoardStateTreeNode(self._board, _move, self._max_children)
            _node.populate_tree(depth - 1)
            self._children.append(_node)

    def evaluate_moves(self, scorer: Scorer, agg_func: function) -> List[(int, chess.Move)]:
        _return_value = list()
        for _m in self._children:
            _score = scorer.evaluate(_m._board)
            _return_value.append((_score, _m._move))

        return _return_value
