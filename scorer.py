from typing import Dict
from chess import WHITE, Board, Piece, Color, Square
from piece_square_tables import PieceSquareTable


class Scorer:
    def __init__(self) -> None:
        pass

    # implementing the Simplified Evaluation Function

    @staticmethod
    def evaluate(self, board: Board) -> float:
        _return_value = 0
        _piece_map = board.piece_map()

        for i in _piece_map:
            _piece = _piece_map[i].symbol

            if _piece.upper() == 'K' and self._is_end_game(board):
                _table = PieceSquareTable['K_EG'].value
            else:
                _table = PieceSquareTable[_piece.upper()].value

            # uppercase means WHITE
            if _piece.isupper():
                # if white, reverse the table
                _table = _table[::-1]
                _mutliplier = 1
            else:
                _mutliplier = -1

            # get the score from the table
            _score = _table[i]

            # add or subtract from the total score depending on the piece's color
            _return_value += _score * _mutliplier

        return _return_value

    @staticmethod
    def _is_end_game(board: Board) -> bool:
        _piece_map = board.piece_map()

        _white_pieces = [_piece_map[x].symbol().upper() for x in filter(
            lambda y: _piece_map[y].symbol().isupper(), _piece_map)]
        _black_pieces = [_piece_map[x].symbol().upper() for x in filter(
            lambda y: _piece_map[y].symbol().islower(), _piece_map)]

        if 'Q' not in _white_pieces and 'Q' not in _black_pieces:
            _return_value = True
        elif 'Q' not in _white_pieces and 'Q' in _black_pieces and (len(_black_pieces) <= 2 or len([x for x in _black_pieces if x in ['B', 'N']]) <= 1):
            _return_value = True
        elif 'Q' not in _black_pieces and 'Q' in _white_pieces and (len(_white_pieces) <= 2 or len([x for x in _white_pieces if x in ['B', 'N']]) <= 1):
            _return_value = True
        else:
            _return_value = False

        return _return_value
