import pygame
import BlackPiece
import CheckersPieces
import CheckersBoard
import RedPiece


def make_history():
    """
    Creates a list for storage
    :return: None
    """
    global history
    history = []


def set_history(move_to_x, move_to_y):
    """
    adds moves to a history list
    :param move_to_x: a row index
    :param move_to_y: a column index
    :return: None
    """
    history.append((move_to_x, move_to_y))


def remove_possible_moves_off_board(current_x, current_y, current_location):
    """
    Removes the possible moves on the board
    :param current_x: a row index
    :param current_y: a column index
    :param current_location: the current location of a piece at current_x, current_y
    :return:
    """
    moves = []
    for pieces in CheckersPieces.possible_moves:
        if pieces.square_x == current_x and pieces.square_y == current_y:
            moves = CheckersPieces.possible_moves[pieces]
            break

    for move in moves:
        if current_location != move:
            CheckersBoard.reload_square_to_board(move[0], move[1])


def is_valid_move(move_from_y, move_from_x, move_to_y, move_to_x):
    """
    Checks to see if attempted move is valid.
    :param move_from_x: a row index
    :param move_from_y: a column index
    :param move_to_x: a row index at destination
    :param move_to_y: a column index at destination
    :return: True if move is valid, False otherwise
    """
    piece = CheckersBoard.checkers_board[move_from_x][move_from_y]
    for pieces in CheckersPieces.possible_moves:
        if pieces.piece == piece and pieces.square_x == move_from_x and pieces.square_y == move_from_y:
            if (move_to_x, move_to_y) in CheckersPieces.possible_moves[pieces]:
                return True
    return False


def move_piece(move_from_y, move_from_x, move_to_y, move_to_x):
    """
    Moves the piece to the selected valid square
    :param move_from_y: a column index
    :param move_from_x: a row index
    :param move_to_y: a column index at destination
    :param move_to_x: a row index at destination
    :return: None
    """
    if CheckersBoard.checkers_board[move_from_x][move_from_y] == "BP" and move_to_x == 0:
        CheckersBoard.checkers_board[move_to_x][move_to_y] = "BK"
        CheckersBoard.checkers_board[move_from_x][move_from_y] = "  "

    elif CheckersBoard.checkers_board[move_from_x][move_from_y] == "RP" and move_to_x == 7:
        CheckersBoard.checkers_board[move_to_x][move_to_y] = "RK"
        CheckersBoard.checkers_board[move_from_x][move_from_y] = "  "
    else:
        CheckersBoard.checkers_board[move_to_x][move_to_y] = CheckersBoard.checkers_board[move_from_x][move_from_y]
        CheckersBoard.checkers_board[move_from_x][move_from_y] = "  "

    CheckersBoard.reload_square_to_board(move_from_x, move_from_y)

    for pieces in CheckersPieces.possible_moves:
        if pieces.square_x == move_to_x and pieces.square_y == move_to_y:
            CheckersPieces.possible_moves[pieces].remove((move_to_x, move_to_y))

    CheckersBoard.display_pieces_on_board()
    set_history(move_from_x, move_from_y)
    set_history(move_to_x, move_to_y)
    CheckersPieces.main()


