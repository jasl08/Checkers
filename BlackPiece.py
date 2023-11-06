import RedKingPiece
import BlackKingPiece
import CheckersPieces
import CheckersBoard
import RedPiece


class BlackPiece:
    def __init__(self, square_x, square_y, piece):
        self.square_x = square_x
        self.square_y = square_y
        self.piece = piece
        self.can_capture = can_capture_left(square_x, square_y, piece) or can_capture_right(square_x, square_y, piece)


def possible_black_piece_moves(current_x, current_y):
    """
    Responsible for finding and storing possible moves for piece
    :param current_x: The "row" of the piece via the 2D array checkers board
    :param current_y: The "column" of the piece via the 2D array checkers board
    :return: None
    """
    current_piece = CheckersBoard.checkers_board[current_x][current_y]
    if CheckersBoard.checkers_board[current_x][current_y][1] == "K":
        if current_piece[0] == "B":
            black_piece = BlackKingPiece.black_king_piece
            current_piece = CheckersBoard.checkers_board[current_x][current_y][0] + "K"
        else:
            black_piece = RedKingPiece.red_king_piece
            current_piece = CheckersBoard.checkers_board[current_x][current_y][0] + "K"
    else:
        black_piece = BlackPiece(current_x, current_y, current_piece)

    if black_piece not in CheckersPieces.possible_moves:
        CheckersPieces.possible_moves[black_piece] = []

    if current_x - 1 >= 0 and current_y - 1 >= 0:
        if CheckersBoard.checkers_board[current_x - 1][current_y - 1] == "  " and not can_capture_right(current_x,
                                                                                                        current_y,
                                                                                                        current_piece) and not RedPiece.black_king_capture_check(
            black_piece):
            valid_move = (current_x - 1, current_y - 1)
            CheckersPieces.possible_moves[black_piece].append(valid_move)

    if current_x - 1 >= 0 and current_y + 1 < 8:
        if CheckersBoard.checkers_board[current_x - 1][current_y + 1] == "  " and not can_capture_left(current_x,
                                                                                                       current_y,
                                                                                                       current_piece) and not RedPiece.black_king_capture_check(
            black_piece):
            valid_move = (current_x - 1, current_y + 1)
            CheckersPieces.possible_moves[black_piece].append(valid_move)

    possible_black_piece_moves_left(current_x, current_y, current_piece, black_piece)
    possible_black_piece_moves_right(current_x, current_y, current_piece, black_piece)
    del_no_capture_moves()


def possible_black_piece_moves_left(current_x, current_y, current_piece, black_piece):
    """
    Checks to see if piece can capture on the left side
    :param current_x: The "row" of the piece via the 2D array checkers board
    :param current_y: The "column" of the piece via the 2D array checkers board
    :param current_piece: The specific piece
    :param black_piece: A piece object
    :return: None
    """
    # moving left diagonal capture
    if can_capture_left(current_x, current_y, current_piece):
        valid_move = (current_x - 2, current_y - 2)
        CheckersPieces.possible_moves[black_piece].append(valid_move)


def possible_black_piece_moves_right(current_x, current_y, current_piece, black_piece):
    """
    Checks to see if piece can capture on the right side
    :param current_x: The "row" of the piece via the 2D array checkers board
    :param current_y: The "column" of the piece via the 2D array checkers board
    :param current_piece: The specific piece
    :param black_piece: A piece object
    :return: None
    """
    if can_capture_right(current_x, current_y, current_piece):
        valid_move = (current_x - 2, current_y + 2)
        CheckersPieces.possible_moves[black_piece].append(valid_move)


def can_capture_left(current_x, current_y, current_piece):
    """
    Checks to see if piece can capture left
    :param current_x: The "row" of the piece via the 2D array checkers board
    :param current_y: The "column" of the piece via the 2D array checkers board
    :param current_piece: The specific piece
    :return: True if piece can be captured, or False if not
    """
    # left side diagonal
    if current_x - 1 < 0 or current_y - 1 < 0:
        return False

    if current_x - 2 < 0 or current_y - 2 < 0:
        return False

    if CheckersBoard.checkers_board[current_x - 1][current_y - 1] == "  " or \
            CheckersBoard.checkers_board[current_x - 1][current_y - 1][0] == current_piece[0]:
        return False

    if CheckersBoard.checkers_board[current_x - 2][current_y - 2] != "  ":
        return False

    else:
        return True


def can_capture_right(current_x, current_y, current_piece):
    """
    Checks to see if piece can capture right
    :param current_x: The "row" of the piece via the 2D array checkers board
    :param current_y: The "column" of the piece via the 2D array checkers board
    :param current_piece: The specific piece
    :return: True if piece can be captured, or False if not
    """
    # right side diagonal
    if current_x - 1 < 0 or current_y + 1 > 8:
        return False

    if current_x - 2 < 0 or current_y + 2 >= 8:
        return False

    if CheckersBoard.checkers_board[current_x - 1][current_y + 1] == "  " or \
            CheckersBoard.checkers_board[current_x - 1][current_y + 1][0] == current_piece[0]:
        return False

    if CheckersBoard.checkers_board[current_x - 2][current_y + 2] != "  ":
        return False

    else:
        return True


def del_no_capture_moves():
    """
    Deletes moves if a piece can capture, helps with force capturing
    :return: None
    """
    capture_ctr = 0
    for pieces in CheckersPieces.possible_moves:
        if pieces.can_capture and pieces.piece[0] == "B":
            capture_ctr += 1

    if capture_ctr > 0:
        for pieces in CheckersPieces.possible_moves:
            if not pieces.can_capture and pieces.piece[0] == "B":
                CheckersPieces.possible_moves[pieces] = []


def red_king_capture_check(piece):
    """
    Helps with red king if piece can be captured
    :param piece: A piece object
    :return: True if can capture, False otherwise
    """
    if piece.piece[1] == "K":
        return can_capture_right(piece.square_x, piece.square_y, piece.piece) or can_capture_left(piece.square_x,
                                                                                                  piece.square_y,
                                                                                                  piece.piece)
    return False
