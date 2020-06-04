rooms = int(input())

free_chairs = 0
not_enough = False

for room in range(1, rooms+1):
    chairs_and_places = input().split()
    chairs = chairs_and_places[0].count("X")
    places = int(chairs_and_places[1])
    if chairs < places:
        print(f"{places - chairs} more chairs needed in room {room}")
        not_enough = True
    elif chairs >= places:
        free_chairs += chairs - places

if not not_enough:
    print(f"Game On, {free_chairs} free chairs left")