from typing import List, Tuple
from .player import Player
import chess
from .board_state_tree_node import BoardStateTreeNode


class RandomPlayer(Player):

    def _enumerate_moves(self, board: chess.Board) -> List[Tuple[float, chess.Move]]:
        _tree = BoardStateTreeNode(board, 1)
        _tree.populate_tree(1)
        return [(1, _tree._children[0]._move)]