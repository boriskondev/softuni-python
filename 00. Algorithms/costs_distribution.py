from itertools import combinations

participants = int(input("How many are you? "))

names = []

for participant in range(1, participants + 1):
    name = input(f"Name of person {participant}: ")
    names.append(name)


for combination in list(combinations(names, 2)):
    print(combination)


'''
from itertools import combinations

how_many = int(input("How many are you? "))

people = {}

for i in range(1, how_many + 1):
    name = input(f"Person {i} name: ")
    expense = float(input(f"Person {i} expense: "))
    people[name] = expense


for names in combinations(people.keys(), 2):
    first_taking = people[names[0]] / how_many
    second_taking = people[names[1]] / how_many
    if first_taking > second_taking:
        print(f"{names[0]} should take {(first_taking - second_taking):.2f} from {names[1]}.")
    elif second_taking > first_taking:
        print(f"{names[1]} should take {(second_taking - first_taking):.2f} from {names[0]}.")
    else:
        print(f"{names[0]} and {names[1]} are equal.")
'''