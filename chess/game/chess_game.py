from chess.input.input_parser import InputParser
from chess.models.board.chess_board import ChessBoard
from chess.moves.moves_calculator import MoveCalculator
from chess.utils.dimentions import Dimensions
from chess.validators.validator import Validator


class ChessGame:
    def __init__(self):
        self.board = ChessBoard(Dimensions.HEIGHT, Dimensions.WIDTH)

    def play(self):
        try:
            user_input = input("Input - ")
            piece_type, position = InputParser.parse(user_input)
            is_valid, message = Validator.validate(piece_type, position, self.board)
            if is_valid:
                moves = MoveCalculator.get_possible_moves(piece_type, position, self.board)
                print("Output - " + ", ".join(moves))
            else:
                print("Validation Error : ", message)
        except Exception as e:
            print("Error: ", e)
