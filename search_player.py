from typing import List, Tuple
from player import Player
from scorer import Scorer
import chess
from board_state_tree_node import BoardStateTreeNode


class SearchPlayer(Player):
    def __init__(self, depth: int, max_children: int):
        self._depth = depth
        self._max_children = max_children

    def _enumerate_moves(self, board: chess.Board) -> List[Tuple[float, chess.Move]]:
        _tree = BoardStateTreeNode(board, self._max_children)
        _tree.populate_tree(self._depth)
        return _tree.evaluate_moves(Scorer())