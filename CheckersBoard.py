# importing
import pygame
import CheckersPieces
import Gameplay


# Reminder: 2D arrays are row - col, while images are col - row

def checkers_board_set_up():
    """
    Sets up the starting position of a checkers game
    :return: None
    """
    # visual representation of checkers board
    global checkers_board
    checkers_board = [["  ", "RP", "  ", "RP", "  ", "RP", "  ", "RP"],
                      ["RP", "  ", "RP", "  ", "RP", "  ", "RP", "  "],
                      ["  ", "RP", "  ", "RP", "  ", "RP", "  ", "RP"],
                      ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                      ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                      ["BP", "  ", "BP", "  ", "BP", "  ", "BP", "  "],
                      ["  ", "BP", "  ", "BP", "  ", "BP", "  ", "BP"],
                      ["BP", "  ", "BP", "  ", "BP", "  ", "BP", "  "]]


def display_pieces_on_board():
    """
    Loads the pieces to the screen
    :return: None
    """
    for row in range(0, 8):
        for col in range(0, 8):
            if checkers_board[row][col] == "BP":
                draw_black_piece(col, row)
            elif checkers_board[row][col] == "RP":
                draw_red_piece(col, row)
            elif checkers_board[row][col] == "BK":
                draw_black_king_piece(col, row)
            elif checkers_board[row][col] == "RK":
                draw_red_king_piece(col, row)


def draw_black_piece(row_image, col_image):
    """
    Loads the black checkers pieces to the screen
    :param row_image: Row index of a 2D array
    :param col_image: Column index of a 2D array
    :return: None
    """
    xy_square = convert_indexes_to_square(col_image, row_image)
    row_image = xy_square[0]
    col_image = xy_square[1]

    black_piece = pygame.image.load("elements/black_checker_piece.png").convert_alpha()
    black_piece = pygame.transform.smoothscale(black_piece, (70, 70))
    black_piece_rect = black_piece.get_rect()
    black_piece_rect.center = row_image, col_image
    screen.blit(black_piece, black_piece_rect)


def draw_black_king_piece(row_image, col_image):
    """
    Loads the black king pieces to the screen
    :param row_image: Row index of a 2D array
    :param col_image: Column index of a 2D array
    :return: None
    """
    xy_square = convert_indexes_to_square(col_image, row_image)
    row_image = xy_square[0]
    col_image = xy_square[1]

    black_king_piece = pygame.image.load("elements/black_checker_king_piece.png").convert_alpha()
    black_king_piece = pygame.transform.smoothscale(black_king_piece, (70, 70))
    black_king_piece_rect = black_king_piece.get_rect()
    black_king_piece_rect.center = row_image, col_image
    screen.blit(black_king_piece, black_king_piece_rect)


def draw_red_piece(row_image, col_image):
    """
    Loads the red checkers pieces to the screen
    :param row_image: Row index of a 2D array
    :param col_image: Column index of a 2D array
    :return: None
    """
    xy_square = convert_indexes_to_square(col_image, row_image)
    row_image = xy_square[0]
    col_image = xy_square[1]

    red_piece = pygame.image.load("elements/red_checker_piece.png").convert_alpha()
    red_piece = pygame.transform.smoothscale(red_piece, (70, 70))
    red_piece_rect = red_piece.get_rect()
    red_piece_rect.center = row_image, col_image
    screen.blit(red_piece, red_piece_rect)


def draw_red_king_piece(row_image, col_image):
    """
    Loads the red king pieces to the screen
    :param row_image: Row index of a 2D array
    :param col_image: Column index of a 2D array
    :return: None
    """
    xy_square = convert_indexes_to_square(col_image, row_image)
    row_image = xy_square[0]
    col_image = xy_square[1]

    red_king_piece = pygame.image.load("elements/red_checker_king_piece.png").convert_alpha()
    red_king_piece = pygame.transform.smoothscale(red_king_piece, (70, 70))
    red_king_piece_rect = red_king_piece.get_rect()
    red_king_piece_rect.center = row_image, col_image
    screen.blit(red_king_piece, red_king_piece_rect)


def draw_checkers_board():
    """
    Loads the board to the screen
    :return: None
    """
    screen_map = pygame.image.load("elements/checkers_board.png")
    map_size = screen_map.get_size()
    map_rect = screen_map.get_rect()

    global screen
    screen = pygame.display.set_mode(map_size)
    screen_map = screen_map.convert_alpha()
    screen.blit(screen_map, map_rect)


