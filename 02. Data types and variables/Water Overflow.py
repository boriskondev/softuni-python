tank_capacity = 255
times_to_pour = int(input())

counter = 0
total_poured = 0

while counter < times_to_pour:
    pour = int(input())
    if tank_capacity >= pour:
        tank_capacity -= pour
        total_poured += pour
    else:
        print("Insufficient capacity!")
    counter += 1

print(total_poured)