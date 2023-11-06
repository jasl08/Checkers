import CheckersBoard
import BlackKingPiece
import BlackPiece
import Gameplay
import RedKingPiece
import RedPiece


# CheckerPieces.py file is responsible for the handling of pieces and its processes

def possible_moves_set_up():
    """
    Sets up possible moves storage
    :return: None
    """
    global possible_moves
    possible_moves = {}


def calculate_possible_moves():
    """
    Calculates all possible moves for each piece on the board
    :return: None
    """
    for x in range(0, 8):
        for y in range(0, 8):
            if CheckersBoard.checkers_board[x][y] == "BP":
                BlackPiece.possible_black_piece_moves(x, y)
            elif CheckersBoard.checkers_board[x][y] == "RP":
                RedPiece.possible_red_piece_moves(x, y)
            elif CheckersBoard.checkers_board[x][y] == "BK":
                BlackKingPiece.possible_black_king_piece_moves(x, y)
            elif CheckersBoard.checkers_board[x][y] == "RK":
                RedKingPiece.possible_red_king_piece_moves(x, y)

    # restricts all other pieces if one piece can keep capturing
    if len(Gameplay.history) > 0:
        current_piece = ""
        last_move = Gameplay.history[-1]
        for piece in possible_moves:
            if piece.square_x == last_move[0] and piece.square_y == last_move[1]:
                current_piece = piece
                break

        for piece in possible_moves:
            if piece.piece[0] == current_piece.piece[0] and not (piece.square_x, piece.square_y) == (
                    current_piece.square_x, current_piece.square_y):
                possible_moves[piece] = []


def checker_pieces_process():
    """
    Steps to set up pieces
    :return: None
    """
    possible_moves_set_up()
    calculate_possible_moves()


def main():
    """
    Main
    :return: None
    """
    checker_pieces_process()
