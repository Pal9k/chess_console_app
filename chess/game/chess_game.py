from chess.board.chess_board import ChessBoard
from chess.pieces.piece_factory import PieceFactory


class ChessGame:
    def __init__(self):
        self.board = ChessBoard(8, 8)

    def parse_input(self, user_input):
        piece_type, position = user_input.split(', ')
        x, y = self.board.get_position_coordinates(position)
        return piece_type, x, y

    def get_possible_moves(self, piece_type, x, y):
        chess_piece = PieceFactory.create_piece(piece_type, x, y)
        return chess_piece.get_possible_moves(self.board)

    def play(self):
        user_input = input("Input - ")
        piece_type, x, y = self.parse_input(user_input)
        moves = self.get_possible_moves(piece_type, x, y)
        print("Output - " + ", ".join(moves))
