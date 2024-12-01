from chess.board.chess_board import ChessBoard


class PositionValidator:

    @staticmethod
    def validate(position: str, board: ChessBoard) -> bool:
        if not PositionValidator.is_valid_column(position[0], board.get_width()):
            return False

        if not PositionValidator.is_valid_row(position[1:], board.get_height()):
            return False

        return True

    @staticmethod
    def is_valid_row(row: str, height: int) -> bool:
        return 1 <= int(row) <= height

    @staticmethod
    def is_valid_column(column: str, width: int) -> bool:
        column_index = ord(column) - ord('A')
        return 0 <= column_index < width
