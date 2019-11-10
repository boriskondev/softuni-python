courses = {}

while True:
    command = input().split(" : ")
    if command[0] == "end":
        break
    course, name = command[0], command[1]
    if course not in courses:
        courses[course] = []
        courses[course].append(name)
    else:
        courses[course].append(name)

for course_info in sorted(courses.items(), key=lambda x: len(x[1]), reverse=True):
    print(f"{course_info[0]}: {len(course_info[1])}")
    [print(f"-- {x}") for x in sorted(course_info[1])]