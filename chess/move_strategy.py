from abc import ABC, abstractmethod

from chess.chess_board import ChessBoard


class MoveStrategy(ABC):
    @abstractmethod
    def get_possible_moves(self, x: int, y: int, board: ChessBoard) -> list[str]:
        raise NotImplementedError("Should be overridden by subclasses.")
