from itertools import combinations

how_many = int(input("How many people are you? "))

print()

people = {}

for i in range(1, how_many + 1):
    name = input(f"Person {i} name: ")
    expense = float(input(f"Person {i} expenses: "))
    people[name] = [expense, 0]
    print()

for first, second in combinations(people.keys(), 2):
    first_takes = people[first][0] / how_many
    second_takes = people[second][0] / how_many
    if first_takes > second_takes:
        amount_due = first_takes - second_takes
        print(f"{first} should take {amount_due:.2f} leva from {second}.")
        people[first][1] += amount_due
    elif second_takes > first_takes:
        amount_due = second_takes - first_takes
        print(f"{second} should take {amount_due:.2f} leva from {first}.")
        people[second][1] += amount_due
    else:
        print(f"{first} and {second} are clear. No one owes anything.")

print()

print("At the end of the day the situation is:")
for name, details in sorted(people.items(), key=lambda x: x[1][1]):
    print(f"- {name} should receive {details[1]:.2f} leva in total")

# Better mechanics here - not only income, but expense as well?