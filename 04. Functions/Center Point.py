def closest_to_center(x_1, y_1, x_2, y_2):
    x_dist = (x_1 ** 2 + y_1 ** 2) ** 0.5
    y_dist = (x_2 ** 2 + y_2 ** 2) ** 0.5
    if x_dist < y_dist or x_dist == y_dist:
        print((int(x_1), int(y_1)))
    elif y_dist < x_dist:
        print((int(x_2), int(y_2)))


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

closest_to_center(x1, y1, x2, y2)