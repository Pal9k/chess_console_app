from chess.chess_board import ChessBoard
from chess.move_strategy import MoveStrategy


class King(MoveStrategy):

    def get_possible_moves(self, x: int, y: int, board: ChessBoard) -> list[str]:
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        possible_moves = [(x + dx, y + dy) for dx, dy in directions]
        return [board[nx][ny] for nx, ny in possible_moves if board.is_valid_position(nx, ny)]
