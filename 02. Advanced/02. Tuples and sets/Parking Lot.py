token = input().split(", ")

parking_lot = []

while token[0] != "END":
    direction, number = token
    if direction == "IN":
        parking_lot.append(number)
    elif direction == "OUT":
        if number in parking_lot:
            parking_lot.remove(number)
        else:
            continue
    token = input().split(", ")

if parking_lot:
    [print(c) for c in set(parking_lot)]
else:
    print("Parking Lot is Empty")