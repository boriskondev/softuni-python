# Problem after entering in game 2 (replay)
# After second turn ask if you want to start again


def show_game_board(playing_board):
    for row in playing_board:
        for column in row:
            print(column, end=" ")
        print()
    print()


def take_turn():
    desired_row = int(input("Choose row: "))
    desired_column = int(input("Choose column: "))
    desired_row_index = desired_row - 1
    desired_column_index = desired_column - 1
    coordinates = desired_row_index, desired_column_index
    return coordinates


def check_player_turn(playing_board, coordinates):
    player_row_index = coordinates[0]
    player_column_index = coordinates[1]
    if 0 <= player_row_index <= 2 and 0 <= player_column_index <= 2:
        if playing_board[player_row_index][player_column_index] == "-":
            print()
            return coordinates
    print("Not a valid move. Try again.")
    print()
    return check_player_turn(playing_board, take_turn())


def check_row_win(playing_board):
    for row in playing_board:
        if len(set(row)) == 1 and "-" not in row:
            print(set(row))
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
    if len(set(left_diagonal)) == 1 and "-" not in left_diagonal or len(set(right_diagonal)) == 1 and "-" not in right_diagonal:
        return True
    return False


def yes_or_no():
    positives = ["yes", "ye", "y"]
    negatives = ["no", "n"]
    user_input = input("Yes/No: ").lower()
    if user_input in positives:
        return "yes"
    elif user_input in negatives:
        return "no"
    else:
        print("Not a valid answer. Try again.", end=" ")
        return yes_or_no()


board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
players = [1, 2]
winner = False
draw = False
turns = 0

show_game_board(board)

while True:
    for player in players:
        print(f"Player {player} turn:")
        turn_coordinates = take_turn()
        correct_coordinates = check_player_turn(board, turn_coordinates)
        board[correct_coordinates[0]][correct_coordinates[1]] = str(player)
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
            print()
            show_game_board(board)
            turns = 0
            continue
        else:
            print("See you next time!")
            break