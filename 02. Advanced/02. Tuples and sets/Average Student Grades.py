students = int(input())

grade_book = {}

for _ in range(students):
    name, grade = input().split()
    if name not in grade_book:
        grade_book[name] = []
        grade_book[name].append(float(grade))
    else:
        grade_book[name].append(float(grade))

for student in grade_book.items():
    print(f"{student[0]} ->", end=" ")
    [print(f"{grade:.2f}", end=" ") for grade in student[1]]
    average = sum(student[1]) / len(student[1])
    print(f"(avg: {average:.2f})")