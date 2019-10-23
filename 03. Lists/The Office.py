happiness = list(map(int, input().split()))
factor = int(input())

multiplied_happiness = [x * factor for x in happiness]
average_happiness = sum(multiplied_happiness) / len(multiplied_happiness)
really_happy = len([x for x in multiplied_happiness if x >= average_happiness])
if really_happy >= len(multiplied_happiness) / 2:
    print(f"Score: {really_happy}/{len(multiplied_happiness)}. Employees are happy!")
else:
    print(f"Score: {really_happy}/{len(multiplied_happiness)}. Employees are not happy!")