def round_coord(x, base=45):
    """
    Assists in conversion from screen coordinates to indexes
    :param x: A screen coordinate
    :param base: 45
    :return: A rounded x integer
    """
    return x - (x % base)


def convert_indexes_to_square(index_x, index_y):
    """
    Responsible for conversion from indexes of 2D array to squares on board
    :param index_x: A row index
    :param index_y: A column index
    :return: a pair of screen coordinates
    """
    row = (index_x + 1) * 90 - 45
    col = (index_y + 1) * 90 - 45
    return col, row


def convert_square_to_indexes(x_location, y_location):
    """
    Responsible for conversion from square on board to a pair of indexes for a 2D array
    :param x_location: x screen coordinate
    :param y_location: y screen coordinate
    :return: A pair of indexes for a 2D array
    """
    x_location = int(round_coord(x_location) / 90)
    y_location = int(round_coord(y_location) / 90)

    # resize if location = 8, would pose problems for the 2D array
    if x_location == 8:
        x_location -= 1

    if y_location == 8:
        y_location -= 1

    return y_location, x_location


def highlight_selected_square(x_board, y_board):
    """
    Helps in highlighting a square on a board once clicked
    :param x_board: a row index
    :param y_board: a col index
    :return: None
    """
    xy_pair = convert_indexes_to_square(x_board, y_board)
    x_board = xy_pair[0]
    y_board = xy_pair[1]
    square_highlight = pygame.image.load("elements/square_highlight.png").convert_alpha()
    square_highlight = pygame.transform.smoothscale(square_highlight, (90, 90))
    square_highlight_rect = square_highlight.get_rect()
    square_highlight_rect.center = (y_board, x_board)
    screen.blit(square_highlight, square_highlight_rect)

    reload_piece_to_board(x_board, y_board)


def reload_piece_to_board(y_square, x_square):
    """
    Redraws a piece to the board after highlighted selection / possible moves display
    :param y_square: x screen coordinate
    :param x_square: y screen coordinate
    :return: None
    """
    xy_index = convert_square_to_indexes(x_square, y_square)
    x_index = xy_index[0]
    y_index = xy_index[1]

    if checkers_board[x_index][y_index] == "BP":
        draw_black_piece(y_index, x_index)
    elif checkers_board[x_index][y_index] == "RP":
        draw_red_piece(y_index, x_index)
    elif checkers_board[x_index][y_index] == "BK":
        draw_black_king_piece(y_index, x_index)
    elif checkers_board[x_index][y_index] == "RK":
        draw_red_king_piece(y_index, x_index)


def reload_square_to_board(y_index, x_index):
    """
    Redraws a square at given coordinates
    :param y_index: a row index
    :param x_index: a column inex
    :return: None
    """
    if (y_index % 2 == 1 and x_index % 2 == 0) or (
            y_index % 2 == 0 and x_index % 2 == 1):
        xy_index = convert_indexes_to_square(x_index, y_index)
        x_square = xy_index[0]
        y_square = xy_index[1]

        square_highlight = pygame.image.load("elements/dark_square.png").convert_alpha()
        square_highlight = pygame.transform.smoothscale(square_highlight, (90, 90))
        square_highlight_rect = square_highlight.get_rect()
        square_highlight_rect.center = (y_square, x_square)
        screen.blit(square_highlight, square_highlight_rect)


def load_possible_moves(current_x, current_y):
    """
    Loads the possible moves to the board for a corresponding piece
    :param current_x: a row index
    :param current_y: a column index
    :return: None
    """
    list_of_moves = []
    for pieces in CheckersPieces.possible_moves:
        if pieces.square_x == current_x and pieces.square_y == current_y:
            list_of_moves = CheckersPieces.possible_moves[pieces]

    for move in list_of_moves:
        square = convert_indexes_to_square(move[0], move[1])
        possible_moves = pygame.image.load("elements/possible_moves.png").convert_alpha()
        possible_moves = pygame.transform.smoothscale(possible_moves, (35, 35))
        possible_moves_rect = possible_moves.get_rect()
        possible_moves_rect.center = (square[0], square[1])
        screen.blit(possible_moves, possible_moves_rect)


def set_up_process():
    """
    Steps in setting up the board
    :return: None
    """
    # displays the checkers board to screen
    draw_checkers_board()

    # sets up a 2D array representation of the board and pieces
    checkers_board_set_up()

    # uses the 2D array to load in the checkers pieces
    display_pieces_on_board()

    # makes a new history
    Gameplay.make_history()


def main():
    """
    Main
    :return: None
    """
    set_up_process()
