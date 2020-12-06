board = []


# creates the board
def initialize_board():
    global board
    board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    return board


# displays the board
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


def is_input_in_range(index):
    index = int(index)
    if 0 < index <= 9:
        return True
    return False


def is_input_is_alpha(index):
    if index.isalpha():
        return True
    return False


def is_input_is_numeric(index):
    if index.isnumeric():
        return True
    return False


def validate_input(index):
    if not is_input_is_alpha(index):
        if is_input_is_numeric(index) and is_input_in_range(index):
            index = int(index) - 1
            if takenPositions.__contains__(index):
                return False
            takenPositions.append(index)
            return True
        return False
    return False


def get_input_from_user(input_string):
    index = input(input_string)
    return index


def player_one_movement():
    index = get_input_from_user("PLAYER ONE | Please enter one position from 1 to 9 : ")
    while not validate_input(index):
        index = get_input_from_user("PLAYER ONE | Please enter one position from 1 to 9 : ")
    board[int(index) - 1] = "X"
    check_win("X")


def player_two_movement():
    index = get_input_from_user("PLAYER TWO | Please enter one position from 1 to 9 : ")
    while not validate_input(index):
        index = get_input_from_user("PLAYER TWO | Please enter one position from 1 to 9 : ")
    board[int(index) - 1] = "O"
    check_win("O")
    return


def set_win():
    global isPlayerWin
    isPlayerWin = True


def check_win(sign):
    check_horizontal_win(sign)
    check_vertical_win(sign)
    check_diagonal_win(sign)


def check_horizontal_win(sign):
    if ((board[0] == sign and board[1] == sign and board[2] == sign) or (
            board[2] == sign and board[1] == sign and board[0] == sign)):
        set_win()
    elif ((board[3] == sign and board[4] == sign and board[5] == sign) or (
            board[5] == sign and board[4] == sign and board[3] == sign)):
        set_win()
    elif ((board[6] == sign and board[7] == sign and board[8] == sign) or (
            board[8] == sign and board[7] == sign and board[6] == sign)):
        set_win()


def check_vertical_win(sign):
    if ((board[0] == sign and board[3] == sign and board[6] == sign or (
            board[6] == sign and board[3] == sign and board[0] == sign))):
        set_win()
    elif ((board[1] == sign and board[4] == sign and board[7] == sign) or (
            board[7] == sign and board[4] == sign and board[1] == sign)):
        set_win()
    elif (board[2] == sign and board[5] == sign and board[8] == sign) or (
            board[8] == sign and board[5] == sign and board[2] == sign):
        set_win()


def check_diagonal_win(sign):
    if ((board[0] == sign and board[4] == sign and board[8] == sign or (
            board[8] == sign and board[4] == sign and board[0] == sign))):
        set_win()
    elif ((board[2] == sign and board[4] == sign and board[6] == sign or (
            board[6] == sign and board[4] == sign and board[2] == sign))):
        set_win()


def is_win():
    return isPlayerWin


def is_game_over():
    return not board.__contains__("-")


# game engine method
def game():
    display_board()
    while True:
        player_one_movement()
        display_board()
        if is_win():
            print("PLAYER ONE WON THE MATCH")
            break
        elif is_game_over():
            print("GAME OVER! TIE! :D :P")
            break
        player_two_movement()
        display_board()
        if is_win():
            print("PLAYER TWO WON THE MATCH")
            break
        elif is_game_over():
            print("GAME OVER! TIE! :D :P")
            break


# main
board = initialize_board()
takenPositions = []
isPlayerWin = False
game()
