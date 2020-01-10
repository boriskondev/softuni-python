from itertools import combinations

how_many = int(input("How many people are you? "))

people = {}

for i in range(1, how_many + 1):
    name = input(f"Person {i} name: ")
    expense = float(input(f"Person {i} expense: "))
    people[name] = expense


for first, second in combinations(people.keys(), 2):
    first_takes = people[first] / how_many
    second_takes = people[second] / how_many
    if first_takes > second_takes:
        print(f"{first} should take {(first_takes - second_takes):.2f} from {second}.")
    elif second_takes > first_takes:
        print(f"{second} should take {(second_takes - first_takes):.2f} from {first}.")
    else:
        print(f"{first} and {second} are clear. No one owes anything.")
