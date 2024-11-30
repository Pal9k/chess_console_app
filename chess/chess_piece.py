from chess.chess_board import ChessBoard
from chess.move_strategy import MoveStrategy


class ChessPiece:
    def __init__(self, x: int, y: int, move_strategy: MoveStrategy):
        self.x = x
        self.y = y
        self.move_strategy = move_strategy

    def get_possible_moves(self, board: ChessBoard) -> list[str]:
        return self.move_strategy.get_possible_moves(self.x, self.y, board)
