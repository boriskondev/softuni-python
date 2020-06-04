def get_magic_triangle(rows):
    result = []
    while rows:
        if len(result) == 0:
            result.append([1])
        elif len(result) == 1:
            result.append([1, 1])
        else:
            row = []
            for i in range(len(result[-1])):
                if i == 0:
                    row.append(1)
                elif i <= len(result[-1]) - 1:
                    row.append(result[-1][i - 1] + result[-1][i])
            row.append(1)
            result.append(row)
        rows -= 1
    return result


[print(row) for row in get_magic_triangle(int(input()))]