def remove_pieces_from_board(current_x, current_y, move_to_x, move_to_y):
    """
    Helps with removing captured pieces from the board
    :param current_x: a row index
    :param current_y: a column index
    :param move_to_x: a row index at destination
    :param move_to_y: a column index at destination
    :return: None
    """
    if CheckersBoard.checkers_board[current_x][current_y] == "RP" or CheckersBoard.checkers_board[current_x][
        current_y] == "RK" or CheckersBoard.checkers_board[current_x][current_y] == "BK" and can_capture(current_x,
                                                                                                         current_y):

        if current_x + 2 == move_to_x and current_y + 2 == move_to_y:
            CheckersBoard.checkers_board[current_x + 1][current_y + 1] = "  "
            CheckersBoard.reload_square_to_board(current_x + 1, current_y + 1)

        if current_x + 2 == move_to_x and current_y - 2 == move_to_y:
            CheckersBoard.checkers_board[current_x + 1][current_y - 1] = "  "
            CheckersBoard.reload_square_to_board(current_x + 1, current_y - 1)

        CheckersBoard.display_pieces_on_board()

    if CheckersBoard.checkers_board[current_x][current_y] == "BP" or CheckersBoard.checkers_board[current_x][
        current_y] == "RK" or CheckersBoard.checkers_board[current_x][current_y] == "BK" and can_capture(current_x,
                                                                                                         current_y):
        if current_x - 2 == move_to_x and current_y + 2 == move_to_y:
            CheckersBoard.checkers_board[current_x - 1][current_y + 1] = "  "
            CheckersBoard.reload_square_to_board(current_x - 1, current_y + 1)

        if current_x - 2 == move_to_x and current_y - 2 == move_to_y:
            CheckersBoard.checkers_board[current_x - 1][current_y - 1] = "  "
            CheckersBoard.reload_square_to_board(current_x - 1, current_y - 1)

        CheckersBoard.display_pieces_on_board()


def can_capture(current_x, current_y):
    """
    Checks to see if a piece can capture
    :param current_x: a row index
    :param current_y: a column inedx
    :return: True if piece can capture, else returns False
    """
    current_piece = CheckersBoard.checkers_board[current_x][current_y]

    if current_piece == "BP":
        left = BlackPiece.can_capture_left(current_x, current_y, current_piece)
        right = BlackPiece.can_capture_right(current_x, current_y, current_piece)

        return left or right

    elif current_piece == "RP":
        left = RedPiece.can_capture_left(current_x, current_y, current_piece)
        right = RedPiece.can_capture_right(current_x, current_y, current_piece)

        return left or right

    else:
        left_black = BlackPiece.can_capture_left(current_x, current_y, current_piece)
        right_black = BlackPiece.can_capture_right(current_x, current_y, current_piece)
        left_red = RedPiece.can_capture_left(current_x, current_y, current_piece)
        right_red = RedPiece.can_capture_right(current_x, current_y, current_piece)
        return left_black or right_black or left_red or right_red


def piece_can_still_move(move_x, move_y):
    """
    Checks to see if a piece can still capture for multiple jumps
    :param move_x: a row index
    :param move_y: a column index
    :return: True if piece can still capture, else returns False
    """
    for pieces in CheckersPieces.possible_moves:
        if pieces.square_x == move_x and pieces.square_y == move_y:
            if pieces.can_capture:
                return True
    return False


def red_wins_message():
    """
    Displays a red wins message
    :return: None
    """
    red_win_message = pygame.image.load("elements/red_win_message.png").convert_alpha()
    red_win_message = pygame.transform.smoothscale(red_win_message, (720, 720))
    red_win_message_rect = red_win_message.get_rect()
    red_win_message_rect.center = (720 / 2, 720 / 2)
    CheckersBoard.screen.blit(red_win_message, red_win_message_rect)


def black_wins_message():
    """
    Displays a black wins message
    :return: None
    """
    black_win_message = pygame.image.load("elements/black_win_message.png").convert_alpha()
    black_win_message = pygame.transform.smoothscale(black_win_message, (720, 720))
    black_win_message_rect = black_win_message.get_rect()
    black_win_message_rect.center = (720 / 2, 720 / 2)
    CheckersBoard.screen.blit(black_win_message, black_win_message_rect)


def restart_game():
    """
    Resets a game
    :return: None
    """
    CheckersBoard.main()
    CheckersPieces.main()
    main()


