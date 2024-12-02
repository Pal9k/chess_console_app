from chess.models.board.chess_board import ChessBoard
from chess.models.pieces.piece import Piece


class Queen(Piece):

    def get_possible_moves(self, board: ChessBoard) -> list[str]:
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        possible_moves = []

        for dx, dy in directions:
            nx, ny = self.x + dx, self.y + dy
            while board.is_valid_position(nx, ny):
                possible_moves.append(board[nx][ny])
                nx += dx
                ny += dy

        return possible_moves
