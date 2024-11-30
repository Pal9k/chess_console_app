class ChessBoard:
    def __init__(self, height, width):
        self.positions = self._generate_positions(height, width)

    @staticmethod
    def _generate_positions(height, width):
        positions = []
        for row_index in range(height, 0, -1):
            row = []
            for column_index in range(width):
                column_letter = chr(ord('A') + column_index)
                row.append(f"{column_letter}{row_index}")
            positions.append(row)
        return positions

    def get_height(self) -> int:
        return len(self.positions)

    def get_width(self) -> int:
        return len(self.positions[0])

    def get_chess_board(self) -> list[list[str]]:
        return self.positions