def main():
    """
    # main gameplay of Checkers
    :return: None
    """
    active = True
    square_selected = False
    selected_piece = "  "
    black_player_turn = True
    red_player_turn = False
    game_over = False

    while active:

        if black_player_turn and game_over:
            game_over = False
            black_player_turn = None
            red_player_turn = None
            red_wins_message()
            pygame.display.update()

        elif red_player_turn and game_over:
            game_over = False
            black_player_turn = None
            red_player_turn = None
            black_wins_message()
            pygame.display.update()

        for event in pygame.event.get():

            # quit
            if event.type == pygame.QUIT:
                active = False

            # press "N" key for new game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    active = False
                    restart_game()

            if active:
                key = 0
                value = 0
                red_pieces = 0
                black_pieces = 0
                for pieces in CheckersPieces.possible_moves:
                    key += 1
                    if len(CheckersPieces.possible_moves[pieces]) == 0:
                        value += 1
                    if pieces.piece[0] == "B":
                        black_pieces += 1
                    if pieces.piece[0] == "R":
                        red_pieces += 1

                if key == value or black_pieces == 0 or red_pieces == 0:
                    game_over = True

            if black_player_turn:
                for piece in CheckersPieces.possible_moves:
                    if piece.piece[0] == "R":
                        CheckersPieces.possible_moves[piece] = []

            if red_player_turn:
                for piece in CheckersPieces.possible_moves:
                    if piece.piece[0] == "B":
                        CheckersPieces.possible_moves[piece] = []

            # mouse down
            if event.type == pygame.MOUSEBUTTONUP and not square_selected:

                # gets the position of the first mouse click
                first_pos = pygame.mouse.get_pos()

                # converts x and y coordinates on screen to a 2D array index
                xy_index = CheckersBoard.convert_square_to_indexes(first_pos[1], first_pos[0])
                x_index_pos_1 = xy_index[0]
                y_index_pos_1 = xy_index[1]

                if black_player_turn:
                    if CheckersBoard.checkers_board[y_index_pos_1][x_index_pos_1][0] == "B":
                        CheckersBoard.highlight_selected_square(x_index_pos_1, y_index_pos_1)
                        selected_piece = CheckersBoard.checkers_board[y_index_pos_1][x_index_pos_1]
                        CheckersBoard.load_possible_moves(y_index_pos_1, x_index_pos_1)

                elif red_player_turn:
                    if CheckersBoard.checkers_board[y_index_pos_1][x_index_pos_1][0] == "R":
                        CheckersBoard.highlight_selected_square(x_index_pos_1, y_index_pos_1)
                        selected_piece = CheckersBoard.checkers_board[y_index_pos_1][x_index_pos_1]
                        CheckersBoard.load_possible_moves(y_index_pos_1, x_index_pos_1)

                square_selected = not square_selected

            # mouse down second time after selection
            elif event.type == pygame.MOUSEBUTTONUP and square_selected:

                # gets the second position of square
                second_pos = pygame.mouse.get_pos()

                # converts x and y coordinates on screen to a 2D array index
                xy_index = CheckersBoard.convert_square_to_indexes(second_pos[1], second_pos[0])

                x_index_pos_2 = xy_index[0]
                y_index_pos_2 = xy_index[1]

                if CheckersBoard.checkers_board[y_index_pos_2][x_index_pos_2] != selected_piece and is_valid_move(
                        x_index_pos_1, y_index_pos_1,
                        x_index_pos_2, y_index_pos_2) and not game_over:
                    remove_pieces_from_board(y_index_pos_1, x_index_pos_1, y_index_pos_2, x_index_pos_2)
                    remove_possible_moves_off_board(y_index_pos_1, x_index_pos_1, (x_index_pos_2, y_index_pos_2))
                    move_piece(x_index_pos_1, y_index_pos_1, x_index_pos_2, y_index_pos_2)

                    if abs(y_index_pos_2 - y_index_pos_1) != 1 and abs(x_index_pos_2 - x_index_pos_1) != 1:
                        if not piece_can_still_move(y_index_pos_2, x_index_pos_2):
                            black_player_turn = not black_player_turn
                            red_player_turn = not red_player_turn

                    else:
                        black_player_turn = not black_player_turn
                        red_player_turn = not red_player_turn

                elif not game_over:
                    CheckersBoard.reload_square_to_board(y_index_pos_1, x_index_pos_1)
                    CheckersBoard.reload_piece_to_board(first_pos[1], first_pos[0])
                    remove_possible_moves_off_board(y_index_pos_1, x_index_pos_1, (y_index_pos_1, x_index_pos_1))

                square_selected = not square_selected

        pygame.display.update()
