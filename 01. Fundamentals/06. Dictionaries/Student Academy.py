students = {}

rows = int(input())

for row in range(rows):
    name = input()
    grade = float(input())

    if name not in students:
        students[name] = []
        students[name].append(grade)
    else:
        students[name].append(grade)

averages = {key: sum(value) / len(value) for (key,value) in students.items() if value != 0}

for name_grade in sorted(averages.items(), key=lambda x: x[1], reverse=True):
    if name_grade[1] >= 4.50:
        print(f"{name_grade[0]} -> {name_grade[1]:.2f}")
