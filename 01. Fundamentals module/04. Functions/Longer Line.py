def longer_line(x_11, y_11, x_21, y_21, x_12, y_12, x_22, y_22):
    p1x_side = abs(x_11) + abs(x_21)
    p1y_side = abs(y_11) + abs(y_21)
    p1_diag = (p1x_side ** 2 + p1y_side ** 2) ** 0.5
    p2x_side = abs(x_12) + abs(x_22)
    p2y_side = abs(y_12) + abs(y_22)
    p2_diag = (p2x_side ** 2 + p2y_side ** 2) ** 0.5
    if p1_diag > p2_diag or p1_diag == p2_diag:
        return x_11, y_11, x_21, y_21
    elif p2_diag > p1_diag:
        return x_12, y_12, x_22, y_22


def closest_to_center(tup):
    x_1, y_1, x_2, y_2 = tup
    x_dist = (x_1 ** 2 + y_1 ** 2) ** 0.5
    y_dist = (x_2 ** 2 + y_2 ** 2) ** 0.5
    if x_dist < y_dist or x_dist == y_dist:
        a = int(x_1), int(y_1)
        b = int(x_2), int(y_2)
        return f"{a}{b}"
    elif y_dist < x_dist:
        a = int(x_2), int(y_2)
        b = int(x_1), int(y_1)
        return f"{a}{b}"


x11 = float(input())
y11 = float(input())
x21 = float(input())
y21 = float(input())
x12 = float(input())
y12 = float(input())
x22 = float(input())
y22 = float(input())

closest = longer_line(x11, y11, x21, y21, x12, y12, x22, y22)
rearrange = closest_to_center(closest)

print(rearrange)