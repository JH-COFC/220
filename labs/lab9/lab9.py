"""
Name: <Jordan Herder>
<lab9>.py
"""


def build_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board


def print_board(board):
    """ prints the values of board """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    if str(board[position]).isnumeric():
        return True
    else:
        return False


def fill_spot(board, position, character):
    character = character.strip().lower()
    board[position-1] = character


def winning_game(board):
    for i in range(0,8,3):
        horizontal = board[i] == board[i+1] == board[i+2]
        if horizontal:
            return horizontal

    for i in range(0,2):
        vertical = board[i] == board[i+3] == board[i+6]
        if vertical:
            return vertical

    if board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
        return True
    else:
        return False


def game_over(board):
    if winning_game(board):
        return True

    for position in range(len(board)):
        empty = is_legal(board, position)
        if empty:
            return False

    return True


def get_winner(board):
    if winning_game(board):
        xCount = 0
        oCount = 0

        for position in board:
            if position == 'x':
                xCount += 1
            elif position == 'o':
                oCount += 1
        if xCount == oCount:
            return 'o'
        else:
            return 'x'
    else:
        return None


def play(board):
    num_turns = 0
    while not game_over(board):
        if num_turns % 2 == 0:
            character = 'x'
            position = eval(input("x's, choose a position:"))
            while not is_legal(board, position-1):
                print('invalid position, please try again')
                position = eval(input("x's, choose a position:"))
            fill_spot(board, position, character)
            num_turns += 1
        elif num_turns % 2 == 1:
            character = 'o'
            position = eval(input("o's, choose a position:"))
            while not is_legal(board, position-1):
                print('invalid position, please try again')
                position = eval(input("o's, choose a position:"))
            fill_spot(board, position, character)
            num_turns += 1
        print_board(board)
    winner = get_winner(board)
    if winner == 'x':
        print("x's win!")
    elif winner == 'o':
        print("o's win!")
    else:
        print("Tie")


def main():
    play_again = True
    while play_again:
        board = build_board()
        print_board(board)
        play(board)
        want_to_play = input("Would you like to play again?")
        if want_to_play[0] == 'y':
            play_again = True
        else:
            play_again = False


if __name__ == '__main__':
    main()
