from abc import ABC, abstractmethod

from chess.board.chess_board import ChessBoard


class Piece(ABC):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @abstractmethod
    def get_possible_moves(self, board: ChessBoard) -> list[str]:
        raise NotImplementedError("Should be overridden by subclasses.")
