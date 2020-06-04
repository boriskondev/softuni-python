command = input()

initial_list = [int(x) for x in input().split()]

result = 0

if command == "Even":
    result = len(initial_list) * sum([x for x in initial_list if x % 2 == 0])
elif command == "Odd":
    result = len(initial_list) * sum([x for x in initial_list if x % 2 != 0])

print(result)