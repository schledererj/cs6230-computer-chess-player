from typing import Callable, List, Tuple
import chess
import random
from numpy import mean
from copy import deepcopy

from scorer import Scorer


class BoardStateTreeNode:
    def __init__(self, board: chess.Board, max_children: int, move: chess.Move = None) -> None:
        self._board = board.copy()
        self._move = move
        self._max_children = max_children
        self._children = list()

    def populate_tree(self, depth: int) -> None:
        if depth <= 0:
            return

        _legal_moves = list(self._board.legal_moves)
        _random_moves = [random.choice(_legal_moves)
                         for x in range(self._max_children)]
        for _move in _random_moves:
            _new_node_board = self._board.copy()
            if self._move:
                _new_node_board.push(_move)
            _node = BoardStateTreeNode(_new_node_board, self._max_children, _move)
            _node.populate_tree(depth - 1)
            self._children.append(_node)

    def evaluate_moves(self, scorer: Scorer, agg_func: Callable=mean) -> List[Tuple[float, chess.Move]]:
        _return_value = list()

        # root node
        if not self._move:
            for _c in self._children:
                _evaled_moves = _c.evaluate_moves(scorer, agg_func)
                _return_value.extend(_evaled_moves)

        # bottom of tree
        elif not self._children:
            _score = scorer.evaluate(self._board)
            _return_value.append((float(_score), self._move))

        # middle of tree
        else:
            _evaled_moves = [x.evaluate_moves(scorer, agg_func) for x in self._children]
            _average_score = agg_func([x[0][0] for x in _evaled_moves])
            _return_value.append((_average_score, self._move))

        return _return_value
