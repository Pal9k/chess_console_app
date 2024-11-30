from chess.board.chess_board import ChessBoard
from chess.pieces.strategies.base_move_strategy import MoveStrategy


class QueenMoveStrategy(MoveStrategy):

    def get_possible_moves(self, x: int, y: int, board: ChessBoard) -> list[str]:
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        possible_moves = []

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            while board.is_valid_position(nx, ny):
                possible_moves.append(board[nx][ny])
                nx += dx
                ny += dy

        return possible_moves
