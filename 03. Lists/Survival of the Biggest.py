li = input().split()
remove = int(input())

li = list(map(int, li))

for rem in range(remove):
    min_num = min(li)
    li.remove(min_num)

print(li)
