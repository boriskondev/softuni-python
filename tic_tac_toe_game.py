import time


def yes_or_no():
    positives = ["yes", "ye", "y"]
    negatives = ["no", "n"]
    user_input = input("Yes/No: ").lower()
    if user_input in positives:
        return "yes"
    elif user_input in negatives:
        return "no"
    else:
        print("Not a valid answer. Try again.")
        return yes_or_no()


def show_rules():
    rules = ["- The game is played by two players on a 3 by 3 squares grid;",
             "- Each player puts a sign in an empty square (\"X\" for the first player, \"O\" for the second);",
             "- The first player to get 3 of their signs in row, column or a diagonal wins;",
             "- If all 9 squares are filled and there is no winner, the game ends in a draw."]
    print("Here they are:")
    time.sleep(1.5)
    for rule in rules:
        print(rule)
        time.sleep(3)
    time.sleep(5)


def show_game_board(playing_board):
    for row in playing_board:
        for column in row:
            print(column, end=" ")
        print()
    print()


def take_turn_and_validate(playing_board):
    row = int(input("Choose row: "))
    column = int(input("Choose column: "))
    row_index = row - 1
    column_index = column - 1
    if 0 <= row_index <= 2 and 0 <= column_index <= 2:
        if playing_board[row_index][column_index] == "-":
            print()
            return row_index, column_index
    print("Not a valid turn. Try again with correct cell coordinates.")
    print()
    return take_turn_and_validate(playing_board)


def check_row_win(playing_board):
    for row in playing_board:
        if len(set(row)) == 1 and "-" not in row:
            return True
    return False


def check_column_win(playing_board):
    for i in range(len(playing_board)):
        column = [row[i] for row in playing_board]
        if len(set(column)) == 1 and "-" not in column:
            return True
    return False


def check_diagonal_win(playing_board):
    left_diagonal = []
    right_diagonal = []
    left_counter = 0
    right_counter = 2
    for row in playing_board:
        for i in range(len(row)):
            if i == left_counter:
                left_diagonal.append(row[i])
            if i == right_counter:
                right_diagonal.append(row[i])
        left_counter += 1
        right_counter -= 1
    if len(set(left_diagonal)) == 1 and "-" not in left_diagonal:
        return True
    elif len(set(right_diagonal)) == 1 and "-" not in right_diagonal:
        return True
    return False


players = [1, 2]
board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
winner = False
draw = False
turns = 0

print("Welcome to the good old game of Tic-Tac-Toe!")
time.sleep(2)
print("Do you want to see the rules first?")
answer = yes_or_no()
if answer == "yes":
    show_rules()

print()
print("OK, let's kick it!")
print("This is the playing board:")
print()
time.sleep(1)

show_game_board(board)

time.sleep(2)

while True:
    for player in players:
        print(f"Turn of player {player}:")
        coordinates = take_turn_and_validate(board)
        if player == 1:
            board[coordinates[0]][coordinates[1]] = "X"
        else:
            board[coordinates[0]][coordinates[1]] = "O"
        show_game_board(board)
        turns += 1
        if check_row_win(board) or check_column_win(board) or check_diagonal_win(board):
            print(f"Player {player} wins!")
            winner = True
            break
        elif turns == 9:
            print("It's a draw!")
            draw = True
            break

    if winner or draw:
        print("Do you want to play again?")
        answer = yes_or_no()
        if answer == "yes":
            board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
            winner = False
            draw = False
            turns = 0
            print()
            show_game_board(board)
            continue
        else:
            print("See you next time!")
            break