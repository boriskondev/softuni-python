def print_matrix(mtr):
    for r in mtr:
        print(" ".join(map(str, r)))


def valid_row(r, mtr_row):
    if r < 0 or r > mtr_row - 1:
        return False
    return True


def valid_col(c, mtr_col):
    if c < 0 or c > mtr_col - 1:
        return False
    return True


matrix = []

rows, columns = [int(x) for x in input().split()]

for row in range(rows):
    matrix.append([x for x in input().split()])

while True:
    command = input().split()
    if command[0] == "END":
        break
    elif command[0] == "swap":
        if len(command[1:]) != 4:
            print("Invalid input!")
        else:
            coordinates = [int(x) for x in command[1:]]
            if valid_row(coordinates[0], rows) and valid_row(coordinates[2], rows) and \
                    valid_col(coordinates[1], columns) and valid_col(coordinates[3], columns):
                matrix[coordinates[0]][coordinates[1]], matrix[coordinates[2]][coordinates[3]] = \
                    matrix[coordinates[2]][coordinates[3]], matrix[coordinates[0]][coordinates[1]]
                print_matrix(matrix)
            else:
                print("Invalid input!")

    else:
        print("Invalid input!")