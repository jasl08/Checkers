import BlackPiece
import CheckersPieces
import RedPiece


class BlackKingPiece:

    def __init__(self, square_x, square_y, piece):
        self.square_x = square_x
        self.square_y = square_y
        self.piece = piece
        self.can_capture = can_capture(square_x, square_y, piece)


def possible_black_king_piece_moves(current_x, current_y):
    """
    Responsible for finding and storing possible moves for piece
    :param current_x: The "row" of the piece via the 2D array checkers board
    :param current_y: The "column" of the piece via the 2D array checkers board
    :return: None
    """
    current_piece = "BK"
    global black_king_piece
    black_king_piece = BlackKingPiece(current_x, current_y, current_piece)
    CheckersPieces.possible_moves[black_king_piece] = []

    BlackPiece.possible_black_piece_moves(current_x, current_y)
    RedPiece.possible_red_piece_moves(current_x, current_y)


def can_capture(current_x, current_y, current_piece):
    """
    Checks to see if piece can capture opponent's piece
    :param current_x: The "row" of the piece via the 2D array checkers board
    :param current_y: The "column" of the piece via the 2D array checkers board
    :param current_piece: The current piece at current_x, current_y of the 2D array checkers board
    :return: True if piece can capture, or False if it can't
    """
    b_l = BlackPiece.can_capture_left(current_x, current_y, current_piece)
    b_r = BlackPiece.can_capture_right(current_x, current_y, current_piece)
    r_r = RedPiece.can_capture_right(current_x, current_y, current_piece)
    r_l = RedPiece.can_capture_left(current_x, current_y, current_piece)
    return b_l or b_r or r_r or r_l
