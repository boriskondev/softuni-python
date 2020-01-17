persons = {}

while True:
    command = input().split(":")
    if command[0] == "Results":
        break
    elif command[0] == "Add":
        person = command[1]
        health = int(command[2])
        energy = int(command[3])
        if person not in persons:
            persons[person] = [health, energy]
        else:
            persons[person][0] += health
    elif command[0] == "Attack":
        attacker_name = command[1]
        defender_name = command[2]
        damage = int(command[3])
        if attacker_name in persons and defender_name in persons:
            persons[defender_name][0] -= damage
            persons[attacker_name][1] -= 1
            if persons[defender_name][0] <= 0:
                print(f"{defender_name} was disqualified!")
                del persons[defender_name]
            if persons[attacker_name][1] <= 0:
                print(f"{attacker_name} was disqualified!")
                del persons[attacker_name]
    elif command[0] == "Delete":
        name_or_all = command[1]
        if name_or_all == "All":
            persons.clear()
        else:
            if name_or_all in persons:
                del persons[name_or_all]

print(f"People count: {len(persons.keys())}")

for person, stats in sorted(persons.items(), key=lambda x: (-x[1][0], x[0])):
    print(f"{person} - {stats[0]} - {stats[1]}")