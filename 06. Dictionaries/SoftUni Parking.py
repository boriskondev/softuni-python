parking_lot = {}

parking_spots = int(input())

for spot in range(parking_spots):
    command = input().split()
    if command[0] == "register":
        name = command[1]
        plate = command[2]
        if name not in parking_lot:
            parking_lot[name] = plate
            print(f"{name} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate}")
    elif command[0] == "unregister":
        name = command[1]
        if name not in parking_lot:
            print(f"ERROR: user {name} not found")
        else:
            del parking_lot[name]
            print(f"{name} unregistered successfully")

for k in parking_lot:
    print(f"{k} => {parking_lot[k]}")