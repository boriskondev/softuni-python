command = input().split("-")

todo = []


def srt(el):
    return el[0]


while command[0] != "End":
    num = int(command[0])
    activity = command[1]
    todo.append((int(command[0]), command[1]))
    command = input().split("-")

todo_sorted = [el[1] for el in sorted(todo, key=srt)]


print(todo_sorted)