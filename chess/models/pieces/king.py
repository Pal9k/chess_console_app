from chess.models.board.chess_board import ChessBoard
from chess.models.pieces.piece import Piece


class King(Piece):

    def get_possible_moves(self, board: ChessBoard) -> list[str]:
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        possible_moves = [(self.x + dx, self.y + dy) for dx, dy in directions]
        return [board[nx][ny] for nx, ny in possible_moves if board.is_valid_position(nx, ny)]
