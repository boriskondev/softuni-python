capacity = int(input())
people = int(input())

courses = 0

if capacity % people != 0:
    courses += 1

courses += capacity // people

print(courses)