from chess.chess_board import ChessBoard
from chess.chess_piece_factory import ChessPieceFactory

if __name__ == '__main__':

    piece_type, position = input("Input - ").split(',')

    board = ChessBoard(8, 8)
    x, y = board.get_position_coordinates(position)
    chess_piece = ChessPieceFactory.create_piece(piece_type, x, y)
    moves = chess_piece.get_possible_moves(board)

    print("Output - ", moves)
